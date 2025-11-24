A = [1, 2, 3, 4]
B = [2, 4, 6, 8]
R = {(1, 2), (2, 4), (3, 6), (4, 8)}

def buat_matriks_relasi(A, B, R):
    matriks = []
    for a in A:
        baris = []
        for b in B:
            if (a, b) in R:
                baris.append(1)
            else:
                baris.append(0)
        matriks.append(baris)
    return matriks

hasil = buat_matriks_relasi(A, B, R)
print(hasil)