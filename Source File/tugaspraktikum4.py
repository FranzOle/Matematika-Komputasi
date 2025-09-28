
def analisis_kelas(matkom, strukdat):
    matkom = {m.strip() for m in matkom}
    strukdat = {s.strip() for s in strukdat}

    print("Analisis Kehadiran Mahasiswa")
    print("Mahasiswa yang hadir di kedua kelas:", matkom.intersection(strukdat))
    print("Mahasiswa yang hanya hadir di salah satu kelas:", matkom.symmetric_difference(strukdat))
    print("Total mahasiswa (unik) yang hadir minimal di satu kelas:", len(matkom.union(strukdat)))
    print("Daftar mahasiswa:", matkom.union(strukdat))

def analisis_algo_basisdata(algo, basisdata):
    algo = {a.strip() for a in algo}    
    basisdata = {b.strip() for b in basisdata}

    print("Analisis Kehadiran Mahasiswa Algoritma dan Basis Data")
    print("Mahasiswa yang hadir di kedua kelas:", algo.intersection(basisdata))
    print("Mahasiswa yang hanya hadir di salah satu kelas:", algo.symmetric_difference(basisdata))
    print("Total mahasiswa (unik) yang hadir minimal di satu kelas:", len(algo.union(basisdata)))
    print("Daftar mahasiswa:", algo.union(basisdata))


def input_mahasiswa():
    matkom = input("Masukkan nama mahasiswa Matematika Komputasi: ").split(",")
    strukdat = input("Masukkan nama mahasiswa Struktur Data: ").split(",")

    analisis_kelas(matkom, strukdat)

def input_algo_basisdata():
    algo = input("Masukkan nama mahasiswa Algoritma: ").split(",")
    basisdata = input("Masukkan nama mahasiswa Basis Data: ").split(",")
    analisis_algo_basisdata(algo, basisdata)

if __name__ == "__main__":
    # input_mahasiswa()
    input_algo_basisdata()
