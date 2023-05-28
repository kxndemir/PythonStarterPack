import random

def sayi_tahmin_oyunu():
    sayi = random.randint(1, 10)  # Randint aralığını değiştirirseniz seçtiği sayı aralığı değişir.
    tahmin_hakki = 3  # Anlayacağınız üzere kullanıcıya verilen tahmin hakkı değeri.

    print('''[~] Sayı tahmin oyununa hoş geldin!
[~] 1-10 arasında bir sayı tuttum. Hadi tahmin etmeye çalış.''')

    while tahmin_hakki > 0:
        print("[!] Kalan tahmin hakkınız:", tahmin_hakki)  # Tahmin hakkını belirtir.
        tahmin = int(input("Tahmininizi girin: "))  # Kullanıcıdan tahmin alınır.

        if tahmin == sayi:
            print("\n\n[!] Tebrikler! Doğru tahmin ettiniz.")
            break
        elif tahmin < sayi:
            print("\n\n[!] Daha yüksek bir sayı deneyin.")
        else:
            print("\n\n[!] Daha düşük bir sayı deneyin.")

        tahmin_hakki -= 1

    if tahmin_hakki == 0:
        print("Tahmin hakkınız kalmadı. Doğru sayı:", sayi)

sayi_tahmin_oyunu()
