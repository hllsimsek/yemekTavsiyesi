def yemek_tavsiyesi(saat):
    try:
        # Sadece saati alıyoruz, dakika kısmını atlıyoruz
        saat = int(saat.split(":")[0])

        if 7 <= saat < 12:
            return "Kahvalti Yapiniz"
        elif 12 <= saat < 15:
            return "Ogle Yemegi Yiyiniz"
        elif 16 <= saat < 20:
            return "Aksam Yemegi Yiyiniz"
        elif 21 <= saat <= 23 or 0 <= saat < 7:
            return "Sadece Meyve ya da Kuruyemis Yemelisiniz"
        else:
            return "Gecersiz saat araligi girdiniz."
    except ValueError:
        return "Lutfen saati dogru formatta giriniz (ornek: 07:30)."