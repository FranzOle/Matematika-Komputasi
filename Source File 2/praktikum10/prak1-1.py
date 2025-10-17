def is_valid_partition(original_set, partition):
    # Langkah 1: Gabungkan semua elemen dalam partisi menjadi satu.
    combined_set = set().union(*partition)

    # Langkah 2: Cek dua kondisi utama secara bersamaan.
    # Kondisi A: Apakah gabungan semua partisi sama persis dengan himpunan asli?
    # Kondisi B: Apakah jumlah total elemen di semua partisi (jika dijumlahkan satu per satu)
    is_fully_covered = (combined_set == original_set)
    is_not_overlapping = (sum(len(part) for part in partition) == len(original_set))

    # Jika kedua kondisi terpenuhi maka ini adalah partisi yang valid
    if is_fully_covered and is_not_overlapping:
        return True, "Benar ini merupakan partisi yang valid."
    else:
        return False, "Ini bukan merupakan partisi yang valid."

# Data 
original_set = {'Adam', 'Bella', 'Charlie', 'Deny', 'Dewi', 'Eko', 'Farid'}
partition = [{'Adam', 'Bella', 'Charlie', 'Deny'}, {'Dewi', 'Eko', 'Farid'}]

valid, message = is_valid_partition(original_set, partition)
print(f"Himpunan Asli: {original_set}")
print(f"Partisi yang diuji: {partition}")
print(f"\nHasil: {message} (Status: {valid})")