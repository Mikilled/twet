from selenium_stealth import stealth
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pickle
import time
import datetime

def main_opensea():
        global links
        driver.get('https://opensea.io/activity?search[chains][0]=ETHEREUM&search[eventTypes][0]=AUCTION_SUCCESSFUL')
        time.sleep(4)
        all_block = driver.find_elements(By.CSS_SELECTOR, '.hmswhC')
        links = []
        for block in all_block:
                a = block.get_attribute('href')
                links.append(a)



def search_twit():
        global links
        global twiters
        for link in links:
                driver.get(link)
                a = driver.find_elements(By.XPATH, '//*[@id="main"]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[1]/a')
                if len(a) != 0:
                        for i in a:
                                b = i.get_attribute('href')
                                if 'twitter' in b:
                                        twiters.append(b)



def twiter():
        global globtwiters
        globtwiters = list(set(globtwiters))
        global twiters
        global freetwit
        for twit in globtwiters:
                driver.get(twit)
                time.sleep(2)
                tw = driver.find_elements(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/span')
                if len(tw) != 0:
                        print(twit)
                        freetwit.append(twit)
                else:
                        continue


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("start-maximized")
chrome_options = webdriver.ChromeOptions()
prefs =  {
        'profile.managed_default_content_settings.images': 2,
        'profile.managed_default_content_settings.mixed_script': 2,
        'profile.managed_default_content_settings.media_stream': 2,
        'profile.managed_default_content_settings.stylesheets':2
    }
chrome_options.add_experimental_option("prefs", prefs)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=chrome_options)



stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

print("PARSER Opensea v1.3.3")


try:
    f = open('config.txt', 'r',encoding="utf-8")
    cooks = str(f.readline())
except FileNotFoundError:
    f = open('config.txt', 'w', encoding="utf-8")
    print('Конфиг не обнаружен - нужно создать')
    cooks = input('введите путь до куки-')
    f.write(cooks)
f.close()

n = int(input('введите кол-во прогонов-'))

#"C:\wit\cookies.pkl"
c = 0
globtwiters = []
freetwit = []
while c != n:
        links = []
        twiters = []
        main_opensea()
        search_twit()
        globtwiters = globtwiters + twiters
        c+=1


driver.get("https://twitter.com")
time.sleep(1)
for cookie in pickle.load(open(cooks.rstrip(), "rb")):
    driver.add_cookie(cookie)
time.sleep(2)
twiter()

print(freetwit)
j = ''
now = str((datetime.datetime.today()).strftime("%Y-%m-%d-%H-%M-%S.txt"))
f = open(now, 'w',encoding="utf-8")
for i in range(len(freetwit)):
        j = freetwit[i]
        f.write(j+'\n')
f.close()





