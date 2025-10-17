citrakara_fakultas_teknik = input("Masukkan nama mahasiswa CitraKara Fakultas Teknik (pisahkan dengan spasi): ").split()
batara_fakultas_vokasi = input("Masukkan nama mahasiswa Batara Fakultas Vokasi (pisahkan dengan spasi): ").split()

set_citrakara = set(citrakara_fakultas_teknik)
set_batara = set(batara_fakultas_vokasi)

print(f"CitraKara Fakultas Teknik: {set_citrakara}")
print(f"Batara Fakultas Vokasi: {set_batara}")

is_saling_lepas = set_citrakara.isdisjoint(set_batara)

if is_saling_lepas:
    print("Kedua himpunan saling lepas (tidak ada mahasiswa yang hadir di kedua acara)")
else:
    print("Kedua himpunan tidak saling lepas (ada mahasiswa yang hadir di kedua acara)")