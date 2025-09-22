m = int(input("Минуты: "))

hours = m // 60  # целое деление для часов
minutes = m % 60  # остаток от деления для минут

print(f"{hours}:{minutes:02d}")