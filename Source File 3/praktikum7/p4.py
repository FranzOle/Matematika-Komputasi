A = {1, 2, 3, 4}
B = {2, 4, 6, 8}
R = {(1, 2), (2, 4), (3, 6), (4, 8)}

def cek_fungsi(HimpunanA, HimpunanB, RelasiR):
    # Ubah relasi R ke set untuk mempermudah pengecekan
    RelasiR = set(RelasiR)
    pemetaan = {}

    # Periksa apakah ada elemen A yang memiliki lebih dari satu pasangan
    for a, b in RelasiR:
        # Pastikan domain (a) dan kodomain (b) ada di himpunannya
        if a not in HimpunanA or b not in HimpunanB:
            return False
            
        # Jika a sudah punya pasangan sebelumnya (lebih dari 1 output)
        if a in pemetaan and pemetaan[a] != b:
            return False
        else:
            pemetaan[a] = b
            
    # Pastikan setiap elemen di Himpunan A punya tepat 1 pasangan
    for a in HimpunanA:
        if a not in pemetaan:
            return False

    return True

hasil = cek_fungsi(A, B, R)

print("Relasi R:", R)
print("Apakah R merupakan fungsi dari A ke B?", hasil)