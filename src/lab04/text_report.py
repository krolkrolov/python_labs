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