A = {1, 2, 3, 4}

# Fungsi awal: f(x) = 2x + 1
def hitung_fungsi_f(x):
    return 2 * x + 1

# Fungsi untuk membuat dictionary (mapping) dari fungsi f
def buat_mapping_f(HimpunanA):
    pemetaan = {}
    for x in HimpunanA:
        # Pasangan (x, f(x))
        pemetaan[x] = hitung_fungsi_f(x)
    return pemetaan

# Fungsi untuk membuat fungsi invers dari mapping
def buat_invers_fungsi(pemetaan_f):
    invers_map = {}
    # Menukar posisi key (x) dan value (f(x))
    for key, value in pemetaan_f.items():
        invers_map[value] = key
    return invers_map

# Langkah 1: Buat fungsi f dalam bentuk dictionary
pemetaan_f = buat_mapping_f(A)

# Langkah 2: Buat fungsi invers
f_invers = buat_invers_fungsi(pemetaan_f)

# Menampilkan hasil fungsi f
print("Fungsi f(x, f(x)):")
for x, y in pemetaan_f.items():
    print(f"f({x}) = {y}")

# Menampilkan hasil fungsi invers
print("\nFungsi invers f^-1 (y, x):")
for y, x in f_invers.items():
    print(f"f^-1({y}) = {x}")