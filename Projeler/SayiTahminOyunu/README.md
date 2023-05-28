# Python Sayı Tahmin Oyunu

Bu proje, kullanıcının belirli bir aralıkta rastgele seçilen bir sayıyı tahmin etmeye çalıştığı bir Python oyununu içerir. Oyun, kullanıcının tahmin ettiği sayıya göre geri bildirim verir ve sonunda doğru sayıyı bulup bulamadığını bildirir.

## Nasıl Kullanılır

1. Python diline ait bir IDE veya metin düzenleyici açın.
2. Yeni bir Python dosyası oluşturun ve adını "sayi_tahmin_oyunu.py" gibi uygun bir isim verin.
3. İlgili kodları sayi_tahmin_oyunu.py dosyasına yapıştırın.
4. Dosyayı kaydedin ve çalıştırın.

## Kullanım

1. Program çalıştırıldığında, 1 ile 10 arasında rastgele bir sayı seçilir ve kullanıcıya bu aralıkta bir sayı tahmin etmesi söylenir.
2. Kullanıcı, tahminini girmek için bir giriş kutusu alır.
3. Tahmin hakkı sayısı ve doğru cevaba göre geri bildirimler alınır.
4. Eğer kullanıcı doğru sayıyı tahmin ederse, tebrik mesajı görüntülenir. Aksi takdirde, tahmin hakkı tükenene kadar kullanıcıya daha fazla tahmin şansı verilir ve doğru sayı açıklanır.

## Örnek Çıktı

```python
[~] Sayı tahmin oyununa hoş geldin!
[~] 1-10 arasında bir sayı tuttum. Hadi tahmin etmeye çalış.
[!] Kalan tahmin hakkınız: 3
Tahmininizi girin: 5

[!] Daha yüksek bir sayı deneyin.
[!] Kalan tahmin hakkınız: 2
Tahmininizi girin: 8

[!] Daha düşük bir sayı deneyin.
[!] Kalan tahmin hakkınız: 1
Tahmininizi girin: 7

[!] Daha düşük bir sayı deneyin.
Tahmin hakkınız kalmadı. Doğru sayı: 6
```

## Gereksinimler
Bu sayı tahmin oyunu, Python 3 sürümüyle uyumludur. Python 3 veya daha üst bir sürüm yüklü olmalıdır. (Python 3.6 vb.)

Bu kod, rastgele sayı seçmek için `random` kütüphanesini kullanır. Kullanıcının girişlerini almak için input() fonksiyonu kullanılır.

Kod, kullanıcının tahmin hakkını takip eder, kullanıcının tahminine göre geri bildirim verir ve doğru sayıyı belirleyene kadar döngüyü tekrarlar.
