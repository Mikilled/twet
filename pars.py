from selenium import webdriver
from selenium_stealth import stealth
import pickle
import time



def main_opensea():
        global links
        driver.get('https://opensea.io/activity/')
        time.sleep(3)
        all_block = driver.find_elements_by_css_selector('.hmswhC')
        print(all_block)
        links = []
        for block in all_block:
                a = block.get_attribute('href')
                links.append(a)
        print(links)




def search_twit():
        global links
        global twiters
        for link in links:
                driver.get(link)
                a = driver.find_elements_by_xpath('//*[@id="main"]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[1]/a')
                if len(a) != 0:
                        for i in a:
                                b = i.get_attribute('href')
                                if 'twit' in b:
                                        print(b)
                                        twiters.append(b)





def twiter():
        global globtwiters
        globtwiters = list(set(globtwiters))
        global twiters
        global freetwit
        for twit in globtwiters:
                driver.get(twit)
                time.sleep(2)
                tw = driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/span')
                if len(tw) != 0:
                        print('found')
                        freetwit.append(twit)
                else:
                        print('not found')
                        continue




options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)


options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(chrome_options=chrome_options, options=options, executable_path=r"C:\chromedriver.exe")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

print("PARSER Opensea v1.1")
print("https://chromedriver.storage.googleapis.com/index.html?path=101.0.4951.41/")
print("должно быть установленно в корень диска c и прописано в PATH")



n = int(input('введите кол-во прогонов по opensea\n'))
save = input('введите путь куда сохранить твитеры(без ковычек)\n')
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
for cookie in pickle.load(open("C:\wit\cookies.pkl", "rb")):
    driver.add_cookie(cookie)
time.sleep(2)

twiter()

print(freetwit)
j = ''
f = open(save, 'w',encoding="utf-8")
for i in range(len(freetwit)):
        j = freetwit[i]
        f.write(j+'\n')
f.close()





