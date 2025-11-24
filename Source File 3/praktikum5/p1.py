R = {(1, 2), (2, 3), (3, 4), (4, 5)}
R2 = {("a", "b"), ("b", "c"), ("c", "d")}

def invers_relasi(relasi_asli):
    return {(b, a) for a, b in relasi_asli}

print("Relasi Awal R:", R)
print("Relasi Invers dari R:", invers_relasi(R))

print("\nRelasi Awal R2:", R2)
print("Relasi Invers dari R2:", invers_relasi(R2))