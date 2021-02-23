from math import sqrt
print("Triangle Detector by Gading")
while True:
    try:
        a = int(input("Masukkan panjang sisi a : "))
        b = int(input("Masukkan panjang sisi b : "))
        c = int(input("Masukkan panjang sisi c : "))
    except:
        print("Nilai tidak boleh ≤ 0 atau desimal.")
    else:
        siku = sqrt(a**2 + b**2) 
        ab = a + b
        bc = b + c
        ca = c + a
        x = ab > c
        y = bc > a
        z = ca > b
        abc = a and b < c
        bca = b and c < a
        cab = c and a < b
        if c == siku:
            print("Segitiga tersebut adalah siku-siku.")
        elif a == b == c:
            print("Segitiga tersebut adalah sama sisi.")
        elif a == b and ab > c:
            print("Segitiga tersebut adalah sama kaki.")
        elif b == c and bc > a:
            print("Segitiga tersebut adalah sama kaki.")
        elif c == a and ca > b:
            print("Segitiga tersebut adalah sama kaki.")
        elif a != b and a and b < c and ab > c:
            print("Segitiga tersebut adalah segitiga sembarang.")
        elif b != c and b and c < a and bc > a:
            print("Segitiga tersebut adalah segitiga sembarang.")
        elif c != a and c and a < b and ca > b:
            print("Segitiga tersebut adalah segitiga sembarang.")
        else:
            print("Tidak bisa membentuk segitiga karena melebihi 180 derajat.")
        break