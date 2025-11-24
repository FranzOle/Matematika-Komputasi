import numpy as np

def operasi_matriks(MatriksA, MatriksB):
    MatriksA = np.array(MatriksA)
    MatriksB = np.array(MatriksB)

    hasil_tambah = MatriksA + MatriksB
    
    hasil_kurang = 2 * MatriksA - MatriksB
    
    hasil_kali_AB = MatriksA.dot(MatriksB)
    hasil_kali_BA = MatriksB.dot(MatriksA)
    
    is_komutatif = np.array_equal(hasil_kali_AB, hasil_kali_BA)
    
    print("Matriks A:\n", MatriksA)
    print("Matriks B:\n", MatriksB)
    print("\nHasil A + B:\n", hasil_tambah)
    print("\nHasil 2A - B:\n", hasil_kurang)
    print("\nHasil A x B:\n", hasil_kali_AB)
    print("\nHasil B x A:\n", hasil_kali_BA)
    print("\nApakah A x B = B x A ?", is_komutatif)
    
    return hasil_tambah, hasil_kurang, hasil_kali_AB, hasil_kali_BA, is_komutatif

MatriksA = [[1, 2],
            [3, 4]]

MatriksB = [[2, 0],
            [1, 3]]

operasi_matriks(MatriksA, MatriksB)