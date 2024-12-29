import unittest
from main import yemek_tavsiyesi

class TestYemekTavsiyesi(unittest.TestCase):
    def test_kahvalti(self):
        self.assertEqual(yemek_tavsiyesi("08:00"), "Kahvalti Yapiniz")

    def test_ogle_yemegi(self):
        self.assertEqual(yemek_tavsiyesi("13:00"), "Ögle Yemegi Yiyiniz")

    def test_aksam_yemegi(self):
        self.assertEqual(yemek_tavsiyesi("18:00"), "Aksam Yemegi Yiyiniz")

    def test_gece_atistirmasi(self):
        self.assertEqual(yemek_tavsiyesi("22:00"), "Sadece Meyve ya da Kuruyemis Yemelisiniz")

    def test_gecersiz_saat(self):
        self.assertEqual(yemek_tavsiyesi("25:00"), "Gecersiz saat araligi girdiniz.")

    def test_hatalı_format(self):
        self.assertEqual(yemek_tavsiyesi("saat"), "Lutfen saati dogru formatta giriniz (ornek: 07:30).")
