from selenium import webdriver
import time
import random

from urllib3.packages.six import ensure_text

takipci = []
takip = []

baslangıc  = time.time()

def kisiListesi():
    scroll()
    elements = driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
    sonuc = []
    for i in elements:
        i = "/" + i.text + "/"
        sonuc.append(i)
    return sonuc

def scroll():
    jscommand = """
    followers = document.querySelector(".isgrP");
    followers.scrollTo(0,followers.scrollHeight);
    var lenOfPage = followers.scrollHeight;
    return lenOfPage 
    """
    lenofpage = driver.execute_script(jscommand)
    match = False
    while (match == False):
        Lastcount = lenofpage
        time.sleep(0.5)
        lenofpage = driver.execute_script(jscommand)
        if Lastcount == lenofpage:
            match=True

driver = webdriver.Chrome() # r"C:\Users\****\****\***chromedriver"
url = "https://www.instagram.com/"

driver.get(url)
time.sleep(2)
kAdi = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
sifre = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
time.sleep(1)
kullanıcıAdı = "----" #Kullanıcı Adı
kAdi.send_keys(kullanıcıAdı)
sifre.send_keys("----") #Sifre
girisYap = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()
time.sleep(3)
driver.get("https://www.instagram.com/"+ kullanıcıAdı + "/")
time.sleep(3)

takipciButonu = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
time.sleep(1)
takipci = kisiListesi()

driver.back()

takipButonu = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
time.sleep(1)
takip = kisiListesi()

takipEtmeyenler = []
for takipler in takip:
    if(not(takipler in takipci)):
        takipEtmeyenler.append(takipler)

sayac = 0 

for i in takipEtmeyenler:
    try:
        if(sayac < 80):
            driver.get("https://www.instagram.com{}".format(i))
            driver.find_element_by_css_selector("button[class^='_5f5mN    -fzfL     _6VtSN     yZn4P   ']").click()
            time.sleep(0.5)
            driver.find_element_by_xpath('//button[text() = "Takibi Bırak"]').click()
            time.sleep(random.randrange(20,30))
            sayac +=1
    except:
        print("Hata Oluştu Kişi:" + i)
        break 



bitis = time.time()
print(sayac)
print(bitis - baslangıc)

driver.close()

