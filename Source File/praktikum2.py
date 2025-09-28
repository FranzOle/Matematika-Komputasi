
def identity_law():
    print("Hukum Identitas:")
    p = True
    print(f"Hasil dari p AND True = {p and True}")
    print(f"Hasil dari p OR False = {p or False}\n")


def commutative_law():
    print("Hukum Komutatif:")
    p = True
    q = False
    print(f"Hasil dari p AND q = {p and q}")
    print(f"Hasil dari q AND p = {q and p}")
    print(f"Hasil dari p OR q = {p or q}")
    print(f"Hasil dari q OR p = {q or p}\n")

def associative_law():
    print("Hukum Asosiatif:")
    p = True
    q = False
    r = True
    print(f"Hasil dari (p AND q) AND r = {(p and q) and r}")
    print(f"Hasil dari p AND (q AND r) = {p and (q and r)}")
    print(f"Hasil dari (p OR q) OR r = {(p or q) or r}")
    print(f"Hasil dari p OR (q OR r) = {p or (q or r)}\n")

def distributive_law():
    print("Hukum Distributif:")
    p = True
    q = False
    r = True
    print(f"Hasil dari p AND (q OR r) = {p and (q or r)}")
    print(f"Hasil dari (p AND q) OR (p AND r) = {(p and q) or (p and r)}")
    print(f"Hasil dari p OR (q AND r) = {p or (q and r)}")
    print(f"Hasil dari (p OR q) AND (p OR r) = {(p or q) and (p or r)}\n")

def converse():
    print("Hukum Konvers (Converse):")
    p = True
    q = False
    print(f"Hasil dari q → p = {(not q) or p}\n")

def inverse():
    print("Hukum Invers (Inverse):")
    p = True
    q = False
    print(f"Hasil dari ¬p → ¬q = {not p}->{not q}\n")

def contrapositive():
    print("Hukum Kontrapositif (Contrapositive):")
    p = True
    q = False
    print(f"Hasil dari ¬q → ¬p = {not q}->{not p}\n")

def modus_ponens():
    print("Modus Ponens:")
    p = True
    q = True

    print(f"Premis 1: p = {p}")
    print(f"Premis 2: p → q = {(not p) or q}")
    print(f"Kesimpulan: q = {q}\n")

def modus_tollens():
    print("Modus Tollens:")
    p = True
    q = False

    print(f"Premis 1: ¬q = {not q}")
    print(f"Premis 2: p → q = {(not p) or q}")
    print(f"Kesimpulan: ¬p = {not p}\n")

def syllogism():
    print("Silogisme:")
    p = True
    q = True
    r = False

    print(f"Premis 1: p → q = {p} -> {r} \n")



if __name__ == "__main__":
    print("=== Hukum Logika Proporsional,Variasi Proposisi Kondisional,Teori Logika Inferensi dan Validitas ===\n")
    identity_law()
    commutative_law()
    associative_law()
    distributive_law()

    converse()
    inverse()
    contrapositive()

    modus_ponens()
    modus_tollens()
    syllogism()