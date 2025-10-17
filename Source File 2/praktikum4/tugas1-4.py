from itertools import chain, combinations

def power_set(s):
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

kelas_a = input("List mahasiswa kelas A:").split()

print(f"Himpunan kuasa:", power_set(kelas_a))