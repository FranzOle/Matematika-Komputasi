# Fungsi pertama: f(x) = 2x + 3
def hitung_f(x):
    return 2 * x + 3

# Fungsi kedua: g(x) = x^2
def hitung_g(x):
    return x**2

# Fungsi untuk menghitung komposisi f(g(x))
def komposisi_fg(f, g, x):
    # Hitung g(x) (fungsi dalam/inner)
    nilai_dalam = g(x)
    # Masukkan hasil g(x) ke f
    return f(nilai_dalam)

# Menghitung (f o g)(x)
print("Hasil (f o g)(x) yaitu f(g(x)):")
for x in [1, 2, 3]:
    # Hitung komposisi f(g(x))
    hasil_fg = komposisi_fg(hitung_f, hitung_g, x)
    print(f"f(g({x})) = {hasil_fg}")

# Menghitung (g o f)(x)
print("\nHasil (g o f)(x) yaitu g(f(x)):")
for x in [1, 2, 3]:
    # Hitung komposisi g(f(x))
    # Note: Bisa juga memanggil g(f(x)) secara langsung
    hasil_gf = hitung_g(hitung_f(x)) 
    print(f"g(f({x})) = {hasil_gf}")