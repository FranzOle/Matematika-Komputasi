A = {1, 2, 3}
R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}

def cek_sifat_relasi(HimpunanA, RelasiR):
    is_refleksif = all((a, a) in RelasiR for a in HimpunanA)
    
    is_simetris = True
    for a, b in RelasiR:
        if (b, a) not in RelasiR:
            is_simetris = False
            break
            
    is_antisimetris = True
    for a, b in RelasiR:
        if (b, a) in RelasiR and a != b:
            is_antisimetris = False
            break

    is_transitif = True
    for a, b in RelasiR:
        for x, c in RelasiR:
            if b == x and (a, c) not in RelasiR:
                is_transitif = False
                break
        if not is_transitif:
            break
            
    return is_refleksif, is_simetris, is_antisimetris, is_transitif

ref, sym, antisym, trans = cek_sifat_relasi(A, R)

print("Refleksif  :", ref)
print("Simetris   :", sym)
print("Antisimetris:", antisym)
print("Transitif  :", trans)