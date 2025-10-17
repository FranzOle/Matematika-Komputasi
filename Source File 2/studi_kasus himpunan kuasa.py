from itertools import chain, combinations

def himpunan_kuasa(s):
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

kursus = {"Denny", "Budi", "Citra"}
kuasa = himpunan_kuasa(kursus)
print(f"Himpunan Kuasa: {kuasa}")