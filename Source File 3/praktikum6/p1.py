A = {1, 2, 3}
R = [(1, 1), (2, 2), (3, 3), (1, 2), (2, 3)]

is_refleksif = all((a, a) in R for a in A)
is_antisimetri = all((b, a) not in R for (a, b) in R if a != b)
is_transitif = all((a, c) in R for (a, b) in R for (b2, c) in R if b == b2)

is_pengurutan_parsial = is_refleksif and is_antisimetri and is_transitif

print("Apakah R merupakan relasi pengurutan parsial?", is_pengurutan_parsial)