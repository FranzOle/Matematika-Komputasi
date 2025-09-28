def teori_himpunan():
    himpunan_a = {1, 2, 3, 4, 5}
    himpunan_b = set([4, 5, 6, 7, 8])

    print(f"Himpunan A: {himpunan_a}")
    print(f"Himpunan B: {himpunan_b}")

def kardinalitas_himpunan():
    himpunan_a = {1, 2, 3, 4, 5}
    print(f"Kardinalitas Himpunan A: {len(himpunan_a)}")

def himpunan_kosong():
    himpunan_kosong = set()
    print(f"Himpunan Kosong: {himpunan_kosong}")

def sub_himpunan():
    himpunan_a = {1, 2, 3}
    himpunan_b = {1, 2, 3,}

    print(f"Himpunan A adalah subhimpunan dari Himpunan B {himpunan_a.issubset(himpunan_b)}")

def himpunan_sama():
    himpunan_a = {1, 2, 3}
    himpunan_b = {1, 2, 3}

    print(f"Himpunan A sama dengan Himpunan B {himpunan_a == himpunan_b}")
    
if __name__ == "__main__":
    print("Himpunan \n")
    teori_himpunan() 
    print("\n")
    kardinalitas_himpunan()
    print("\n")
    himpunan_kosong()
    print("\n")
    sub_himpunan()
    print("\n")
    himpunan_sama()

    print("\n")