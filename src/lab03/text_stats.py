import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "lib"))

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

    print(f"Всего слов: {count_words}")
    print(f"Уникальных слов: {count_words_unique}")
    print()
    print("Топ 5:")
    k = 0
    print(f'{"слово":^15} | {"частота":^15}')
    print(f'{"-"*15}-|-{"-"*15}')
    for word, counts in dict_words_sort:
        if k == 5:
            break
        k += 1
        print(f"{word:^15} | {counts:^15}")


if __name__ == "__main__":
    script()
