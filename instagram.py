from selenium import webdriver
import time

tadi = []
sadi = []


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
        time.sleep(1)
        lenofpage = driver.execute_script(jscommand)
        if Lastcount == lenofpage:
            match=True

driver = webdriver.Chrome(r"C:\Users\murat\Desktop\AA\PYTHON\Selenium\chromedriver")
url = "https://www.instagram.com/"

driver.get(url)
time.sleep(2)
kAdi = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
sifre = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
time.sleep(1)
kullanıcı_adi = "muratsahh_"
kAdi.send_keys(kullanıcı_adi)
sifre.send_keys("Mrt61mhmt")
girisYap = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()
time.sleep(3)
driver.get("https://www.instagram.com/"+ kullanıcı_adi +"/")
time.sleep(4)
takipci = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
time.sleep(3)
scroll()

elements = driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

for i in elements:
    tadi.append(i.text)

driver.back()
time.sleep(1)
takip = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
time.sleep(2)
scroll()
elements = driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
for j in elements:
    sadi.append(j.text)
    
for ta in tadi:
    if(not(ta in sadi)):
        print("-------------")
        print(ta)