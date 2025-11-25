import csv
from pathlib import Path

try:
    from openpyxl import Workbook
except ImportError:
    raise ImportError("Требуется установить openpyxl: pip install openpyxl")


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
        with csv_file.open("r", encoding="utf-8") as f:
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
