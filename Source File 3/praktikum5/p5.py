H = {1, 2, 3, 4}
R = {(1, 1), (2, 2), (3, 3), (4, 4), (1, 3), (3, 1)}
R_coba = {(1, 1), (2, 2), (3, 3), (1, 2)}

def cek_sifat(H, R_uji):
    ref = all((a, a) in R_uji for a in H)
    
    sim = True
    for a, b in R_uji:
        if (b, a) not in R_uji:
            sim = False
            break
            
    antisim = True
    for a, b in R_uji:
        if (b, a) in R_uji and a != b:
            antisim = False
            break
            
    trans = True
    for a, b in R_uji:
        for x, c in R_uji:
            if b == x and (a, c) not in R_uji:
                trans = False
                break
        if not trans:
            break
            
    return ref, sim, antisim, trans

def cek_setara(H, R_uji):
    ref, sim, antisim, trans = cek_sifat(H, R_uji)
    
    print("Refleksif  :", ref)
    print("Simetris   :", sim)
    print("Transitif  :", trans)
    print("Antisimetris:", antisim)
    
    if ref and sim and trans:
        print("Kesimpulan: R ini ADALAH relasi kesetaraan.")
    else:
        print("Kesimpulan: R ini BUKAN relasi kesetaraan.")

print(">>> Uji Relasi R Soal <<<")
cek_setara(H, R)

print("\n>>> Uji Relasi R_coba Lain <<<")
cek_setara(H, R_coba)