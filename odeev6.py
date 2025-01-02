
class BankaHesabi:
   def __init__(self, hesapSahibi):
      self.hesapSahibi = hesapSahibi
      self.bakiye = 0.0
   def paraYatir(self, amount):
      self.bakiye += amount
      return self.bakiye
   def paraCek(self, amount):
      if amount < 0:
         print("Geçersiz miktar.")
      elif amount > self.bakiye:
         print("Yetersiz bakiye.")
      else:
         self.bakiye -= amount
         return self.bakiye

name = str(input("Adınız: "))
hesap = BankaHesabi(name)
print(hesap.hesapSahibi)
print(hesap.bakiye)
miktar = float(input("Yatırmak istediğiniz miktar (İptal için 0 giriniz): "))
print(hesap.paraYatir(miktar))
cek = float(input("Çekmek istediğiniz miktar (İptal için 0 giriniz): "))
print(hesap.paraCek(cek))
        