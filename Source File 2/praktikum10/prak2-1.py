def verify_proposition(A, B):
    union_result = A.union(B)
    intersection_result = A.intersection(union_result)
    
    return intersection_result == A

A1 = {2, 4, 6}
B1 = {4, 6, 8}
print(f"Menguji A = {A1}, B = {B1}")
print(f"Hasil verifikasi A ∩ (A ∪ B) = A adalah: {verify_proposition(A1, B1)}\n")


A2 = {'apel', 'jeruk', 'mangga'}
B2 = {'mangga', 'pisang', 'anggur'}
print(f"Menguji A = {A2}, B = {B2}")
print(f"Hasil verifikasi A ∩ (A ∪ B) = A adalah: {verify_proposition(A2, B2)}\n")

A3 = {1, 2, 3, 4, 5}
B3 = {2, 3}
print(f"Menguji A = {A3}, B = {B3}")
print(f"Hasil verifikasi A ∩ (A ∪ B) = A adalah: {verify_proposition(A3, B3)}\n")

A4 = {10, 20, 30}
B4 = {40, 50, 60}
print(f"Menguji A = {A4}, B = {B4}")
print(f"Hasil verifikasi A ∩ (A ∪ B) = A adalah: {verify_proposition(A4, B4)}")