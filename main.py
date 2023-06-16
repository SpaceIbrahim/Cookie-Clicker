from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import keyboard
import time

# with open("save.txt", 'w') as code:
#     code.write("AMONG US")

i = 1
options = Options()
options.add_experimental_option('detach', True)
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
service = Service(r"C:\Users\pace\Documents\Development\chromedriver_win32\chromedriver.exe")
window = webdriver.Chrome(service=service,options=options)

LINK = "https://orteil.dashnet.org/cookieclicker/"
window.get(LINK)

time.sleep(6)
print(i)
window.find_element(By.XPATH, "/html/body/div[1]/div/a[1]").click()

lang_select = window.find_element(By.ID, "langSelect-EN")
lang_select.click()

time.sleep(10)
with open("save.txt", 'r') as code:
    window.find_element(By.ID, "prefsButton").click()
    window.find_element(By.XPATH, '//*[@id="menu"]/div[3]/div/div[4]/a[2]').click()
    export_code = window.find_element(By.ID, "textareaPrompt")
    export_code.send_keys(code.read())
    time.sleep(3)
    load = window.find_element(By.ID, "promptOption0")
    load.click()
    time.sleep(1)
    window.find_element(By.XPATH, '//*[@id="menu"]/div[1]').click()
    
COOKIE = window.find_element(By.ID, "bigCookie")

start = int(time.time())
current = int(time.time())
while i == 1:
    
    COOKIE.click()
    
    if current > start + 5:
        print("CHECKED")
        try:
            unlocked = window.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
            print([n.text for n in unlocked])
            unlocked[len(unlocked)-1].click()
        except:
            pass
        try:
            upgrades = window.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")
            print([n.text for n in upgrades])
            upgrades[len(upgrades)-1].click()
        except:
            pass
        start = current
    if keyboard.is_pressed('q'):
        with open("save.txt", 'w') as code:
            try:
                window.find_element(By.ID, "prefsButton").click()
                window.find_element(By.XPATH, '//*[@id="menu"]/div[3]/div/div[3]').click()
                time.sleep(1)
                window.find_element(By.XPATH, '//*[@id="menu"]/div[3]/div/div[4]/a[1]').click()
                export_code = window.find_element(By.ID, "textareaPrompt")
            except:
                print("ERROR")
                break
            else:
                time.sleep(1)
                code.write(export_code.text)
                time.sleep(3)
        window.close()
        i = 0
    elif keyboard.is_pressed('w'):
        username = input("Enter username: ")
        print("Username is: " + username)
    current = int(time.time())
    