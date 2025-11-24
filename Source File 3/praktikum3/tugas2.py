import numpy as np

def buat_relasi(A, B, aturan):
    return [(a, b) for a in A for b in B if b == aturan(a)]

A = [1, 2, 3, 4]
B = [2, 4, 6, 8]

relasi_ganda = buat_relasi(A, B, lambda a: 2*a)
print("Relasi b = 2a:", relasi_ganda)

relasi_kuadrat = buat_relasi(A, B, lambda a: a**2)
print("Relasi b = a^2:", relasi_kuadrat)