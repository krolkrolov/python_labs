import pytest
import json
import csv
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from lab05.json_csv import json_to_csv, csv_to_json


class TestJsonToCsv:
    """Тесты для json_to_csv"""

    @pytest.mark.parametrize(
        "data,expected",
        [
            ([{"name": "Алиса", "age": 25}], [{"name": "Алиса", "age": "25"}]),
            (
                [{"name": "Алиса"}, {"name": "Боб", "city": "СПб"}],
                [{"name": "Алиса", "city": ""}, {"name": "Боб", "city": "СПб"}],
            ),
        ],
    )
    def test_json_to_csv(self, tmp_path, data, expected):
        """Позитивные тесты JSON -> CSV"""
        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "test.csv"

        json_file.write_text(json.dumps(data), encoding="utf-8")
        json_to_csv(str(json_file), str(csv_file))

        with csv_file.open("r", encoding="utf-8") as f:
            assert list(csv.DictReader(f)) == expected

    @pytest.mark.parametrize(
        "content,error",
        [
            ("{invalid}", "Ошибка декодирования"),
            ('{"name": "Алиса"}', "список объектов"),
            ("[]", "Пустой JSON"),
        ],
    )
    def test_json_to_csv_errors(self, tmp_path, content, error):
        """Негативные тесты JSON -> CSV"""
        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "test.csv"

        json_file.write_text(content, encoding="utf-8")
        with pytest.raises(ValueError, match=error):
            json_to_csv(str(json_file), str(csv_file))

    def test_json_to_csv_not_found(self):
        """Тест несуществующего файла"""
        with pytest.raises(FileNotFoundError):
            json_to_csv("nonexistent.json", "out.csv")


class TestCsvToJson:
    """Тесты для csv_to_json"""

    @pytest.mark.parametrize(
        "rows,expected",
        [
            ([{"name": "Алиса", "age": "25"}], [{"name": "Алиса", "age": "25"}]),
            ([{"name": "Алиса", "age": ""}], [{"name": "Алиса", "age": ""}]),
        ],
    )
    def test_csv_to_json(self, tmp_path, rows, expected):
        """Позитивные тесты CSV -> JSON"""
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "test.json"

        with csv_file.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)

        csv_to_json(str(csv_file), str(json_file))

        with json_file.open("r", encoding="utf-8") as f:
            assert json.load(f) == expected

    def test_csv_to_json_errors(self, tmp_path):
        """Негативные тесты CSV -> JSON"""
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "test.json"

        # Пустой файл
        csv_file.write_text("", encoding="utf-8")
        with pytest.raises(ValueError, match="пуст"):
            csv_to_json(str(csv_file), str(json_file))

    def test_csv_to_json_not_found(self):
        """Тест несуществующего файла"""
        with pytest.raises(FileNotFoundError):
            csv_to_json("nonexistent.csv", "out.json")


class TestRoundTrip:
    """Тесты полного цикла"""

    def test_round_trip(self, tmp_path):
        """JSON -> CSV -> JSON"""
        data = [{"name": "Алиса", "age": 25}]

        # JSON -> CSV -> JSON
        json1 = tmp_path / "1.json"
        csv_file = tmp_path / "test.csv"
        json2 = tmp_path / "2.json"

        json1.write_text(json.dumps(data), encoding="utf-8")
        json_to_csv(str(json1), str(csv_file))
        csv_to_json(str(csv_file), str(json2))

        # Проверяем что данные сохранились
        with json2.open("r", encoding="utf-8") as f:
            result = json.load(f)

        assert len(result) == len(data)
        assert result[0]["name"] == "Алиса"
