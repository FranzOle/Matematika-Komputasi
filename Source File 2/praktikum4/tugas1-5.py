kalkulus = input("List Mahasiswa Kalkulus:").split()
fisika_dasar = input("List Mahasiswa Fisika Dasar:").split()

print(f"Mahasiswa Kalkulus:", kalkulus)
print(f"Mahasiswa Fisika Dasar:", fisika_dasar)

set_kalkulus = set(kalkulus)
set_fisika = set(fisika_dasar)

gabungan = set_kalkulus.union(set_fisika)
irisan = set_kalkulus.intersection(set_fisika)
selisih = set_kalkulus.difference(set_fisika)
himpunan_semesta = set_kalkulus.union(set_fisika)
komplemen_kalkulus = himpunan_semesta.difference(set_kalkulus)
komplemen_fisika = himpunan_semesta.difference(set_fisika)

print(f"Gabungan:", gabungan)
print(f"Irisan:", irisan)
print(f"Selisih (Kalkulus - Fisika Dasar):", selisih)
print(f"Komplemen Kalkulus:", komplemen_kalkulus)
print(f"Komplemen Fisika Dasar:", komplemen_fisika)