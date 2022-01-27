from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyfiglet
from colorama import Fore, Back, Style, init
init(autoreset=True)
BlackList = []
Rapor = []
def configOku():
    global comment, email, name, website, son_kaldigi_site
    try:
        with open("blacklist.txt","r") as f:
            for i in f:
                BlackList.append(i)
            f.close()
        with open("rapor.txt","r") as f:
            for i in f:
                Rapor.append(i)
            f.close()
        with open("Config/site_list.txt","r") as f:
            f.close()
        with open("Ayar/comment.txt","r") as f:
            comment = f.readline()
            f.close()
        with open("Ayar/email.txt","r") as f:
            email = f.readline()
            f.close()
        with open("Ayar/name.txt","r") as f:
            name = f.readline()
            f.close()
        with open("Config/son_kaldigi_site.txt","r") as f:
            son_kaldigi_site = f.readline()
            f.close()
        with open("Ayar/website.txt","r") as f:
            website = f.readline()
            f.close()
        print("")
        print(Fore.GREEN + "Configler Başarıyla Okundu.")
    except:
        print("")
        print(Fore.RED + "Configler Okunurken Hata Oluştu Lütfen Takım Dosyaların Doğruluğundan Emin Olduktan Sonra Tekrar Deneyin.")

def start(): #Listenin Başından başlar
    yorum_sayac = 1
    with open("Config//site_list.txt","r+") as f:
        for i in f:
            if yorum_sayac > yorum_sayisi:
                print(Fore.MAGENTA + "Tüm yorumlar atıldı.")
                input("Programı kapatmak için enter basınız.")
                exit()
            else:
                pass
            if i in BlackList:
                print(Fore.MAGENTA + "Blacklist Algılandı Site Atlanıyor...")
                continue
              
            
            tarayici = webdriver.Chrome()
            tarayici.set_page_load_timeout(60)
            try:
                try:
                    with open("Config//son_kaldigi_site.txt","w") as f:
                        f.write(i)
                        f.close()
                    tarayici.get(i)
                    try:
                        ELEMcomment = tarayici.find_element(By.NAME, "comment")
                    except:
                        ELEMcomment = tarayici.find_element(By.NAME, "comment_txt")
                    try:
                       ELEMauthor = tarayici.find_element(By.NAME, "author")
                    except:
                        ELEMauthor = tarayici.find_element(By.ID, "author")
                    try:
                        ELEMemail = tarayici.find_element(By.NAME, "email")
                    except:
                        ELEMemail = tarayici.find_element(By.ID, "email")
                    try:
                        ELEMwebsite = tarayici.find_element(By.NAME, "url")
                    except:
                        pass
                    try:
                        ELEMsubmit = tarayici.find_element(By.NAME, "submit")
                    except:
                        ELEMsubmit = tarayici.find_element(By.ID, "submit")
                    ELEMcomment.send_keys(comment)
                    ELEMauthor.send_keys(name)
                    ELEMemail.send_keys(email)
                    try:
                        ELEMwebsite.send_keys(website)
                    except:
                        pass
                    time.sleep(1)
                    tarayici.execute_script("arguments[0].click();", ELEMsubmit)
                    print(Fore.GREEN + "[+] {}.Yorum Başarıyla Yapıldı.".format(yorum_sayac))
                    with open("rapor.txt","a") as f:
                        if i in Rapor:
                            pass
                        else:
                            f.write(i)
                        f.close()
                    yorum_sayac += 1
                    time.sleep(2)
                    tarayici.quit()
                except:
                    print(Fore.MAGENTA + "Bilinmeyen Bir Hata Oluştu!")
                    print(Fore.RED + "Devam Ediliyor...")
                    with open("blacklist.txt","a") as f:
                            if i in BlackList:
                                pass
                            else:
                                f.write(i)
                            f.close()
                    time.sleep(2)
                    tarayici.quit()
            except TimeoutException as ex:
                print(Fore.MAGENTA+"Site Zaman Aşımına Uğradı")
                print(Fore.RED + "Devam Ediliyor...")
                time.sleep(2)
                tarayici.quit()
            

def start2(): #Kaldığı yerden başlar
    yorum_sayac = 1
    devamEt = False
    with open("Config//site_list.txt","r+") as f:
        for i in f:
            
            if i == son_kaldigi_site:
                devamEt = True
            else:
                pass
            if devamEt is False:
                pass
            else:
                if yorum_sayac > yorum_sayisi:
                    print(Fore.MAGENTA + "Tüm yorumlar atıldı.")
                    input("Programı Kapatmak için ENTER Basınız.")
                    exit()
                else:
                    pass
                if i in BlackList:
                    print(Fore.MAGENTA + "Blacklist Algılandı Site Atlanıyor...")
                    continue
                tarayici = webdriver.Chrome()
                tarayici.set_page_load_timeout(60)
                try:
                    try:
                        with open("Config//son_kaldigi_site.txt","w") as f:
                            f.write(i)
                            f.close()
                        tarayici.get(i)
                        try:
                            ELEMcomment = tarayici.find_element(By.NAME, "comment")
                        except:
                            ELEMcomment = tarayici.find_element(By.NAME, "comment_txt")
                        try:
                           ELEMauthor = tarayici.find_element(By.NAME, "author")
                        except:
                            ELEMauthor = tarayici.find_element(By.ID, "author")
                        try:
                            ELEMemail = tarayici.find_element(By.NAME, "email")
                        except:
                            ELEMemail = tarayici.find_element(By.ID, "email")
                        try:
                            ELEMwebsite = tarayici.find_element(By.NAME, "url")
                        except:
                            pass
                        try:
                            ELEMsubmit = tarayici.find_element(By.NAME, "submit")
                        except:
                            ELEMsubmit = tarayici.find_element(By.ID, "submit")
                        ELEMcomment.send_keys(comment)
                        ELEMauthor.send_keys(name)
                        ELEMemail.send_keys(email)
                        try:
                            ELEMwebsite.send_keys(website)
                        except:
                            pass
                        time.sleep(1)
                        tarayici.execute_script("arguments[0].click();", ELEMsubmit)
                        print(Fore.GREEN + "[+] {}.Yorum Başarıyla Yapıldı!".format(yorum_sayac))
                        with open("blacklist.txt","a") as f:
                            if i in BlackList:
                                pass
                            else:
                                f.write(i)
                            f.close()
                        yorum_sayac += 1
                        time.sleep(3)
                        tarayici.quit()
                    except:
                            print(Fore.MAGENTA + "Bilinmeyen Bir Hata Oluştu!")
                            print(Fore.RED + "Devam Ediliyor...")
                            with open("rapor.txt","a") as f:
                                if i in Rapor:
                                    pass
                                else:
                                    f.write(i)
                                f.close()
                            time.sleep(2)
                            tarayici.quit()
                except TimeoutException as ex:
                    print(Fore.MAGENTA+"Site Zaman Aşımına Uğradı!")
                    print(Fore.RED + "Devam Ediliyor...")
                    time.sleep(2)
                    tarayici.quit()
                
        
text = pyfiglet.figlet_format('Auto Comment',)
print(text)
print("")
print(Back.RED + "R10= Seonuz Youtube= https://www.youtube.com/c/BatuhanAktaş75.")
print("")
print(Fore.MAGENTA + "[BILGI]:", "Iletisim icin Bionluk Adresinden UlaÅŸabilirsiniz;")
print("")
print(Fore.GREEN + " Github= batuhapro")
print("")


print(Fore.MAGENTA + "Configler Okunuyor...")
configOku()
print("")
print(Back.MAGENTA + "[?] Listenin Başından Başla -- > 1/n[?] Son Kaldığın Siteden Devam Et --> 2")
print("")
secim = input("Seciminiz >> ")
if secim == "1":
    yorum_sayisi = int(input("Kaç Tane Yorum Yapmak İstiyorsunuz: "))
    input("İşleme başlamak için ENTER Basınız.")
    start()
elif secim == "2":
    yorum_sayisi = int(input("KaÃ§ Tane Yorum Yapmak Ä°stiyorsunuz: "))
    input("İşleme başlamak için ENTER Basınız.")
    start2()
else:
    print(Fore.RED + "Lütfen geçerli biri işlem yapınız.")
    input("Kapatmak için ENTER Basınız.")
