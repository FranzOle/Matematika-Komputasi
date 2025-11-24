A = {1, 2, 3}
B = {4, 5, 6}
f = {(1, 4), (2, 5), (3, 6)}

is_fungsi = len(f) == len(A)

is_injektif = len({b for _, b in f}) == len(f)

is_surjektif = {b for _, b in f} == B

print("Apakah f adalah fungsi?", is_fungsi)
print("Apakah f injektif?", is_injektif)
print("Apakah f surjektif?", is_surjektif)