from selenium_stealth import stealth
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pickle
import time
import datetime
import threading
from threading import Thread
from queue import Queue

def add_queue(n):
        global urls
        urls_file = open('urls.txt', 'r', encoding="utf-8")
        for i in range(n):
            urls.put(str(urls_file.readline().rstrip()))
        text = urls_file.read()
        text = "\n".join(text.split("\n")[(n-1):])
        urls_file.close()
        urls_file = open('urls.txt', 'w', encoding="utf-8")
        urls_file.truncate(0)
        urls_file.write(text)
        urls_file.close()

def write_urls(n):
        global urls








def bank(str2,given_url):
    global all_twit
    global zin
    page = 0
    eexit = 0
    while (True):
        url = given_url + 'follower?order=-usd_value' + '&page=' + str(page)
        globals()[str2].get(url)
        wait = WebDriverWait(globals()[str2], 500)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "db-linkTable-row")))
        # time.sleep(6)
        all_block = globals()[str2].find_elements(By.CLASS_NAME, 'db-linkTable-row')
        links = []
        for block in all_block:
            a = block.get_attribute('href')
            links.append(a)

        for link in links:
            globals()[str2].get(link)
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "db-table-row")))
            elements = globals()[str2].find_elements(By.CLASS_NAME, 'HeaderInfo_totalAsset__2noIk')
            for e in elements:
                time.sleep(1.5)
                e = int((e.text[1:]).replace(",", ""))
                # print(e)
                if e > 500:
                    followers = globals()[str2].find_elements(By.CLASS_NAME, 'HeaderInfo_socialNum__3LOsi')
                    if (int((followers[1].text).replace(",", ""))) > 300 and (zin == 1):
                        with open('urls.txt', 'a') as f:
                            f.write('\n'+link+'/')

                    a = globals()[str2].find_elements(By.CLASS_NAME, 'UserTag_snsLink__sevIe')
                    if len(a) != 0:
                        for i in a:
                            b = i.get_attribute('href')
                            if 'twitter' in b:
                                if not (b in all_twit):
                                    all_twit.append(b)
                                    queue1.put(b)
                else:
                    eexit += 1
                    if eexit >=3:
                        return
        page = page + 100


def twiter():
        global now
        f = open(now, 'a', encoding="utf-8")
        twit_file = open('all_twiters.txt', 'a', encoding="utf-8")
        globtwiters = []
        while queue1.empty() != True:
                globtwiters.append(queue1.get())
        for twit in globtwiters:
                driver1.get(twit)
                time.sleep(1)
                driver1.get(twit)
                time.sleep(4)
                tw = driver1.find_elements(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/span')
                if len(tw) != 0:
                        print(twit)
                        f.write(twit + '\n')
                        twit_file.write(twit + '\n')
                else:
                        continue
        f.close()
        twit_file.close()




def check_twit():
        global  now
        global driver1
        print("запуск потока -чекера твитера")
        options1 = webdriver.ChromeOptions()
        options1.add_argument('--headless')
        options1.add_argument("start-maximized")
        chrome_options1 = webdriver.ChromeOptions()
        prefs =  {
                'profile.managed_default_content_settings.images': 2,
                'profile.managed_default_content_settings.mixed_script': 2,
                'profile.managed_default_content_settings.media_stream': 2,
                'profile.managed_default_content_settings.stylesheets':2
            }
        chrome_options1.add_experimental_option("prefs", prefs)
        options1.add_experimental_option("excludeSwitches", ["enable-automation"])
        options1.add_experimental_option('useAutomationExtension', False)

        driver1 = webdriver.Chrome(options=chrome_options1)



        stealth(driver1,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        driver1.get("https://twitter.com")
        time.sleep(2)
        for cookie in pickle.load(open(cooks.rstrip(), "rb")):
                driver1.add_cookie(cookie)
        time.sleep(6)
        print("поток чекера твитера запущен")
        while True:
                if (threading.active_count() != 2):
                        while (queue1.qsize() == 0):
                                pass
                        twiter()
                else:
                        driver1.quit()
                        break


def pars(i):
        global k
        global all_twit
        j = i+2
        str2 = "driver" + str(j)

        print("запуск потока -",i+1)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("start-maximized")
        chrome_options = webdriver.ChromeOptions()
        prefs = {
                'profile.managed_default_content_settings.images': 2,
                'profile.managed_default_content_settings.mixed_script': 2,
                'profile.managed_default_content_settings.media_stream': 2,
                'profile.managed_default_content_settings.stylesheets': 2
        }
        chrome_options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        globals()[str2] = webdriver.Chrome(options=chrome_options)

        stealth(globals()[str2],
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        print("поток парсера запущен-",i+1)
        c = 0
        all_twit = []
        while c != k:
                url = urls.get()
                bank(str2,url)
                c += 1

        globals()[str2].quit()





print("@Miki@ \nPARSER debank v1.0.0")
now = str((datetime.datetime.today()).strftime("%Y-%m-%d-%H-%M-%S.txt"))
n = int(input('введите кол-во потоков'))
k = int(input('кол-во прогонов'))
# k = 1
# n = 1
urls = Queue()
queue1 = Queue()
eror = 0
while eror != 3:
        try:
                try:
                        f = open('config.txt', 'r',encoding="utf-8")
                        cooks = str(f.readline().rstrip())
                        zin = int(f.readline().rstrip())
                except FileNotFoundError:
                        f = open('config.txt', 'w', encoding="utf-8")
                        print('Конфиг не обнаружен - нужно создать')
                        cooks = input('введите путь до куки-')
                        f.write(cooks+'\n')
                        zin = input('нужно ли записывать url(0 или 1) - ')
                        f.write(zin+'\n')
                f.close()
                if (zin == 1):
                    print('ВНИМАНИЕ ВКЛЮЧЕНА ЗАПИСЬ URL')
                    time.sleep(1)
                try:
                        add_queue(n*k)
                except FileNotFoundError:
                        print('Загадка от Жака Фреско - парсить?, что?\n на размышление дается 3 секунды')
                        time.sleep(3)
                        print("может создашь файл с сылками urls.txt")
                        input()


                all_twit = []
                twit_file = open('all_twiters.txt', 'a+', encoding="utf-8")
                twit_file.seek(0)
                all_twit = twit_file.read()
                aLL_twit = all_twit.split("\n")
                twit_file.close()

                time.sleep(1)
                th1 = Thread(target=check_twit).start()

                for i in range(n):
                    str1 = "th" + str(i)
                    globals()[str1] = Thread(target=pars, args=(i,)).start()

                eror = 3
        except:
                print('произошла ощибка - запускаю заного')
                eror+=1
                print('\n', 'перезапуск-', eror,'/3')
