full_name = input("ФИО: ")

cleaned_name = " ".join(full_name.split())
parts = cleaned_name.split()

initials = "".join(part[0].upper() for part in parts if part)

print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len(cleaned_name)}")