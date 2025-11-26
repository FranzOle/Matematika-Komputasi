import math

# 1. Fungsi Identitas: f(x) = x
def identitas(x):
    return x

# 2. Fungsi Konstan: f(x) = c
def konstan(x, c):
    return c

# 3. Fungsi Linear: f(x) = ax + b
def linear(x, a, b):
    return a * x + b

# 4. Fungsi Kuadrat: f(x) = ax^2 + bx + c
def kuadrat(x, a, b, c):
    return a * x**2 + b * x + c

# Fungsi untuk mencetak tabel nilai f(x)
def tampilkan_tabel(func, label, *params):
    print(f"\n=== {label} ===")
    print("x\t|\tf(x)")
    print("----------------")
    
    for x in range(-3, 4):
        if params:
            fx = func(x, *params)
        else:
            fx = func(x)
        print(f"{x}\t|\t{fx}")
    print()

# Nilai parameter
a = 1
b = 2
c = 3

# Menampilkan tabel
tampilkan_tabel(identitas, "Fungsi Identitas f(x) = x")
tampilkan_tabel(konstan, f"Fungsi Konstan f(x) = {c}", c)
tampilkan_tabel(linear, f"Fungsi Linear f(x) = {a}x + {b}", a, b)
tampilkan_tabel(kuadrat, f"Fungsi Kuadrat f(x) = {a}x^2 + {b}x + {c}", a, b, c)
