A = {1, 2, 3}
R = {(1, 2), (2, 3)}

def klosur_refleksif(A, R):
    # Salin relasi awal R
    R_klosur = set(R)
    # Tambahkan (a, a) untuk setiap a di A
    for a in A:
        R_klosur.add((a, a))
    return R_klosur

def klosur_simetris(R):
    # Salin relasi awal R
    R_klosur = set(R)
    # Untuk setiap pasangan (a, b), tambahkan (b, a)
    for a, b in list(R_klosur):
        if (b, a) not in R_klosur:
            R_klosur.add((b, a))
    return R_klosur

def klosur_transitif(R):
    # Salin relasi awal R
    R_klosur = set(R)
    changed = True
    
    # Ulangi proses sampai tidak ada pasangan baru yang ditambahkan
    while changed:
        changed = False
        new_pairs = set()
        
        # Cari rantai (a, b) dan (b, c) untuk menambahkan (a, c)
        for a, b in R_klosur:
            for x, c in R_klosur:
                if b == x and (a, c) not in R_klosur:
                    new_pairs.add((a, c))
                    
        # Jika ada pasangan baru, tambahkan dan ulangi
        if new_pairs:
            R_klosur.update(new_pairs)
            changed = True
            
    return R_klosur

print("Relasi awal R =", R)
print("-" * 30)

R_ref = klosur_refleksif(A, R)
print("Klosur Refleksif :", R_ref)

R_sym = klosur_simetris(R)
print("Klosur Simetris  :", R_sym)

R_trans = klosur_transitif(R)
print("Klosur Transitif :", R_trans)