import math

# 1. Fungsi Identitas: f(x) = x
def identitas(x):
    # Mengembalikan nilai x apa adanya
    return x

# 2. Fungsi Konstan: f(x) = c
def konstan(x, c):
    # Nilai fungsi selalu sama berapa pun x
    return c

# 3. Fungsi Linear: f(x) = ax + b
def linear(x, a, b):
    # Fungsi garis lurus dengan gradien a dan intercept b
    return a * x + b

# 4. Fungsi Kuadrat: f(x) = ax^2 + bx + c
def kuadrat(x, a, b, c):
    # Membentuk parabola
    return a * x**2 + b * x + c

# Fungsi untuk mencetak tabel nilai f(x)
def tampilkan_tabel(func, label, *params):
    print(f"\n=== {label} ===")
    print("x\t|\tf(x)")
    print("----------------")
    
    # Hitung dari x = -3 sampai x = 3
    for x in range(-3, 4):
        # Memanggil fungsi dengan parameter yang sesuai
        fx = func(x, *params)
        print(f"{x}\t|\t{fx}")
    print()

# Nilai parameter awal yang bisa diubah untuk eksplorasi
a = 1
b = 2
c = 3

# Menampilkan tabel untuk setiap jenis fungsi
tampilkan_tabel(identitas, "Fungsi Identitas f(x) = x", None) # Parameter c/a/b/c tidak dipakai
tampilkan_tabel(konstan, f"Fungsi Konstan f(x) = {c}", c) # Hanya butuh c
tampilkan_tabel(linear, f"Fungsi Linear f(x) = {a}x + {b}", a, b) # Butuh a dan b
tampilkan_tabel(kuadrat, f"Fungsi Kuadrat f(x) = {a}x^2 + {b}x + {c}", a, b, c) # Butuh a, b, c