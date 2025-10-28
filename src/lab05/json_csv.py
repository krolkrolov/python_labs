import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — алфавитный.
    """
    json_file = Path(json_path)
    
    # Проверка существования файла
    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    
    # Чтение JSON
    try:
        with json_file.open('r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка декодирования JSON: {e}")
    except Exception as e:
        raise ValueError(f"Ошибка чтения файла: {e}")
    
    # Валидация данных
    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")
    
    # Определение всех возможных полей (алфавитный порядок)
    fieldnames = set()
    for item in data:
        fieldnames.update(item.keys())
    fieldnames = sorted(fieldnames)
    
    if not fieldnames:
        raise ValueError("JSON не содержит полей для преобразования")
    
    # Запись CSV
    try:
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                # Заполняем отсутствующие поля пустыми строками
                complete_row = {field: str(row.get(field, '')) for field in fieldnames}
                writer.writerow(complete_row)
    except Exception as e:
        raise ValueError(f"Ошибка записи CSV: {e}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    """
    csv_file = Path(csv_path)
    
    # Проверка существования файла
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    # Чтение CSV
    try:
        with csv_file.open('r', encoding='utf-8') as f:
            # Пробуем прочитать как CSV с заголовком
            reader = csv.DictReader(f)
            data = list(reader)
            
    except csv.Error as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    except Exception as e:
        raise ValueError(f"Ошибка обработки CSV: {e}")
    
    # Валидация данных
    if not data:
        raise ValueError("CSV файл пуст или не содержит данных")
    
    # Проверяем что есть поля (значит был заголовок)
    if not reader.fieldnames:
        raise ValueError("CSV файл должен содержать заголовок")
    
    # Запись JSON
    try:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")