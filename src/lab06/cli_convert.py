import argparse
import os
import sys
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "lib"))

from io_helpers import json_to_csv, csv_to_json, csv_to_xlsx, ensure_parent_dir


def main():
    parser = argparse.ArgumentParser(
        description="Конвертеры данных между форматами",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(
        dest="command", help="Доступные команды конвертации"
    )

    # Подкоманда json2csv
    json2csv_parser = subparsers.add_parser(
        "json2csv", help="Конвертировать JSON в CSV"
    )
    json2csv_parser.add_argument(
        "--in", dest="input", required=True, help="Входной JSON файл"
    )
    json2csv_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной CSV файл"
    )

    # Подкоманда csv2json
    csv2json_parser = subparsers.add_parser(
        "csv2json", help="Конвертировать CSV в JSON"
    )
    csv2json_parser.add_argument(
        "--in", dest="input", required=True, help="Входной CSV файл"
    )
    csv2json_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной JSON файл"
    )

    # Подкоманда csv2xlsx
    csv2xlsx_parser = subparsers.add_parser(
        "csv2xlsx", help="Конвертировать CSV в XLSX"
    )
    csv2xlsx_parser.add_argument(
        "--in", dest="input", required=True, help="Входной CSV файл"
    )
    csv2xlsx_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной XLSX файл"
    )

    args = parser.parse_args()

    try:
        if args.command == "json2csv":
            ensure_parent_dir(args.output)
            json_to_csv(args.input, args.output)
            print(f"Успешно конвертировано: {args.input} -> {args.output}")
        elif args.command == "csv2json":
            ensure_parent_dir(args.output)
            csv_to_json(args.input, args.output)
            print(f"Успешно конвертировано: {args.input} -> {args.output}")
        elif args.command == "csv2xlsx":
            ensure_parent_dir(args.output)
            csv_to_xlsx(args.input, args.output)
            print(f"Успешно конвертировано: {args.input} -> {args.output}")
        else:
            parser.print_help()
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
