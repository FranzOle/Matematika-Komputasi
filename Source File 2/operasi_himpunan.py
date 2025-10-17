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