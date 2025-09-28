def biconditional_logic():
    print("Logika Bikondisional (Bi-Implikasi) \n")
    # deklarasi proposisi
    p = True
    q = False
    print(f"Proposisi p: {p}")
    print(f"Proposisi q: {q}")
    biconditonal = (p and q) or (not p and not q)
    print(f"Bikondisional p ↔ q bernilai: {biconditonal}\n")

def inference():
    print("Logika Inferensi \n")
    # deklarasi proposisi
    p =  True
    q = False
    implication = not p or q
    print(f"Proposisi p: {p}")
    print(f"Proposisi q: {q}")
    print(f"Implikasi p → q bernilai: {implication} \n")

    if p and implication:
        print(f"Dari p dan p → q, maka q bernilai {q} \n") 


def argument():
    print("Argumen:")
    p = True
    q = False
    r = True

    print(f"Proposisi p: {p}")
    print(f"Proposisi q: {q}")
    print(f"Proposisi r: {r}")
    print(f"Premis 1 (p → q): {(not p) or q}")
    print(f"Premis 2 (q → r): {(not q) or r}")
    print(f"Kesimpulan (p → r): {(not p) or r}\n")

def axiom_theorems():
    print("Teorema Aksioma")
    
    aksioma = True
    print(f"Aksioma: {aksioma}")

    teorema = aksioma and True
    print(f"Teorema: {teorema}")

    lemma = teorema
    print(f"Lemma: {lemma}")

    corollary = teorema
    print(f"Corollary: {corollary}\n")

if __name__ == "__main__":
    biconditional_logic()
    inference()
    argument() 
    axiom_theorems()

