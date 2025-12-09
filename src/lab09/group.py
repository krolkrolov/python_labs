import csv
from pathlib import Path
from typing import List
import sys
import os

# Добавляем путь к lab08 в sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from lab08.models import Student
except ImportError:
    # Альтернативный путь
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from lab08.models import Student

class Group:
    """Класс для работы с хранилищем студентов в CSV-файле"""
    
    def __init__(self, storage_path: str):
        """
        Инициализация группы с путем к CSV-файлу
        
        Args:
            storage_path: путь к CSV-файлу с данными студентов
        """
        self.path = Path(storage_path)
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self):
        """Создает файл с заголовком, если его еще нет"""
        if not self.path.exists():
            # Создаются родительские директории если их нет
            self.path.parent.mkdir(parents=True, exist_ok=True)
            # Создаем файл с заголовком
            with open(self.path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
                writer.writeheader()
            print(f"Создан новый файл хранилища: {self.path}")
    
    def _read_all(self) -> List[dict]:
        """
        Чтение всех записей из CSV файла
        
        Returns:
            Список словарей с данными студентов
        """
        if not self.path.exists() or self.path.stat().st_size == 0:
            return []
        
        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    
    def _write_all(self, rows: List[dict]):
        """
        Запись всех записей в CSV файл
        
        Args:
            rows: список словарей с данными студентов
        """
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(rows)
    
    def list(self) -> List[Student]:
        """
        Получение всех студентов в виде объектов Student
        
        Returns:
            Список объектов Student
        """
        rows = self._read_all()
        students = []
        errors = []
        
        for i, row in enumerate(rows, 1):
            try:
                # Преобразуем строковые значения в правильные типы
                row['gpa'] = float(row['gpa'])
                student = Student.from_dict(row)
                students.append(student)
            except (ValueError, KeyError) as e:
                errors.append(f"Строка {i}: {e}")
                continue
        
        if errors:
            print(f"Обнаружены ошибки при чтении студентов:")
            for error in errors:
                print(f"  - {error}")
        
        return students
    
    def add(self, student: Student):
        """
        Добавление нового студента в CSV
        
        Args:
            student: объект Student для добавления
        """
        # Читаем существующие данные
        rows = self._read_all()
        
        # Проверяем, нет ли уже студента с таким ФИО
        for row in rows:
            if row['fio'].strip().lower() == student.fio.strip().lower():
                print(f"Студент с ФИО '{student.fio}' уже существует")
                return False
        
        # Добавляем нового студента
        rows.append(student.to_dict())
        
        # Записываем обратно
        self._write_all(rows)
        print(f"Студент '{student.fio}' успешно добавлен")
        return True
    
    def find(self, substr: str) -> List[Student]:
        """
        Поиск студентов по подстроке в ФИО
        
        Args:
            substr: подстрока для поиска в ФИО
            
        Returns:
            Список найденных студентов
        """
        all_students = self.list()
        substr_lower = substr.strip().lower()
        
        found = [
            student for student in all_students 
            if substr_lower in student.fio.lower()
        ]
        
        print(f"Найдено {len(found)} студентов по запросу '{substr}'")
        return found
    
    def remove(self, fio: str) -> bool:
        """
        Удаление записи(ей) с данным ФИО
        
        Args:
            fio: ФИО студента для удаления
            
        Returns:
            True если удаление прошло успешно, False если студент не найден
        """
        rows = self._read_all()
        initial_count = len(rows)
        
        # Удаляем всех студентов с таким ФИО (регистронезависимо)
        fio_lower = fio.strip().lower()
        rows = [row for row in rows if row['fio'].strip().lower() != fio_lower]
        
        if len(rows) < initial_count:
            self._write_all(rows)
            removed_count = initial_count - len(rows)
            print(f"Удалено {removed_count} студентов с ФИО '{fio}'")
            return True
        else:
            print(f"Студент с ФИО '{fio}' не найден")
            return False
    
    def update(self, fio: str, **fields):
        """
        Обновление полей существующего студента
        
        Args:
            fio: ФИО студента для обновления
            **fields: поля для обновления (например, gpa=4.8, group='БИВТ-21-2')
            
        Returns:
            True если обновление прошло успешно, False если студент не найден
        """
        rows = self._read_all()
        updated = False
        fio_lower = fio.strip().lower()
        
        for row in rows:
            if row['fio'].strip().lower() == fio_lower:
                # Обновляем указанные поля
                for key, value in fields.items():
                    if key in row:
                        row[key] = value
                        updated = True
                
                # Если есть изменения, обновляем строку
                if updated:
                    # Валидируем обновленные данные
                    try:
                        # Создаем временный студент для валидации
                        temp_row = row.copy()
                        temp_row['gpa'] = float(temp_row['gpa'])
                        Student.from_dict(temp_row)
                    except ValueError as e:
                        print(f"Ошибка валидации обновленных данных: {e}")
                        return False
        
        if updated:
            self._write_all(rows)
            print(f"Данные студента '{fio}' успешно обновлены")
            return True
        else:
            print(f"Студент с ФИО '{fio}' не найден")
            return False
    
    def stats(self) -> dict:
        """
        Сбор статистики по студентам (дополнительное задание со звездочкой)
        
        Returns:
            Словарь со статистикой
        """
        students = self.list()
        
        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": []
            }
        
        # Базовая статистика
        gpa_values = [student.gpa for student in students]
        groups_count = {}
        
        for student in students:
            group = student.group
            groups_count[group] = groups_count.get(group, 0) + 1
        
        # Топ-5 студентов по GPA
        sorted_students = sorted(students, key=lambda x: x.gpa, reverse=True)
        top_5 = [
            {"fio": s.fio, "gpa": s.gpa}
            for s in sorted_students[:5]
        ]
        
        return {
            "count": len(students),
            "min_gpa": min(gpa_values) if gpa_values else None,
            "max_gpa": max(gpa_values) if gpa_values else None,
            "avg_gpa": sum(gpa_values) / len(gpa_values) if gpa_values else None,
            "groups": groups_count,
            "top_5_students": top_5
        }