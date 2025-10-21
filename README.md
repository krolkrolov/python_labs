# PYTHON_LABS
## Лабораторная работа 1
### Задание 1
```Python
name = input("Напиши своё имя: ")
age = int(input("Теперь напиши свой возраст: "))
print(f"Привет, {name}! Через год тебе будет {age + 1}")
```


![1-st screen](images/lab01/01ex.png)

---

### Задание 2
```Python
def ctf(value):
    return float(value.replace(',', '.'))

a_input = input("a: ").strip()
b_input = input("b: ").strip()

a = ctf(a_input)
b = ctf(b_input)
total = a + b
avg = total / 2

print(f"sum={total:.2f}; avg={avg:.2f}")
```
![2-nd screen](images/lab01/02.ex.png)

---

### Задание 3
```Python
price = float(input("Введите цену в рублях: "))
discount = float(input("Введите скидку в процентах: "))
vat = float(input("Введите размер НДС в процентах: "))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f"База после скидки: {base:10.2f} ₽")
print(f"НДС: {vat_amount:10.2f} ₽")
print(f"Итого к оплате: {total:10.2f} ₽")
```
![3-rd screen](images/lab01/03ex.png)

---

### Задание 4
```Python
m = int(input("Минуты: "))

hours = m // 60 
minutes = m % 60 

print(f"{hours}:{minutes:02d}")
```
![4-th screen](images/lab01/04ex.png)

---

### Задание 5
```Python
full_name = input("ФИО: ")

cleaned_name = " ".join(full_name.split())
parts = cleaned_name.split()

initials = "".join(part[0].upper() for part in parts if part)

print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len(cleaned_name)}")
```
![5-th screen](images/lab01/05ex.png)

---

### Задание 6*
```Python
n = int(input().strip())
count_offline = 0
count_online = 0

for _ in range(n):
    data = input().split()
    
    if len(data) >= 4:
        format_str = data[-1]
        if format_str == "True":
            count_offline += 1
        elif format_str == "False":
            count_online += 1

print(f"{count_offline} {count_online}")
```
![6-th screen](images/lab01/06ex.png)

---

## Лабораторная работа 2
### Задание 1
```Python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список не может быть пустым")
    return min(nums), max(nums)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    result = []
    for item in mat:
        if not isinstance(item, (list,tuple)):
            raise TypeError(f'Элемент {item} не является списком/кортежем')
        result.extend(item)
    return result
```
![6-th screen](images/lab02/arrays_2.png)
![6-th screen](images/lab02/arrays_1.png)
---
![6-th screen](images/lab02/arrays_3.png)
![6-th screen](images/lab02/arrays_4.png)
---
![6-th screen](images/lab02/arrays_5.png)
![6-th screen](images/lab02/arrays_6.png)

---

### Задание B
```Python
def transpose(mat: list[list[float | int ]]) -> list[list]:
    if not mat:
        return []
    
    row_length = len(mat[0])
    for i, row in enumerate(mat):
        if len(row) != row_length:
            raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидалось {row_length}")
        
    return [[row[j] for row in mat] for j in range(len(mat[0]))]


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    first_row_len = len(mat[0])
    for row in mat:
        if len(row) != first_row_len:
            raise ValueError("Матрица должна быть прямоугольной")

    sums = []
    for row in mat:
        sums.append(sum(row))
    return sums


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    first_row_len = len(mat[0])
    for row in mat:
        if len(row) != first_row_len:
            raise ValueError("Матрица должна быть прямоугольной")
        
    num_cols = len(mat[0])
    sums = []
        
    for j in range(num_cols):
        column_sum = 0
        for row in mat:
            column_sum += row[j]
        sums.append(column_sum)
        
    return sums
```
![6-th screen](images/lab02/matrix_1.png)
![6-th screen](images/lab02/matrix_2.png)
---
![6-th screen](images/lab02/matrix_3.png)
![6-th screen](images/lab02/matrix_4.png)
---
![6-th screen](images/lab02/matrix_5.png)
![6-th screen](images/lab02/matrix_6.png)
---
![6-th screen](images/lab02/matrix_7.png)
![6-th screen](images/lab02/matrix_8.png)

---

### Задание C
```Python
def format_record(rec: tuple[str, str, float]) -> str:
    # Проверка типов
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise TypeError("Запись должна быть кортежем из 3 элементов")
    
    fio, group, gpa = rec
    
    if not isinstance(fio, str):
        raise TypeError("ФИО должно быть строкой")
    if not isinstance(group, str):
        raise TypeError("Группа должна быть строкой")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должно быть числом")
    
    # Обработка и валидация ФИО
    fio_clean = ' '.join(fio.split()).strip() 
    if not fio_clean:
        raise ValueError("ФИО не может быть пустым")
    
    # Обработка и валидация группы
    group_clean = group.strip()
    if not group_clean:
        raise ValueError("Группа не может быть пустой")
    
    # Валидация GPA
    if gpa < 0:
        raise ValueError("GPA не может быть отрицательным")
    
    # Форматирование ФИО с инициалами
    fio_parts = fio_clean.split()
    surname = fio_parts[0].title()
    
    # Формируем инициалы из оставшихся частей (1-2 имени)
    initials = []
    for name_part in fio_parts[1:3]:
        if name_part.strip():
            initials.append(f"{name_part[0].upper()}.")
    
    # Если нет имен, добавляем пустой инициал
    if not initials:
        initials = [""]
    
    fio_formatted = f"{surname} {''.join(initials)}".strip()
    
    # Форматирование GPA с 2 знаками после запятой
    gpa_formatted = f"{gpa:.2f}"
    
    return f"{fio_formatted}, гр. {group_clean}, GPA {gpa_formatted}"
```
![6-th screen](images/lab02/tuples_1.png)
![6-th screen](images/lab02/tuples_2.png)
---
![6-th screen](images/lab02/tuples_3.png)
![6-th screen](images/lab02/tuples_4.png)

---

## Лабораторная работа 3
### Задание A
```Python
import re
from collections import Counter
from typing import Dict, List, Tuple


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if yo2e:
        text = text.replace('Ё', 'Е').replace('ё', 'е')
    
    if casefold:
        text = text.casefold()
    
    text = re.sub(r'[\t\r\n]', ' ', text)
    
    text = ''.join(char for char in text if char.isprintable() or char.isspace())
    
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def tokenize(text: str) -> List[str]:
    tokens = re.findall(r'\b[\w-]+\b', text)
    return tokens


def count_freq(tokens: List[str]) -> Dict[str, int]:
    return dict(Counter(tokens))


def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
```
![6-th screen](images/lab03/text01.png)
![6-th screen](images/lab03/text02.png)
---
![6-th screen](images/lab03/text03.png)
![6-th screen](images/lab03/text04.png)
---
![6-th screen](images/lab03/text05.png)
![6-th screen](images/lab03/text06.png)

---

### Задание B
```Python
import sys
import os

# Добавляем путь к папке lib перед импортом
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from text import normalize, tokenize, count_freq, top_n

def script():
    text = input()
    # Получаем список всех словс
    text_corrected = tokenize(normalize(text))
    # Считаем общее кол-во слов
    count_words = len(text_corrected)
    # Получаем словарь уникальных слов
    dict_words = count_freq(text_corrected)
    # Считаем кол-во уникальных слов
    count_words_unique = len(dict_words)
    # Сортируем словарь по кол-ву слов
    dict_words_sort = top_n(dict_words)

    print(f'Всего слов: {count_words}')
    print(f'Уникальных слов: {count_words_unique}')
    print()
    print('Топ 5:')
    k = 0
    print(f'{"слово":^15} | {"частота":^15}')
    print(f'{"-"*15}-|-{"-"*15}')
    for word, counts in dict_words_sort:
        if k == 5:
            break
        k += 1
        print(f'{word:^15} | {counts:^15}')

if __name__ == "__main__":
    script()
```
![6-th screen](images/lab03/text07.png)

---

## Лабораторная работа 4
### Описание

Реализован модуль для анализа текстовых файлов и генерации отчетов о частоте слов в формате CSV.

---

### Задание A — модуль src/lab04/io_txt_csv.py
Код:
```Python
import csv
from pathlib import Path
from typing import Iterable, Sequence


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
```
#### Тесты:
1) Тест для read_text():

Код проверки:

![6-th screen](images/lab04/lab04(7).png)

input.txt:

![6-th screen](images/lab04/lab04(1).png)

Консоль:

![6-th screen](images/lab04/lab04(8).png)
---
2)  Тест для write_csv():

Код проверки:

![6-th screen](images/lab04/lab04(9).png)

test1.csv:

![6-th screen](images/lab04/lab04(10).png)

Консоль:

![6-th screen](images/lab04/lab04(11).png)
---
3)  Тест для ensure_parent_dir():

Код проверки:

![6-th screen](images/lab04/lab04(12).png)

Созданные дирректории:

![6-th screen](images/lab04/lab04(14).png)

Консоль:

![6-th screen](images/lab04/lab04(13).png)
---

### Задание B — скрипт src/lab04/text_report.py
Код:
```Python
import sys
from pathlib import Path
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from text import normalize, tokenize

from io_txt_csv import read_text, write_csv


def frequencies_from_text(text: str) -> dict[str, int]:
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    return Counter(tokens)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def print_summary(freq: dict[str, int], top_n: int = 5) -> None:
    total_words = sum(freq.values())
    unique_words = len(freq)
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    
    if unique_words > 0:
        sorted_words = sorted_word_counts(freq)
        top_words = sorted_words[:top_n]
        print(f"Топ-{top_n}: {', '.join(f'{word}({count})' for word, count in top_words)}")


def main():
    try:
        # Чтение входного файла
        input_file = Path("data/lab04/input.txt")
        text = read_text(input_file)
        
        # Вычисление частот
        freq = frequencies_from_text(text)
        
        # Подготовка данных для CSV
        sorted_counts = sorted_word_counts(freq)
        csv_data = [(word, count) for word, count in sorted_counts]
        
        # Запись отчета
        output_file = Path("data/lab04/report.csv")
        write_csv(csv_data, output_file, header=("word", "count"))
        
        # Вывод статистики
        print_summary(freq)
        print(f"\nОтчет сохранен в: {output_file}")
        
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
#### Обработка входного файла

Скрипт поддерживает два способа указания входного файла:

##### 1. Хардкодированный путь (по умолчанию)
Если запустить скрипт без параметров, он автоматически использует файл:
`data/lab04/input.txt`


**Пример:**
```bash
python src/lab04/text_report.py
```

#### 2. Через параметры командной строки
Можно указать произвольный входной файл с помощью параметра `--in`:

Пример:
```bash
python src/lab04/text_report.py --in data/my_text.txt
python src/lab04/text_report.py --in /full/path/to/file.txt
```
##### Приоритет использования:

1) Если указан параметр `--in` - используется указанный файл

2) Если параметр не указан - используется хардкодированный путь data/lab04/input.txt

##### Обработка ошибок:

1) Если файл не существует - выводится ошибка и скрипт завершается

2) Рекомендуется использовать относительные пути от корня проекта

#### Использование входного файла

**По умолчанию:** скрипт читает файл `data/lab04/input.txt`

**С указанием файла:** использовать параметр `--in`
```bash
python src/lab04/text_report.py --in data/my_file.txt
```
---

### Тест-кейсы text_report

#### A. Один файл (база):

1) Вход (data/input.txt):

![6-th screen](images/lab04/lab04(1).png)

2) Полученный report.csv:

![6-th screen](images/lab04/lab04(3).png)

3) Консоль:

![6-th screen](images/lab04/lab04(2).png)

#### B. Пустой файл:

1) Вход:

![6-th screen](images/lab04/lab04(4).png)

2) Полученный report.csv:

![6-th screen](images/lab04/lab04(6).png)

3) Консоль:

![6-th screen](images/lab04/lab04(5).png)