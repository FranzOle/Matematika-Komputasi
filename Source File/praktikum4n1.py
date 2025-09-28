def define_sets():
    print("Definisi Set Himpunan:")
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    
    print(f"Set A: {A}")
    print(f"Set B: {B}")

def representation_of_sets():
    print("Remove duplicate dari himpunana")
    C = {1, 2, 2, 3, 4, 4, 5}
    print(f"Set C (dengan duplikat): {{1, 2, 2, 3, 4, 4, 5}}")
    print(f"Set C (tanpa duplikat): {C} \n")

def cardinality_of_sets():
    A = {1, 2, 3, 4, 5}
    print(f"Kardinalitas Set A: {len(A)}\n")

def empty_set():
    empty_set = set()
    print(f"Empty set: {empty_set} \n")

def check_subsets():
    set_E = {1, 2, 3}
    set_F = {1, 2, 3, 4, 5}
    is_subset = set_E.issubset(set_F) 
    print(f"Is Set E a subset of Set F? {is_subset} \n")

def check_equal_sets():
    set_G = {1, 2, 3}
    set_H = {3, 1, 2}
    are_equal = set_G == set_H 
    print(f"Are Set G and Set H equal? {are_equal}")

if __name__ == "__main__":
    print("Set Theory\n")
    define_sets()
    print("\n")
    representation_of_sets()
    cardinality_of_sets()
    empty_set()
    check_subsets()
    check_equal_sets()
