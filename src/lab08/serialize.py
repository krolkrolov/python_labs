import json
from pathlib import Path
from typing import List

try:
    from models import Student  # Для запуска из той же директории
except ImportError:
    from .models import Student  # Для импорта как модуля

def students_to_json(students: List[Student], path: str) -> None:
    """
    Сериализация списка студентов в JSON файл
    """
    data = [student.to_dict() for student in students]
    
    # Создаем директорию если ее нет
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Данные сохранены в файл: {path}")
    print(f"Сохранено {len(students)} студентов")

def students_from_json(path: str) -> List[Student]:
    """
    Десериализация списка студентов из JSON файла
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        students = []
        errors = []
        
        for i, item in enumerate(data, 1):
            try:
                student = Student.from_dict(item)
                students.append(student)
            except (ValueError, KeyError) as e:
                errors.append(f"Строка {i}: {e}")
                continue
        
        if errors:
            print(f"Обнаружены ошибки при загрузке:")
            for error in errors:
                print(f"  - {error}")
        
        print(f"Загружено {len(students)} студентов из файла {path}")
        return students
        
    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return []
    except json.JSONDecodeError:
        print(f"Некорректный JSON в файле: {path}")
        return []