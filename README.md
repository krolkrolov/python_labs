# PYTHON_LABS
## Лабораторная работа 1
### Задание 1
```Python
name = input("Напиши своё имя: ")
age = int(input("Теперь напиши свой возраст: "))
print(f"Привет, {name}! Через год тебе будет {age + 1}")
```


![1-st screen](images/lab01/01ex.png)

---

### Задание 2
```Python
def ctf(value):
    return float(value.replace(',', '.'))

a_input = input("a: ").strip()
b_input = input("b: ").strip()

a = ctf(a_input)
b = ctf(b_input)
total = a + b
avg = total / 2

print(f"sum={total:.2f}; avg={avg:.2f}")
```
![2-nd screen](images/lab01/02.ex.png)

---

### Задание 3
```Python
price = float(input("Введите цену в рублях: "))
discount = float(input("Введите скидку в процентах: "))
vat = float(input("Введите размер НДС в процентах: "))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f"База после скидки: {base:10.2f} ₽")
print(f"НДС: {vat_amount:10.2f} ₽")
print(f"Итого к оплате: {total:10.2f} ₽")
```
![3-rd screen](images/lab01/03ex.png)

---

### Задание 4
```Python
m = int(input("Минуты: "))

hours = m // 60 
minutes = m % 60 

print(f"{hours}:{minutes:02d}")
```
![4-th screen](images/lab01/04ex.png)

---

### Задание 5
```Python
full_name = input("ФИО: ")

cleaned_name = " ".join(full_name.split())
parts = cleaned_name.split()

initials = "".join(part[0].upper() for part in parts if part)

print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len(cleaned_name)}")
```
![5-th screen](images/lab01/05ex.png)

---

### Задание 6*
```Python
n = int(input().strip())
count_offline = 0
count_online = 0

for _ in range(n):
    data = input().split()
    
    if len(data) >= 4:
        format_str = data[-1]
        if format_str == "True":
            count_offline += 1
        elif format_str == "False":
            count_online += 1

print(f"{count_offline} {count_online}")
```
![6-th screen](images/lab01/06ex.png)

---

## Лабораторная работа 2