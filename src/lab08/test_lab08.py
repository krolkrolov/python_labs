#Тестирование функционала лабораторной работы 8

import os
from models import Student
from serialize import students_to_json, students_from_json

def main():
    print("=== Тестирование класса Student ===\n")
    
    # Создание объектов Student
    try:
        student1 = Student(
            fio="Иванов Иван Иванович",
            birthdate="2003-05-15",
            group="BIVT-01",
            gpa=4.8
        )
        
        student2 = Student(
            fio="Петрова Анна Сергеевна",
            birthdate="2002-11-30",
            group="BIVT-21",
            gpa=3.5
        )

        student3 = Student(
            fio="Петрова Анастасия Сергеевна",
            birthdate="2002-10-30",
            group="BIVT-22",
            gpa=3.5
        )
        
        print("Созданные студенты:")
        print(f"1. {student1}")
        print(f"2. {student2}")
        print(f"3. {student3}")
        
        print(f"\nДополнительная информация:")
        print(f"Студент {student1.fio} - отличник: {student1.is_excellent()}")
        print(f"Студент {student2.fio} - отличник: {student2.is_excellent()}")
        print(f"Студент {student3.fio} - отличник: {student3.is_excellent()}")
        print(f"Курс {student1.fio}: {student1.study_year()}")
        print(f"Курс {student2.fio}: {student2.study_year()}")
        print(f"Курс {student3.fio}: {student3.study_year()}")
        
        # Тестирование сериализации/десериализации
        print("\n=== Тестирование сериализации ===")
        
        # Сериализация в JSON - используем абсолютный путь
        students = [student1, student2, student3]
        
        # Получаем абсолютный путь к data/lab08
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "..", "..", "data", "lab08")
        
        output_path = os.path.join(data_dir, "students_output.json")
        input_path = os.path.join(data_dir, "students_input.json")
        
        students_to_json(students, output_path)
        
        # Десериализация из JSON
        print("\n=== Тестирование десериализации ===")
        loaded_students = students_from_json(input_path)
        
        if loaded_students:
            print("\nЗагруженные студенты:")
            for i, student in enumerate(loaded_students, 1):
                print(f"{i}. {student}")
        else:
            print("Студенты не загружены. Проверьте файл students_input.json")
            
        # Тестирование валидации
        print("\n=== Тестирование валидации ===")
        try:
            bad_student = Student(
                fio="Иванов",  # Только имя
                birthdate="2003-05-15",
                group="SE-01",
                gpa=4.8
            )
        except ValueError as e:
            print(f"Ошибка валидации ФИО: {e}")
            
        try:
            bad_student = Student(
                fio="Иванов Иван Иванович",
                birthdate="2003/05/15",  # Неправильный формат
                group="SE-01",
                gpa=4.8
            )
        except ValueError as e:
            print(f"Ошибка валидации даты: {e}")
            
        try:
            bad_student = Student(
                fio="Иванов Иван Иванович",
                birthdate="2003-05-15",
                group="SE-01",
                gpa=6.0  # Вне диапазона
            )
        except ValueError as e:
            print(f"Ошибка валидации GPA: {e}")
            
        # Проверка существования файлов
        print("\n=== Проверка файлов ===")
        print(f"Файл students_input.json существует: {os.path.exists(input_path)}")
        print(f"Файл students_output.json существует: {os.path.exists(output_path)}")
        if os.path.exists(input_path):
            print(f"Путь к students_input.json: {input_path}")
            
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()