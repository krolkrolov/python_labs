def ctf(value):
    return float(value.replace(',', '.'))

a_input = input("a: ").strip()
b_input = input("b: ").strip()

a = ctf(a_input)
b = ctf(b_input)
total = a + b
avg = total / 2

print(f"sum={total:.3f}; avg={avg:.2f}")