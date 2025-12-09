#Тестирование лабораторной работы 9


import sys
import os
from pathlib import Path

# Добавляем src в путь для импорта
current_dir = Path(__file__).parent
src_dir = current_dir / 'src'
sys.path.insert(0, str(src_dir))

try:
    from lab08.models import Student
    from lab09.group import Group
except ImportError as e:
    print(f"Ошибка импорта: {e}")
    print("Проверьте, что файлы lab08 находятся в правильной директории")
    print("Текущий путь Python:")
    for p in sys.path:
        print(f"  {p}")
    sys.exit(1)

def main():
    """Основная функция тестирования"""
    
    # Путь к файлу с данными
    csv_path = "data/lab09/students.csv"
    
    # Создаем директорию если её нет
    Path(csv_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Создаем объект группы
    print("=" * 50)
    print("Создаем объект Group")
    print("=" * 50)
    group = Group(csv_path)
    
    # 1. Добавляем студентов
    print("\n1. Добавление студентов:")
    print("-" * 30)
    
    students_to_add = [
        Student("Иванов Иван Иванович", "2003-10-10", "БИВТ-21-1", 4.3),
        Student("Петрова Анна Сергеевна", "2002-05-15", "БИВТ-21-2", 4.8),
        Student("Сидоров Алексей Петрович", "2003-12-20", "БИВТ-21-1", 3.9),
        Student("Кузнецова Мария", "2001-08-03", "БИС-21-3", 4.5),
        Student("Смирнов Дмитрий", "2004-02-28", "БИВТ-21-1", 4.1),
    ]
    
    for student in students_to_add:
        group.add(student)
        print(f"Добавлен: {student}")
    
    # 2. Выводим всех студентов
    print("\n2. Список всех студентов:")
    print("-" * 30)
    all_students = group.list()
    for student in all_students:
        print(student)
    
    # 3. Поиск студентов
    print("\n3. Поиск студентов по подстроке 'Ива':")
    print("-" * 30)
    found_students = group.find("Ива")
    for student in found_students:
        print(student)
    
    # 4. Обновление данных студента
    print("\n4. Обновление данных студента 'Иванов Иван Иванович':")
    print("-" * 30)
    group.update("Иванов Иван Иванович", gpa=4.7, group="БИВТ-21-2")
    
    # Проверяем обновление
    print("\n5. Проверяем обновление (поиск 'Иванов'):")
    print("-" * 30)
    ivanov = group.find("Иванов")
    for student in ivanov:
        print(student)
    
    # 6. Удаление студента
    print("\n6. Удаление студента 'Кузнецова Мария':")
    print("-" * 30)
    group.remove("Кузнецова Мария")
    
    # 7. Итоговый список
    print("\n7. Итоговый список студентов:")
    print("-" * 30)
    final_students = group.list()
    for student in final_students:
        print(student)
    
    # 8. Статистика (дополнительное задание)
    print("\n8. Статистика по группе:")
    print("-" * 30)
    stats = group.stats()
    
    print(f"Всего студентов: {stats['count']}")
    print(f"Минимальный GPA: {stats['min_gpa']:.2f}")
    print(f"Максимальный GPA: {stats['max_gpa']:.2f}")
    print(f"Средний GPA: {stats['avg_gpa']:.2f}")
    
    print("\nКоличество студентов по группам:")
    for group_name, count in stats['groups'].items():
        print(f"  {group_name}: {count}")
    
    print("\nТоп-5 студентов по GPA:")
    for i, student in enumerate(stats['top_5_students'], 1):
        print(f"  {i}. {student['fio']} - {student['gpa']:.2f}")
    
    # 9. Показываем содержимое CSV файла
    print("\n9. Содержимое CSV файла:")
    print("-" * 30)
    with open(csv_path, 'r', encoding='utf-8') as f:
        print(f.read())

if __name__ == "__main__":
    main()