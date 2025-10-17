from itertools import chain, combinations

def himpunan_kuasa(s):
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

kelas_musik = {"Andi", "Bima", "Clara"}
kuasa = himpunan_kuasa(kelas_musik)
print(f"Himpunan Kuasa dari himpunan(kelas_musik): {kuasa}")