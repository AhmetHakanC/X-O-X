import random

satir1 = ["0", "*", "*", "*", "*", "*", "*", "*", "*", "*"]

oyuncu1 = True
oyuncu2 = False

rakamlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def hep():
    print("--------")
    print(satir1[1], satir1[2], satir1[3])
    print(satir1[4], satir1[5], satir1[6])
    print(satir1[7], satir1[8], satir1[9])
    print("--------")


print("XOX oyununa hoş geldiniz.")
while True:
    print("Oyuncu 1: X, Oyuncu 2: O")
    isim1 = input("Oyuncu 1'in ismi: ")
    isim2 = input("Oyuncu 2'in ismi: ")

    a = input("İlk kim başlasın? '1' veya '2'(Oto= rastgele)(Rastgele için 'r' yazın)")
    hep()
    if (a == "1"):
        oyuncu1 = True
        oyuncu2 = False
    elif (a == "2"):
        oyuncu1 = False
        oyuncu2 = True
    else:
        b = random.randint(1, 2)
        if (b == 1):
            oyuncu1 = True
            oyuncu2 = False
        else:
            oyuncu1 = False
            oyuncu2 = True

    if (oyuncu1 == True):
        print("Oyuncu 1 başlayacak")
    else:
        print("Oyuncu 2 başlayacak.")

    while True:
        if (oyuncu1 == True):
            print("Sıra:", isim1, "'de")
            oyuncu1 = False
            oyuncu2 = True
            while True:
                c = int(input("Hücre no: "))
                if (c not in rakamlar):
                    print("Lütfen geçerli bir sayı giriniz")
                    continue
                if (satir1[c] == "X" or satir1[c] == "O"):
                    print("Bu hücre zaten dolu!")
                    continue
                else:
                    break
            satir1[c] = "X"
            hep()

        else:
            print("Sıra:", isim2, "'de")
            oyuncu1 = True
            oyuncu2 = False
            while True:
                c1 = int(input("Hücre no: "))
                if (c1 not in rakamlar):
                    print("Lütfen geçerli bir sayı giriniz")
                    continue
                if (satir1[c1] == "X" or satir1[c1] == "O"):
                    print("Bu hücre zaten dolu!")
                    continue
                else:
                    break
            satir1[c1] = "O"
            hep()

        if (satir1[1] == "X" and satir1[2] == "X" and satir1[3] == "X" or satir1[1] == "X" and satir1[5] == "X" and
                satir1[9] == "X" or satir1[1] == "X" and satir1[4] == "X"
                and satir1[7] == "X" or satir1[4] == "X" and satir1[5] == "X" and satir1[6] == "X" or satir1[
                    7] == "X" and satir1[8] == "X" and satir1[9] == "X"
                or satir1[3] == "X" and satir1[5] == "X" and satir1[7] == "X" or satir1[2] == "X" and satir1[
                    5] == "X" and satir1[8] == "X" or satir1[3] == "X"
                and satir1[6] == "X" and satir1[9] == "X"):
            print(isim1, " Kazandı.")
            break
        elif (satir1[1] == "O" and satir1[2] == "O" and satir1[3] == "O" or satir1[1] == "O" and satir1[5] == "O" and
              satir1[9] == "O" or satir1[1] == "O" and satir1[4] == "O"
              and satir1[7] == "O" or satir1[4] == "O" and satir1[5] == "O" and satir1[6] == "O" or satir1[7] == "O" and
              satir1[8] == "O" and satir1[9] == "O"
              or satir1[3] == "O" and satir1[5] == "O" and satir1[7] == "O" or satir1[2] == "O" and satir1[5] == "O" and
              satir1[8] == "O" or satir1[3] == "O"
              and satir1[6] == "O" and satir1[9] == "O"):
            print(isim2, " Kazandı.")
            break

    t = input("Tekrar oynamak istiyorsanız 'enter' tuşuna basın.")
    if (t == ""):
        satir1 = ["0", "*", "*", "*", "*", "*", "*", "*", "*", "*"]
        continue
    else:
        print("Oyun Kapatılıyor")
        break
