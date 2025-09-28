def opbicondtional(work_hours, is_late):
   return (work_hours > 8) == (not is_late)

def opinferensi(is_raining):
    # Jika hujan, maka tanah basah
    if is_raining:
        return "Tanah basah"
    else:
        return "Tanah Kering"
    
def opargumen(nilai):
   if nilai > 75:
        return "Lulus"
   else:
        return "Tidak Lulus"


def opakasioma(n):
    return n % 2 == 0

def oplemma(n):
    return opakasioma(n)

def opteorema(a, b):
    return opakasioma(a + b)

def opcorollary(a, b):
    return opakasioma(a + b)

if __name__ == "__main__":
   print("`=== Studi Kasus Praktikum 3 ===\n")

   print("4. Studi Kasus Aksioma, Teorema, Lemma, dan Corollary")
   a = 4
   b = 6

   print(f"Aksioma: {a} adalah bilangan genap? {opakasioma(a)}")
   print(f"Lemma: {b} adalah kelipatan 2? {oplemma(b)}")
   print(f"Teorema: Jumlah {a} dan {b} adalah bilangan genap? {opteorema(a, b)}")

   c = 3
   d = 5
   print(f"Corollary: Jumlah {c} dan {d} adalah bilangan genap? {opcorollary(c, d)} \n")

   print("3. Studi Kasus Argumen")
   nilai = 85
   result = opargumen(nilai)
   print(f"Nilai: {nilai}, Hasil Argumen: {result} \n")

   print("2. Studi Kasus Inferensi")
   is_raining = True  
   result = opinferensi(is_raining)
   print(f"Hasil Inferensi: {result} \n")

   print("1. Studi Kasus Bikondisional")
   work_hours = 9
   is_late = False
   result = opbicondtional(work_hours, is_late)

   if result:
      print("Karyawan mendapat bonus \n")
   else:
      print("Karyawan tidak mendapat bonus \n")