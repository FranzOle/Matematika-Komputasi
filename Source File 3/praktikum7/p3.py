R = {
    ("Andi", "Matematika", 90),
    ("Budi", "Fisika", 85),
    ("Citra", "Kimia", 88)
}

def tampilkan_relasi_tiga_ary(Relasi):
    # Cetak header tabel dengan rataan kolom
    print(f"{'Mahasiswa':<12} {'Mata Kuliah':<12} {'Nilai':>5}")
    print("-" * 32)
    
    # Cetak setiap baris data
    for mahasiswa, mata_kuliah, nilai in Relasi:
        print(f"{mahasiswa:<12} {mata_kuliah:<12} {nilai:>5}")
    print()

print("Relasi awal:")
tampilkan_relasi_tiga_ary(R)

# Tambahkan beberapa data baru
R.add(("Dina", "Biologi", 92))
R.add(("Eko", "Matematika", 75))

print("Relasi setelah penambahan data:")
tampilkan_relasi_tiga_ary(R)