A = {1, 2, 3, 4}
R = {(1, 1), (2, 2), (3, 3), (4, 4), (1, 2), (2, 3), (1, 3)}

def cek_parsial(HimpunanA, RelasiR):
    RelasiR = set(RelasiR)
    
    # 1. Refleksif: (a, a) harus ada untuk semua a di A
    ref = all((a, a) in RelasiR for a in HimpunanA)
    
    # 2. Antisimetri: Jika (a, b) dan (b, a) ada, maka a harus sama dengan b
    antisim = all((b, a) not in RelasiR for a, b in RelasiR if a != b)
    
    # 3. Transitif: Jika (a, b) dan (b, c) ada, maka (a, c) juga harus ada
    trans = True
    for a, b in RelasiR:
        for x, c in RelasiR:
            if b == x and (a, c) not in RelasiR:
                trans = False
                break
        if not trans:
            break
            
    is_parsial = ref and antisim and trans
    
    return ref, antisim, trans, is_parsial

ref, antisim, trans, hasil = cek_parsial(A, R)

print("Refleksif        :", ref)
print("Antisimetri      :", antisim)
print("Transitif        :", trans)
print("Pengurutan Parsial:", hasil)