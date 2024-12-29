from datetime import datetime


def yemek_tavsiyesi(saat):
    try:
        # Saat formatını kontrol et
        dt = datetime.strptime(saat, "%H:%M")
    except ValueError:
        return "Lutfen saati dogru formatta giriniz (ornek: 07:30)."

    # Saat dilimlerine göre yemek tavsiyesi
    if not (0 <= dt.hour < 24 and 0 <= dt.minute < 60):
        return "Gecersiz saat araligi girdiniz."

    if "06:00" <= saat < "10:00":
        return "Kahvalti Yapiniz"
    elif "12:00" <= saat < "15:00":
        return "Ogle Yemegi Yiyiniz"
    elif "17:00" <= saat < "21:00":
        return "Aksam Yemegi Yiyiniz"
    elif "21:00" <= saat < "23:59":
        return "Sadece Meyve ya da Kuruyemis Yemelisiniz"
    else:
        return "Gecersiz saat araligi girdiniz."
