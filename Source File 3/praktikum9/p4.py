def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

nilai_uji = [3, 5, 7]

print("hasil Faktorial (Rekursif)")
for n in nilai_uji:
    print(f"f({n})! = {faktorial(n)}")