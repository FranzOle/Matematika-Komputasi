A = [1, 2, 3, 4]
B = [2, 4, 6, 8]
R = {(1, 2), (2, 4), (3, 6), (4, 8)}

def tampilkan_tabel_relasi(A, B, R):
    print("  ", end="")
    for b in B:
        print(f"{b:>3}", end="")
    print()

    for a in A:
        print(f"{a:>3}", end=" ")
        for b in B:
            if (a, b) in R:
                print(" ✔ ", end="")
            else:
                print(" - ", end="")
        print()

tampilkan_tabel_relasi(A, B, R)