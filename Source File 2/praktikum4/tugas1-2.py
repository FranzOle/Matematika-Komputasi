kelas_a = input("Masukkan nama mahasiswa Kelas A (pisahkan dengan spasi): ").split()
kelas_b = input("Masukkan nama mahasiswa Kelas B (pisahkan dengan spasi): ").split()

set_kelas_a = set(kelas_a)
set_kelas_b = set(kelas_b)

print(f"Mahasiswa Kelas A: {set_kelas_a}")
print(f"Mahasiswa Kelas B: {set_kelas_b}")

if len(set_kelas_a) == len(set_kelas_b):
    print("Hasil: Kedua kelas ekivalen karena jumlah mahasiswanya sama.")
else:
    print("Hasil: Kedua kelas tidak ekivalen karena jumlah mahasiswanya berbeda.")

if set_kelas_a.isdisjoint(set_kelas_b):
    print("Status: Kelas saling lepas (tidak ada mahasiswa yang terdaftar di kedua kelas).")
else:
    print("Status: Kelas tidak saling lepas (ada mahasiswa yang terdaftar di kedua kelas).")