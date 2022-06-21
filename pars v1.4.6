from selenium_stealth import stealth
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import time
import datetime
import threading
from threading import Thread
from queue import Queue


def main_opensea(str2,url):
        links = []
        globals()[str2].get(url)
        time.sleep(4)
        all_block = globals()[str2].find_elements(By.CSS_SELECTOR, '.hmswhC')
        for block in all_block:
                a = block.get_attribute('href')
                links.append(a)
        search_twit(str2,links)


def search_twit(str2,links):
        global all_twit
        for link in links:
                globals()[str2].get(link)
                a = globals()[str2].find_elements(By.XPATH, '//*[@id="main"]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[1]/a')
                if len(a) != 0:
                        for i in a:
                                b = i.get_attribute('href')
                                if 'twitter' in b:
                                        if not(b in all_twit):
                                                all_twit.append(b)
                                                queue1.put(b)



def twiter():
        global freetwit
        global now
        f = open(now, 'a', encoding="utf-8")
        globtwiters = []
        while queue1.empty() != True:
                globtwiters.append(queue1.get())
        for twit in globtwiters:
                driver1.get(twit)
                time.sleep(4)
                tw = driver1.find_elements(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/span')
                if len(tw) != 0:
                        print(twit)
                        f.write(twit + '\n')
                        freetwit.append(twit)
                else:
                        continue
        f.close()





def check_twit():
        global  now
        global driver1
        global freetwit
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
        freetwit = []
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
                        break
        driver1.quit()


def pars_opensea(i,url):
        global n
        global all_twit
        j = i+1
        str2 = "driver" + str(j)

        print("запуск потока - PARSER Opensea-",i)
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
        print("поток чекера opensea запущен-",i)
        c = 0
        all_twit = []
        while c != n:
                main_opensea(str2,url)
                c += 1

        globals()[str2].quit()





print("PARSER Opensea v1.4.6")
now = str((datetime.datetime.today()).strftime("%Y-%m-%d-%H-%M-%S.txt"))
url1='https://opensea.io/activity?search[chains][0]=ETHEREUM&search[eventTypes][0]=AUCTION_SUCCESSFUL'
url2='https://opensea.io/activity?search[eventTypes][0]=AUCTION_CREATED&search[chains][0]=ETHEREUM'
n = int(input('введите кол-во прогонов'))
eror = 0
while eror !=3:
        try:
                try:
                        f = open('config.txt', 'r',encoding="utf-8")
                        cooks = str(f.readline())
                except FileNotFoundError:
                        f = open('config.txt', 'w', encoding="utf-8")
                        print('Конфиг не обнаружен - нужно создать')
                        cooks = input('введите путь до куки-')
                        f.write(cooks)
                f.close()



                queue1 = Queue()
                time.sleep(1)
                th1 = Thread(target=check_twit).start()
                time.sleep(1)
                th2 = Thread(target=pars_opensea, args=(1,url1 )).start()
                time.sleep(1)
                th3 = Thread(target=pars_opensea, args=(2,url2 )).start()
                eror = 3
        except:
                print('произошла ощибка - запускаю заного')
                eror+=1
                print('\n', 'перезапуск-', eror,'/3')
