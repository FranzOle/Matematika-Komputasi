def converse(p, q):
    print("Hukum Konvers (Converse):")
    result = (not q) or p
    print(f"Hasil dari q → p = {result}\n")

def inverse(p, q):
    print("Hukum Invers (Inverse):")
    result = (not p) or (not q)
    print(f"Hasil dari ¬p → ¬q = {result}\n")

def contrapositive(p, q):
    print("Hukum Kontrapositif (Contrapositive):")
    result = (not (not q)) or (not p)  
    print(f"Hasil dari ¬q → ¬p = {result}\n")

if __name__ == "__main__":
    while True:
        p = input("Masukkan nilai p (True/False): ").strip().lower() == "true"
        q = input("Masukkan nilai q (True/False): ").strip().lower() == "true"

        converse(p, q)
        inverse(p, q)
        contrapositive(p, q)

        ulang = input("Coba lagi? (y/n): ").strip().lower()
        if ulang != "y":
            print("Program selesai.")
            break