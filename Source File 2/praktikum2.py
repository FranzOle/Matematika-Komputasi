def equivalent_sets():
    print("Himpunan yang Ekuivalen")
    set_a = {1,2,3,4}
    set_b = {5,6,7,8}

    are_equivalent = len(set_a) == len(set_b)
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Apakah kedua himpunan Ekivalen? {are_equivalent}")
    print("\n")

def disjoint_sets():
    print("Himpunan Saling Lepas")
    set_a = {1,2,3}
    set_b = {4,5,6}
    are_disjoint = set_a.isdisjoint(set_b)
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Apakah kedua himpunan saling lepas? {are_disjoint}")
    print("\n")

def power_set(s):
    print("Himpunan Kuasa")
    from itertools import chain, combinations
    def power_set_generator(s):
        return list(chain.from_iterable(combinations(s,r) for r in range(len(s)+1)))

    p_set = power_set_generator(s)
    print(f"Himpunan:{s}")
    print(f"Himpunan Kuasa: {p_set}")
    print("\n")

def set_operations():
    set_a = {1,2,3,4}
    set_b = {3,4,5,6}

    himpunan_semesta = set_a.union(set_b)

    union = set_a.union(set_b)

    intersection = set_a.intersection(set_b)

    difference = set_a.difference(set_b)

    complement_a = himpunan_semesta.difference(set_a)
    complement_b = himpunan_semesta.difference(set_b)

    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Gabungan (A ∪ B): {union}")
    print(f"Irisan (A ∩ B): {intersection}")
    print(f"Selisih (A - B): {difference}")
    print(f"Komplemen A: (Semesta - A): {complement_a}")
    print(f"Komplemen B: (Semesta - B): {complement_b}")
    print("\n")

equivalent_sets()
disjoint_sets()
power_set({1,2,3})
set_operations()
print("\n")