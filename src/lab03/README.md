# Задание B: Анализ текстовой статистики

## Описание
Программа для анализа текстовой статистики: подсчет общего количества слов, уникальных слов и вывод топ-5 самых частых слов.

## Функциональность
- Нормализация текста (приведение к нижнему регистру)
- Токенизация текста (разбиение на слова)
- Подсчет частоты слов
- Вывод статистики:
  - Общее количество слов
  - Количество уникальных слов
  - Топ-5 самых частых слов

## Код
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
### Запуск программы
```bash
python text_stats.py
```

