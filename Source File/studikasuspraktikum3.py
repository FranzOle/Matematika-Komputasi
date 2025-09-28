def biconditional_case():
    print("Studi Kasus Bikondisional")

    perangkat_a = False
    peranfkat_b = False

    print(f"Perangkat A (p): {perangkat_a}")
    print(f"Perangkat B (q): {peranfkat_b}")
    print(f"Hasil (p ↔ q): {(perangkat_a and peranfkat_b) or (not perangkat_a and not peranfkat_b)}\n")

def inference_case():
    print("Studi Kasus Inferensi")

    perangkat_a = False
    perangkat_b = True

    implication = not perangkat_a or perangkat_b
    print(f"Perangkat A (p): {perangkat_a}")
    print(f"Perangkat B (q): {perangkat_b}")
    print(f"Hasil Implikasi (p → q): {implication}\n")

    if perangkat_a and implication:
        print(f"Dari p dan p → q, maka q bernilai {perangkat_b} \n")

def argument_case():
    print("Studi Kasus Argumen")
    
    proyek_selesai_tepat_waktu = True
    klien_puas = True
    perusahaan_terima_bonus = True
    
    premise_1 = not proyek_selesai_tepat_waktu or klien_puas
    premise_2 = not klien_puas or perusahaan_terima_bonus
    
    conclusion = not proyek_selesai_tepat_waktu or perusahaan_terima_bonus
    
    print(f"Premis 1 (p -> q): {premise_1}")
    print(f"Premis 2 (q -> r): {premise_2}")
    print(f"Kesimpulan (p -> r): {conclusion} \n")

def axioms_theorems_case():
    print("Studi Kasus Aksioma, Teorema, Lemma, dan Corollary")

    # Aksioma
    aksioma = "Total sudut segitiga adalah 180 derajat"
    print(f"Aksioma: {aksioma}")

    # Teorema
    teorema = "Segitiga siku-siku memiliki sudut 90 derajat"
    print(f"Teorema: {teorema}")

    # Lemma
    lemma = "Sudut di seberang sisi terpanjang dalam segitiga siku-siku adalah 90 derajat"
    print(f"Lemma: {lemma}")

    # Corollary
    corollary = "Jika segitiga memiliki sudut 90 derajat, maka segitiga tersebut adalah segitiga siku-siku"
    
    print(f"Corollary: {corollary} \n")

def cek_status_jaringan(p, q):
    biconditional = (p and q) or (not p and not q)

    if biconditional:
        if p and q:
            hasil = "Perangkat berfungsi dengan baik"
        else:
            hasil = "Perangkat bermasalah dan tidak sinkron"
    else:
        hasil = "Status perangkat tidak sinkron"

    return biconditional, hasil
        

def biconditional_case2():
    print("Bikondisional dalam jaringan komputer")

    #case 1
    p1 = True
    q1 = False

    result1, status1 = cek_status_jaringan(p1, q1)
    print(f"Perangkat A (p): {p1}, Perangkat B (q): {q1}")
    print(f"Hasil (p ↔ q): {result1}, Status: {status1}\n")

    #case 2
    p2 = True
    q2 = True
    result2, status2 = cek_status_jaringan(p2, q2)
    print(f"Perangkat A (p): {p2}, Perangkat B (q): {q2}")
    print(f"Hasil (p ↔ q): {result2}, Status: {status2}\n")

def alarm_keamanan(sensor, alarm):
    implication = not sensor or alarm

    if implication:
        if sensor and alarm:
            return "Sistem berfungsi dengan baik"
        else:
            return "Sistem gagal"
    else:
        return "Sistem gagal"
    
def studi_kasus_alarm():
    print("Sistem Alarm Keamanan")

    sensor1, alarm1 = True, False
    message1 = alarm_keamanan(sensor1, alarm1)
    print(f"Sensor mendeteksi Gerakan:{sensor1}, Alarm berbunyi:{alarm1}, Hasil:{message1}")

    sensor2, alarm2 = True, True
    message2 = alarm_keamanan(sensor2, alarm2)
    print(f"Sensor mendeteksi Gerakan:{sensor2}, Alarm berbunyi:{alarm2}, Hasil:{message2}")

def perusahaan(proyek_selesai, klien_puas, bonus):
    premise1 = not proyek_selesai or klien_puas
    premise2 = not klien_puas or bonus
    conclusion = not proyek_selesai or bonus

    if premise1 and premise2 and conclusion:
        if proyek_selesai and klien_puas and bonus:
            return "Perusahaan menerima Bonus"
        else:
            return "Tidak ada bonus"
    else:
        return "Tidak ada bonus"

def business_case():
    print("Teori Argumen proses Bisnis")
    
    proyek_selesai1, klien_puas1, bonus1 = True, False, False
    message1 = perusahaan(proyek_selesai1, klien_puas1, bonus1)
    print(f"Proyek Selesai tepat waktu: {proyek_selesai1}, Klien puas: {klien_puas1}, Perusahaan menerima bonus: {bonus1}, Kesimpulan: {message1}")
    
    proyek_selesai2, klien_puas2, bonus2 = True, True, True
    message2 = perusahaan(proyek_selesai2, klien_puas2, bonus2)
    print(f"Proyek Selesai tepat waktu: {proyek_selesai2}, Klien puas: {klien_puas2}, Perusahaan menerima bonus: {bonus2}, Kesimpulan: {message2}")

def segitiga(sudut1, sudut2, sudut3):
    if sudut1 + sudut2 + sudut3 != 180:
        return f"Sudut 1:{sudut1}, Sudut 2:{sudut2}, Sudut 3:{sudut3}, Kesimpulan: Bukan segitiga (Jumlah sudut >180)"
    
    if 90 in (sudut1, sudut2, sudut3):
        return f"Sudut 1:{sudut1}, Sudut 2:{sudut2}, Sudut 3:{sudut3}, Kesimpulan: Ini adalah segitiga siku siku"
    else:
        return f"Sudut 1:{sudut1}, Sudut 2:{sudut2}, Sudut 3:{sudut3}, Kesimpulan: Ini bukan segitiga siku-siku."

def axioms_segitiga():
    print("Teori Aksioma dalam Segitiga")
    
    print(segitiga(90, 60, 30))
    print(segitiga(60, 60, 60))
    print(segitiga(100, 100, 100))


if __name__ == "__main__":
    print("Hello, World! \n")

    biconditional_case()
    inference_case()
    argument_case()
    axioms_theorems_case()

    biconditional_case2()
    studi_kasus_alarm()
    print("\n")
    business_case()
    print("\n")
    axioms_segitiga()