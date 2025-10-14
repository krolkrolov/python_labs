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

### Задание B
```Python
import sys
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




# from text import normalize, tokenize, count_freq, top_n

import io
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')


def main():
    text = sys.stdin.read().strip()
    
    if not text:
        print("Ошибка: ввод пустой")
        return
    
    clean_text = normalize(text)
    words = tokenize(clean_text)
    
    if not words:
        print("Ошибка: нет слов для анализа")
        return
    
    total = len(words)
    unique = len(set(words))
    freqs = count_freq(words)
    top_words = top_n(freqs, 5)
    
    print(f"Всего слов: {total}")
    print(f"Уникальных слов: {unique}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
```
![6-th screen](images/lab03/text07.png)