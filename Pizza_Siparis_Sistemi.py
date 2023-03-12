import csv
from datetime import datetime
from csv import writer
     

                                                                #Pizza classı
class pizza:
  def __init__(self, description, cost):
    self.description = description
    self.cost = cost
                                                                #pizza sınıfı
klasik = pizza("Klasik pizza", 30)
margarita = pizza("Margarita pizza", 40)
turk_pizza = pizza("Türk pizza", 50)
sade = pizza("Sade pizza",  20)
                                                                #Decorator
class decorator(pizza):
  def toplam_ucret(self,pizza):
    ucret = pizza.cost + self.cost
    return ucret
  def pizza_aciklama(self,pizza):
    desc = pizza.description + ' ' + self.description + ' ile hazırlanacaktır.'
    return desc
     
                                                                #Ek malzemelerin decorator#
zeytin = decorator("Zeytin", 2)
mantar = decorator("Mantar",3)
keci_peyniri = decorator("Keçi Peyniri", 4)
et = decorator("Et", 5)
sogan = decorator("Soğan", 2)
mısır = decorator("Mısır", 3)
     

#Menu.txt dosyası oluşturularak, menu değişkeni oluşturulur.
Secim = ['* Lütfen Bir Pizza Tabanı Seçiniz:', '1: Klasik', '2: Margarita', '3: TürkPizza', '4: Sade Pizza', '* Lütfen Sos Seçin:', '11: Zeytin', '12: Mantarlar', '13: Keçi Peyniri', '14: Et', '15: Soğan', '16: Mısır', '* Teşekkür ederiz!' ]
with open("Menu.txt", "a") as file:
  for sec in Secim:
   file.write(sec)
   file.write("\n")
file = open("Menu.txt", "r")
menu = file.read()
file.close()
     

#Menü sözlüğü oluşturulur. Keyleri menüdeki numaralardan, valueları ise alt sınıflardan oluşur.
list_of_menu = {"1":klasik,"2":margarita,"3":turk_pizza,"4":sade,"11":zeytin,"12":mantar,"13":keci_peyniri,"14":et,"15":sogan,"16":mısır}
     

baslik = ['AD', 'TC', 'Kart No', 'Şifre', 'Sipariş Açıklaması', 'Sipariş Zamanı']
with open('Orders_Database.csv', 'a') as database:
    writer_object = writer(database)
    writer_object.writerow(baslik)
    database.close()
     

#Veri tabanına siparişlerin yazılması için oluşturulan fonksiyon.
def kayıt(siparis):
  with open('Orders_Database.csv', 'a') as database:
    writer_object = writer(database)
    writer_object.writerow(siparis)
    database.close()
     

#Pizza seçimi için hazırlanan fonksiyon
def pizza_secimi():
  pizza_numarasi = input("Almak istediğiniz pizza ile ilgili numarayı giriniz: ")
  while True:
   try:
    if int(pizza_numarasi) in range(0,5) :
     secilen_pizza = list_of_menu[pizza_numarasi]
     break
    pizza_numarasi = input("Lütfen menüde olan bir değer giriniz. Almak istediğiniz pizza ile ilgili numarayı giriniz: ")
   except ValueError:
    pizza_numarasi = input("Lütfen menüde olan bir değer giriniz. Almak istediğiniz pizza ile ilgili numarayı giriniz: ")
  return secilen_pizza

#Sipariş işlemlerinin gerçekleşeceği main fonksiyonu
def main():
  print(menu)
  #Siparişin detaylarını liste kullanarak database üzerine yazacağız. Main fonksiyon her çağrıldığında sıfırdan boş bir liste oluşturulyor.
  siparis = []
  #Sipariş bilgileri alınır.
  secilen_pizza = pizza_secimi()
  secilen_malzeme = ek_malzeme_secimi()
  tutar = secilen_malzeme.toplam_ucret(secilen_pizza)
  aciklama = secilen_malzeme.pizza_aciklama(secilen_pizza) + " Toplam tutar: " + str(tutar) +"TL"
  print(aciklama)
  #Ödeme işlemi odeme fonksiyonu çağrılarak gerçekleştiriliyor.
  global kullanici_adi, kimlik_no, kredi_karti_no, sifre, siparis_zamani
  kullanici_adi, kimlik_no, kredi_karti_no, sifre, siparis_zamani = odeme()
  #Sipariş bilgileri order listesine eleman olarak eklenir.
  siparis.append(kullanici_adi) , siparis.append(kimlik_no) , siparis.append(kredi_karti_no),siparis.append(sifre), siparis.append(aciklama),
  siparis.append(siparis_zamani)
  
  #Sipariş bilgileri veritabanına yazılır.
  kayıt(siparis)
  print("Siparişiniz başarı ile alınmıştır.")    

#Ek malzeme seçimi için hazırlanan fonksiyon
def ek_malzeme_secimi():
  malzeme_numarasi = input("Eklemek istediğiniz malzeme ile ilgili numarayı giriniz: ")
  while True:
    try:
     if int(malzeme_numarasi) in range(10,17):
      secilen_malzeme = list_of_menu[malzeme_numarasi]
      break
     malzeme_numarasi = input("Lütfen menüde olan bir değer giriniz. Eklemek istediğiniz malzeme ile ilgili numarayı giriniz: ")
    except ValueError:
       malzeme_numarasi = input("Lütfen menüde olan bir değer giriniz. Eklemek istediğiniz malzeme ile ilgili numarayı giriniz: ")
  return secilen_malzeme
     

#Ödeme fonksiyonu
def odeme():
  kullanici_adi = input("Lütfen adınızı soyadınızı giriniz: ")
  kimlik_no = input("Lütfen TC kimlik numaranızı giriniz: ")
  kredi_karti_no = input("Lütfen kredi karti numaranızı giriniz: ")
  sifre = input("Lütfen karta ait şifreyi giriniz: ")
  siparis_zamani = (datetime.now())
  return kullanici_adi, kimlik_no, kredi_karti_no, sifre, siparis_zamani
     


     

main()
     