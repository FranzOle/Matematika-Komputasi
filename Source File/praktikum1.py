def propotional_logic():
    print("Proportional Logic \n")
    # deklarasi proposisi
    p = True
    q = False
    print(f"Proposisi p: {p}")
    print(f"Proposisi q: {q}")
    print(f"Negasi p: {not p}")
    print(f"Konjungsi p dan q bernilai: {p and q}") 
    print(f"Disjungsi p dan q bernilai: {p or q}\n")

def conjunction():
    print("Konjungsi \n")
    # deklarasi proposisi
    p = True
    q = True
    print(f" p: {p}, q: {q}, Konjungsi p dan q bernilai: {p and q} \n")

def disjunction():
    print("Disjungsi \n")
    # deklarasi proposisi
    p = True
    q = True
    print(f"p: {p}, q: {q}, Disjungsi p dan q bernilai: {p or q} \n")

def implication():
    print("Implikasi (p → q) \n")
    # deklarasi proposisi
    p = True
    q = False
    print(f"p: {p}, q: {q}, Implikasi p → q bernilai: {(not p) or q} \n")

def biconditional():
    print("Bikondisional (p ↔ q) \n")
    # deklarasi proposisi
    p = True
    q = False
    print(f"p: {p}, q: {q}, Bikondisional p ↔ q bernilai: {(p and q) or (not p or q)} \n")

def exclusive_disjunction():
    print("Disjungsi Eksklusif (XOR) \n")
    # deklarasi proposisi
    p = True
    q = False
    print(f"p: {p}, q: {q}, XOR p ⊕ q bernilai: {p != q} \n")

def combine_propositions():
    print("Kombinasi Proposisi \n")
    # deklarasi proposisi
    p = True
    q = False
    r = True
    #(p ∧ q) ∨ r
    print(f"p: {p}, q: {q}, r: {r}, (p ∧ q) ∨ r bernilai: {(p and q) or r}")
    #(p ∨ q) → r
    print(f"p: {p}, q: {q}, r: {r}, (p ∨ q) → r bernilai: {(not (p or q)) or r} \n")


def truth_table():
    print("=== Truth Table ===")
    print("p\tq\tp AND q\tp OR q\tnot p\tp -> q\tp <-> q")
    print("===================================================")   
    for p in [True, False]:
        for q in [True, False]:
            conjunction = p and q
            disjunction = p or q
            negation_p = not p
            implication = (not p) or q
            biconditional = (p and q) or (not p and not q)

            print(f"{p}\t{q}\t{conjunction}\t{disjunction}\t{negation_p}\t{implication}\t{biconditional}") 
    print("===================================================")


if __name__ == "__main__":
    propotional_logic()
    conjunction()
    disjunction()
    implication()
    
    biconditional()
    exclusive_disjunction()
    combine_propositions()
    truth_table()

