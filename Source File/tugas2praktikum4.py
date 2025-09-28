def analisis_tiga_kelas(strukdat, algoritma):
    strukdat = {s.strip() for s in strukdat}
    algoritma = {a.strip() for a in algoritma}

    print("Analisis Kehadiran Mahasiswa (Struktur Data & Algoritma)")
    print("Mahasiswa yang hadir di semua kelas:", strukdat.intersection(algoritma))
    print("Mahasiswa yang hanya hadir di salah satu kelas:", strukdat.symmetric_difference(algoritma))
    print("Total mahasiswa unik yang hadir minimal di satu kelas:", len(strukdat.union(algoritma)))
    print("Daftar mahasiswa unik:", strukdat.union(algoritma))
    print()


def analisis_subset_equal(matkom, strukdat):
    matkom = {m.strip() for m in matkom}
    strukdat = {s.strip() for s in strukdat}

    print("Analisis Kehadiran Mahasiswa (Matematika Komputasi & Struktur Data)")
    print("Apakah semua mahasiswa Matkom hadir juga di Strukdat?", matkom.issubset(strukdat))
    print("Apakah kedua kelompok memiliki jumlah yang sama?", matkom == strukdat)
    print()


def input_mahasiswa():
    matkom = input("Masukkan nama mahasiswa Matematika Komputasi: ").split(",")
    strukdat = input("Masukkan nama mahasiswa Struktur Data: ").split(",")
    algoritma = input("Masukkan nama mahasiswa Algoritma: ").split(",")

    # Analisis poin 1-3
    analisis_tiga_kelas(strukdat, algoritma)
    # Analisis poin 4-5
    analisis_subset_equal(matkom, strukdat)


if __name__ == "__main__":
    input_mahasiswa()
