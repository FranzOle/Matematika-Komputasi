def intersection():
    matkom = {"Deny", "Budi", "Citra", "Dewi", "Eko"}
    strukdat = {"Budi", "Citra", "Eko", "Farhan", "Gita"}
    mahasiswa_kedua_kelas = matkom.intersection(strukdat)

    print("Mahasiswa yang hadir di kedua kelas")
    print(f"Mahasiswa yang hadir di kedua kelas: {mahasiswa_kedua_kelas} \n")

    mahasiswa_satu_kelas = matkom.symmetric_difference(strukdat)
    print(f"Mahasiswa yang hanya hadir di salah satu kelas: {mahasiswa_satu_kelas} \n")

    total_mahasiswa = matkom.union(strukdat)
    print(f"Total mahasiswa yang hadir di setidaknya di satu kelas adalah: {len(total_mahasiswa)} \n")

    matkom_subset_strukdat = matkom.issubset(strukdat)

    if matkom_subset_strukdat:
        print("Semua mahasiswa yang hadir di Matematika Komputasi juga hadir di Struktur Data.")
    else:
        print("Tidak semua mahasiswa yang hadir di Matematika Komputasi hadir di Struktur Data.")

    if len(matkom) == len(strukdat):
        print("Jumlah mahasiswa yang hadir di kedua kelas sama.")
    else:
        print("Jumlah mahasiswa yang hadir di kedua kelas berbeda.")





if __name__ == "__main__":
    intersection()