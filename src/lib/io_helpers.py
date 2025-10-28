import json
import csv
from pathlib import Path
from openpyxl import Workbook
from typing import Iterable, Sequence

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



def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    csv_file = Path(csv_path)
    
    # Проверка существования файла
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    # Чтение CSV
    try:
        with csv_file.open('r', encoding='utf-8') as f:
            # Просто читаем все строки CSV
            reader = csv.reader(f)
            data = list(reader)
            
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    
    # Валидация данных
    if not data:
        raise ValueError("CSV файл пуст")
    
    # Проверяем что есть хотя бы одна строка (заголовок)
    if len(data) == 0:
        raise ValueError("CSV файл должен содержать заголовок")
    
    # Создание XLSX
    try:
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"
        
        # Запись данных
        for row in data:
            ws.append(row)
        
        # Авто-ширина колонок (не менее 8 символов)
        for column in ws.columns:
            max_length = 0
            column_letter = column[0].column_letter
            
            for cell in column:
                try:
                    cell_value = str(cell.value) if cell.value is not None else ""
                    if len(cell_value) > max_length:
                        max_length = len(cell_value)
                except:
                    pass
            
            adjusted_width = max(max_length + 2, 8)  # Минимум 8 символов
            ws.column_dimensions[column_letter].width = adjusted_width
        
        wb.save(xlsx_path)
        
    except Exception as e:
        raise ValueError(f"Ошибка создания XLSX: {e}")



def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)



def write_csv(rows: Iterable[Sequence], path: str | Path, 
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    
    if rows:
        first_length = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_length:
                raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидается {first_length}")
    
    ensure_parent_dir(p)
    
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)


def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)


