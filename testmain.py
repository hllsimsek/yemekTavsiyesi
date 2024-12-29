from main import yemek_tavsiyesi
def test_yemek_tavsiyesi():
    # Kullanıcıdan saat girdisi al
    saat = input("Lütfen saati HH:00 formatinda giriniz: ")  # Dakika kısmı yok, sadece saat girilecek

    # Yemek tavsiyesi fonksiyonunu çağır
    mesaj = yemek_tavsiyesi(saat)

    # Mesajı dosyaya yaz
    with open("mesaj.txt", "w") as dosya:
        dosya.write(mesaj)

    print(f"Sonuc mesaj.txt dosyasına yazildi: {mesaj}")


# Test fonksiyonunu çalıştır
if __name__ == "__main__":
    test_yemek_tavsiyesi()
