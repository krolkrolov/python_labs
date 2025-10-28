import sys
from pathlib import Path

# Добавляем путь к src для импорта модулей
sys.path.append(str(Path(__file__).parent / 'src'))

from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx

def main():
    print("=== Тестирование Lab 5 ===")
    
    try:
        # 1. JSON → CSV
        print("1. Тест JSON → CSV...")
        json_to_csv('data/lab05/samples/people.json', 'data/lab05/out/people_from_json.csv')
        print("   ✓ Успешно создан: data/out/people_from_json.csv")
        
        # 2. CSV → JSON  
        print("2. Тест CSV → JSON...")
        csv_to_json('data/lab05/samples/people.csv', 'data/lab05/out/people_from_csv.json')
        print("   ✓ Успешно создан: data/out/people_from_csv.json")
        
        # 3. CSV → XLSX
        print("3. Тест CSV → XLSX...")
        csv_to_xlsx('data/lab05/samples/people.csv', 'data/lab05/out/people.xlsx')
        print("   ✓ Успешно создан: data/out/people.xlsx")
        
        # 4. Дополнительный тест с cities.csv
        print("4. Тест cities.csv → XLSX...")
        csv_to_xlsx('data/lab05/samples/cities.csv', 'data/lab05/out/cities.xlsx')
        print("   ✓ Успешно создан: data/out/cities.xlsx")
        
        print("\n🎉 Все тесты пройдены успешно!")
        
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")

if __name__ == "__main__":
    main()