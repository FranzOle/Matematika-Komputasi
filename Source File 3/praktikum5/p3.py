R = {(1, 2), (2, 3), (3, 4)}
S = {(2, 5), (3, 6), (4, 7)}

def hitung_komposisi(RelasiSatu, RelasiDua):
    komposisi = set()
    for a, b in RelasiSatu:
        for x, c in RelasiDua:
            if b == x:
                komposisi.add((a, c))
    return komposisi

hasil = hitung_komposisi(R, S)

print("Relasi R:", R)
print("Relasi S:", S)
print("Komposisi R o S:", hasil)