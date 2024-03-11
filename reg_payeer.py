from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from urllib.parse import urlparse, parse_qs
from pathlib import Path
from extension import proxies


import os, shutil, time, requests, random
import time


def ghi_vao_file(ten_file, du_lieu):
    if not os.path.exists(ten_file):
        with open(ten_file, "w") as file:
            file.write(du_lieu)
    else: #<span style="font: bold 21px / 28px Arial, normal, serif, EmojiFont; text-align: center; color: rgb(51, 204, 0); background-color: rgba(51, 204, 0, 0.1); border-radius: 10px; padding: 11px 24px 9px;">53492</span>
        with open(ten_file, "a") as file:
            file.write(du_lieu)


def get_data(stt_acc):
    file_path = os.path.join(os.getcwd() + "\\data", "mail.txt")
    with open(file_path, "r") as file:
        data = file.readlines()
        
        return data[stt_acc]

def get_messages(email, password):
    url = "https://tools.dongvanfb.net/api/get_messages"
    params = {
        "mail": email,
        "pass": password
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    # Check if the response contains messages
    if "messages" in data:
        # Extract the verification code from the third message
        message_content = str(data["messages"][0])
        print(message_content)
        return message_content.split('border-radius: 10px;\\n           padding: 11px 24px 9px 24px;\\n      ">')[1].split('</span>')[0]
    else:
        return None





def ChromeDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-first-run')
    options.add_argument('--no-service-autorun')
    options.add_argument('--password-store-basic')
    options.add_argument('--no-service-autorun')
    options.add_argument('--lang=en-US')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-cpu')
    options.add_argument("--disable-webgl")
    options.add_argument("--disable-canvas")
    options.add_argument("--disable-audio-api")
    options.add_argument("--disable-client-rects")
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "download_restrictions": 3
    }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--enable-main-frame-before-activation')
    options.add_argument('--display-capture-permissions-policy-allowed')
    options.add_argument('--device-scale-factor=1')
    options.add_argument('--disable-web-security')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-plugins-discovery')
    options.add_argument('--disable-gpu-shader-disk-cache')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    thorium_binary_path = "C:\\Users\\ghost\\AppData\\Local\\Thorium\\Application\\thorium.exe"
    options.binary_location = thorium_binary_path
    driver = webdriver.Chrome(options=options)
    return driver
stt_acc = 0
# Example usage:
driver = ChromeDriver()
driver.get("https://payeer.com/en/auth/?register=yes")
# Continue with your automation...
data_acc = get_data(stt_acc)
email = data_acc.split("|")[0]
pass_mail = data_acc.split("|")[1]
input_element = driver.find_element(By.XPATH, '//input[@name="email"]')
input_element.click()
for char in email:
    input_element.send_keys(char)
    time.sleep(0.25)
driver.find_element(By.XPATH, "//button[contains(text(), 'Create Account')]").click()
time.sleep(5)
code = get_messages(email, pass_mail)
input_element = driver.find_element(By.XPATH, '//input[@name="code"]')
input_element.click()
for char in code:
    input_element.send_keys(char)
    time.sleep(0.25)
time.sleep(2)
button_element = driver.find_element(By.XPATH, "//button[@class='login-form__login-btn step2']")
button_element.click()
time.sleep(5)
input_element_1 = driver.find_element(By.XPATH, '//input[@name="new_password"]')
value_1 = input_element_1.get_attribute("value")
print("Giá trị của new_password:", value_1)

# Tìm phần tử input thứ hai
input_element_2 = driver.find_element(By.XPATH, '//input[@name="secret_word"]')
value_2 = input_element_2.get_attribute("value")
print("Giá trị của secret_word:", value_2)

# Tìm phần tử input thứ ba
input_element_3 = driver.find_element(By.XPATH, '//input[@name="nick"]')
value_3 = input_element_3.get_attribute("value")
print("Giá trị của nick:", value_3)
next_button = driver.find_element(By.CSS_SELECTOR, 'button.login-form__login-btn.mini-mid-btn')
next_button.click()
time.sleep(4)

name_input = driver.find_element(By.NAME, "name")
name_input.send_keys("John")
last_name_input = driver.find_element(By.NAME, "last_name")
last_name_input.send_keys("Smith")
done_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="login-form__login-btn mini-mid-btn" and not(@disabled)]'))
)

# Click vào nút "Done"
done_button.click()
data_done = email+'|'+pass_mail+'|'+email+"|"+value_1+'|'+value_2+'|'+value_3
file_path = os.path.join(os.getcwd() + "\\data", "test.txt")
ghi_vao_file(file_path, data_done+"\n")




time.sleep(10000)











