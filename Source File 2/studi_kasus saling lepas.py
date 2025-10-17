matkom = {"Denny", "Budi", "Citra", "Dewi"}
strukdat = {"Eko", "Farhan", "Gita", "Hadi"}

def cek_himpunan_lepas(set_a, set_b):
    return set_a.isdisjoint(set_b)

if cek_himpunan_lepas(matkom, strukdat):
    print("Kedua himpunan saling lepas")
else:
    print("Kedua himpunan memiliki nilai yang sama")