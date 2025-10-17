from collections import Counter

print("PROGRAM PENGHITUNG KEMUNCULAN ELEMEN MULTISET")
print("="*45)

user_input_str = input(
    "Masukkan elemen-elemen multiset (pisahkan dengan koma)\n"
    "Contoh: Nasi Goreng, Nasi Goreng, Sate, Sate, Soto\n\n"
    "Input: "
)

multiset_from_input = [item.strip() for item in user_input_str.split(',')]

print("\n" + "--- HASIL PERHITUNGAN MULTISET ---")

total_elements = len(multiset_from_input)
print(f"Total elemen dalam multiset: {total_elements}")

element_counts = Counter(multiset_from_input)

print("\nJumlah kemunculan setiap elemen:")
for element, count in element_counts.items():
    print(f"'{element}': {count} kali")

print(f"\nBentuk dictionary: {dict(element_counts)}")

print("\n" + "="*45)
print("=== UJI COBA DENGAN DATA BERBEDA ===")
print("="*45)

print("\nTest Case 1: Data dari soal")
test_case_1 = ['Nasi Goreng', 'Nasi Goreng', 'Sate', 'Sate', 'Sate', 'Soto']
counts_1 = Counter(test_case_1)
print("--- HASIL PERHITUNGAN MULTISET ---")
print(f"Total elemen dalam multiset: {len(test_case_1)}")
print("\nJumlah kemunculan setiap elemen:")
for element, count in counts_1.items():
    print(f"'{element}': {count} kali")
print(f"\nBentuk dictionary: {dict(counts_1)}")

print("\nTest Case 2: Menu makanan beragam")
test_case_2 = ['Bakso', 'Bakso', 'Gado-gado', 'Rendang', 'Rendang', 'Rendang', 'Soto', 'Soto']
counts_2 = Counter(test_case_2)
print("--- HASIL PERHITUNGAN MULTISET ---")
print(f"Total elemen dalam multiset: {len(test_case_2)}")
print("\nJumlah kemunculan setiap elemen:")
for element, count in counts_2.items():
    print(f"'{element}': {count} kali")
print(f"\nBentuk dictionary: {dict(counts_2)}")

print("\nTest Case 3: Satu jenis makanan dominan")
test_case_3 = ['Mie Ayam', 'Mie Ayam', 'Mie Ayam', 'Mie Ayam', 'Es Teh', 'Es Teh']
counts_3 = Counter(test_case_3)
print("--- HASIL PERHITUNGAN MULTISET ---")
print(f"Total elemen dalam multiset: {len(test_case_3)}")
print("\nJumlah kemunculan setiap elemen:")
for element, count in counts_3.items():
    print(f"'{element}': {count} kali")
print(f"\nBentuk dictionary: {dict(counts_3)}")