relasi_R = [(1, 1), (2, 2), (1, 2), (2, 1)]
himpunan_A = {1, 2}

refleksif = all((a, a) in relasi_R for a in himpunan_A)
simetris = all((b, a) in relasi_R for (a, b) in relasi_R)
transitif = all((a, c) in relasi_R for (a, b) in relasi_R for (c, d) in relasi_R if b == c)

print("Relasi R:", relasi_R)
print("Refleksif:", refleksif)
print("Simetris:", simetris)
print("Transitif:", transitif)