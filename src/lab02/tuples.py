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
    fio_clean = " ".join(fio.split()).strip()
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


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))

print(format_record(("Петров Пётр", "IKBO-12", 5.0)))

print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))

print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))

print(format_record(("  ", "ABB-01", 3.999)))
