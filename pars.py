from selenium import webdriver
from selenium_stealth import stealth
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
                a = driver.find_elements_by_xpath(
                        '//*[@id="main"]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[1]/a')
                if len(a) != 0:
                        for i in a:
                                b = i.get_attribute('href')
                                if 'twit' in b:
                                        print(b)
                                        twiters.append(b)

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r"C:\chromedriver.exe")

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
while c != n:
        links = []
        twiters = []
        main_opensea()
        search_twit()
        globtwiters = globtwiters + twiters
        c+=1

f = open(save, 'w',encoding="utf-8")
for i in range(len(globtwiters)):
        с = globtwiters[i]
        f.write(c+'\n')
f.close()





















# driver.get('https://opensea.io/pashanimgotbag')
# time.sleep(2)
# a = driver.find_elements_by_xpath('//*[@id="main"]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[1]/a')
# if len(a) != 0:
#         for i in a:
#                 b = i.get_attribute('href')
#                 if 'twit' in b:
#                         print(b)
#
# # for i in all_block:
# #         print(i)
# #         print(i.get_attribute('href'))

