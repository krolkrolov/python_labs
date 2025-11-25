price = float(input("Введите цену в рублях: "))
discount = float(input("Введите скидку в процентах: "))
vat = float(input("Введите размер НДС в процентах: "))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"База после скидки: {base:10.2f} ₽")
print(f"НДС: {vat_amount:10.2f} ₽")
print(f"Итого к оплате: {total:10.2f} ₽")
