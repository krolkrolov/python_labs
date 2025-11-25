import argparse
import sys
import os
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "lib"))

from text import normalize, tokenize, count_freq, top_n
from io_helpers import read_text


def main():
    parser = argparse.ArgumentParser(
        description="CLI-утилиты для работы с текстом",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    # Подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # Подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Анализ частот слов в тексте")
    stats_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    stats_parser.add_argument(
        "--top", type=int, default=5, help="Количество топ-слов (по умолчанию: 5)"
    )

    args = parser.parse_args()

    try:
        if args.command == "cat":
            content = read_text(args.input, encoding="utf-8")
            lines = content.split("\n")

            for i, line in enumerate(lines, 1):
                if args.n:
                    print(f"{i:6d}\t{line}")
                else:
                    print(line)

        elif args.command == "stats":
            content = read_text(args.input, encoding="utf-8")

            # функции из lab03
            normalized_text = normalize(content)
            tokens = tokenize(normalized_text)
            frequency = count_freq(tokens)
            top_words = top_n(frequency, args.top)

            # Дополнительная статистика
            total_words = len(tokens)
            unique_words = len(frequency)

            print(f"Статистика для файла: {args.input}")
            print("=" * 40)
            print(f"Всего слов: {total_words}")
            print(f"Уникальных слов: {unique_words}")
            print()
            print(f"Топ-{args.top} самых частых слов:")
            print("-" * 30)
            print(f'{"Слово":^15} | {"Частота":^10}')
            print(f'{"-"*15}-|-{"-"*10}')
            for i, (word, count) in enumerate(top_words, 1):
                print(f"{word:^15} | {count:^10}")

            # Дополнительно: процентное соотношение
            if total_words > 0:
                print()
                print("Процентное соотношение:")
                for word, count in top_words:
                    percentage = (count / total_words) * 100
                    print(f"{word}: {percentage:.1f}%")
        else:
            parser.print_help()
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
