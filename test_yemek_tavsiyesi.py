import unittest
from main import yemek_tavsiyesi

class TestYemekTavsiyesi(unittest.TestCase):
    def test_kahvalti(self):
        self.assertEqual(yemek_tavsiyesi("08:00"), "Kahvaltı Yapınız")

    def test_ogle_yemegi(self):
        self.assertEqual(yemek_tavsiyesi("13:00"), "Öğle Yemeği Yiyiniz")

    def test_aksam_yemegi(self):
        self.assertEqual(yemek_tavsiyesi("18:00"), "Akşam Yemeği Yiyiniz")

    def test_gece_atistirmasi(self):
        self.assertEqual(yemek_tavsiyesi("22:00"), "Sadece Meyve ya da Kuruyemiş Yemelisiniz")

    def test_gecersiz_saat(self):
        self.assertEqual(yemek_tavsiyesi("25:00"), "Geçersiz saat aralığı girdiniz.")

    def test_hatalı_format(self):
        self.assertEqual(yemek_tavsiyesi("saat"), "Lütfen saati doğru formatta giriniz (örnek: 07:30).")
