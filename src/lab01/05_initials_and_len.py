full_name = input("ФИО: ")

# Обработка строки
cleaned_name = " ".join(full_name.split())  # Убираем лишние пробелы
parts = cleaned_name.split()  # Делим на части по пробелам
print(parts)

# Формируем инициалы в верхнем регистре
initials = "".join(part[0].upper() for part in parts if part)

# Вывод результата
print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len(cleaned_name)}")