A = {1, 2, 3}
relasi = [(a, b) for a in A for b in A if a < b]
print("Pasangan dalam relasi 'lebih kecil dari':", relasi)