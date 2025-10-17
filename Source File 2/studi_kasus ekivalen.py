kursus_a = {"Deni", "Budi", "Citra", "Dewi"}
kursus_b = {"Fahri", "Gina", "Hadi", "Ira"}

def cek_himpunan_ekivalen(set_a, set_b):
    return len(set_a) == len(set_b)

if cek_himpunan_ekivalen(kursus_a, kursus_b):
    print("Kedua himpunan Ekivalen")
else:
    print("Kedua himpunan tidak ekivalen")