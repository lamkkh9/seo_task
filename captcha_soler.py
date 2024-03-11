import requests
import json
import time , re
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import urlparse, parse_qs
from pathlib import Path

import os, shutil, time, requests, random


def Session():
    session = requests.Session()
    retry = Retry(connect=5, backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

class Api_GXP:
    def __init__(self, api_key):
        self.url = "http://sctg.xyz"
        self.key = api_key
        self.max_wait = 300
        self.sleep = 5

    def in_api(self, data):
        session = Session()
        params = {"key": (None, self.key)}
        for key in data:
            params[key] = (None, data[key])
        return session.post(self.url + '/in.php', files=params, verify=False, timeout=15)

    def res_api(self, api_id):
        session = Session()
        params = {"key": self.key, "id": api_id}
        return session.get(self.url + '/res.php', params=params, verify=False, timeout=15)
        
    def get_balance(self):
        session = Session()
        params = {"key": self.key, "action": "getbalance"}
        return session.get(self.url + '/res.php', params=params, verify=False, timeout=15).text

    def run(self, data):
        get_in = self.in_api(data)
        if get_in:
            if "|" in get_in.text:
                api_id = get_in.text.split("|")[1]
            else:
                return get_in.text
        else:
            return "ERROR_CAPTCHA_UNSOLVABLE"
        for i in range(self.max_wait//self.sleep):
            time.sleep(self.sleep)
            get_res = self.res_api(api_id)
            if get_res:
                answer = get_res.text
                if 'CAPCHA_NOT_READY' in answer:
                    continue
                elif "|" in answer:
                    return answer.split("|")[1]
                else:
                    return answer


def captcha(driver):
    api_key = "fb3wCbJlIHPsfEMj74d32dx6oaLeUGc7"  # Thay YOUR_API_KEY bằng khóa API của bạn
    api = Api_GXP(api_key)

    print(api.get_balance())
    elements = driver.find_elements(By.CLASS_NAME, "out-capcha-lab")
    # Tạo một mảng để chứa style của các phần tử
    styles = []
    # Lặp qua 6 phần tử đầu tiên và lấy style của chúng
    for i in range(min(6, len(elements))):
        element = elements[i]
        style = element.get_attribute("style").split('base64,')[1].split('"')[0]
        styles.append(style)
    text = driver.find_element(By.CLASS_NAME, "out-capcha-title").text
    print(text)
    data = {
        "method": "profit",
        "body_1": f"{styles[0]}",
        "body_2": f"{styles[1]}",
        "body_3": f"{styles[2]}",
        "body_4": f"{styles[3]}",
        "body_5": f"{styles[4]}",
        "body_6": f"{styles[5]}",
        "textinstructions": f"{text}"
    }
    profit = api.run(data)

    indices = [int(index) for index in profit.split(",")]
    action = ActionChains(driver)
    for index in indices:
        element_index = index - 1
        if 0 <= element_index < len(elements):
            action.move_to_element(elements[element_index]).click()
    action.perform()

    
    



def create_or_load_profile(profile_path):
    if not os.path.exists(profile_path):
        try:
            # Tạo mới profile nếu thư mục không tồn tại
            shutil.copytree("default_profile", profile_path)  # Thay "default_profile" bằng thư mục mẫu hoặc trống
            print("Created a new profile.")
        except FileNotFoundError:
            print("Thư mục mẫu 'default_profile' không tồn tại.")
    else:
        print("Using an existing profile.")

# Cấu hình ChromeOptions và DesiredCapabilities
chrome_options = Options()
profile_path = os.getcwd() + '/thorium'
create_or_load_profile(profile_path)
chrome_options.add_argument(f'--user-data-dir={profile_path}')

# Ẩn cửa sổ trình duyệt
#chrome_options.add_argument("--headless")

# Tắt thông tin địa phương
chrome_options.add_argument("--disable-features=TranslateUI")
# Tắt Canvas
chrome_options.add_argument("--disable-2d-canvas")
# Tắt Client Rects
chrome_options.add_argument("--disable-prompt-on-repost")

# Tắt WebGL Image
chrome_options.add_argument("--disable-webgl-image-chromium")
# Tắt WebRTC
chrome_options.add_argument("--disable-webrtc")
# Tắt audio context
chrome_options.add_argument("--disable-audio-api")
# Tắt cảnh báo và thông báo

chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument('--no-first-run')
chrome_options.add_argument('--no-service-autorun')
chrome_options.add_argument('--password-store-basic')
chrome_options.add_argument('--no-service-autorun')
chrome_options.add_argument('--lang=en-US')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-cpu')
    
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.default_content_setting_values.notifications": 2,
    "download_restrictions": 3
}
    
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--enable-main-frame-before-activation')
chrome_options.add_argument('--display-capture-permissions-policy-allowed')
chrome_options.add_argument('--device-scale-factor=1')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-plugins-discovery')
chrome_options.add_argument('--disable-gpu-shader-disk-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--disable-page-load-check')
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--log-level=3')
thorium_binary_path = "C:\\Users\\ghost\\AppData\\Local\\Thorium\\Application\\thorium.exe"
chrome_options.binary_location = thorium_binary_path
# Tạo thông tin giả mạo cho phiên bản trình duyệt
browser_version = "120.0.6099.110"
chrome_options.add_argument(f"--version={browser_version}")

# Sử dụng user agent được chỉ định
chrome_options.add_argument("--name=Chrome")
# Đặt cấu hình cho DesiredCapabilities

driver = webdriver.Chrome(options=chrome_options)


api_key = "3239dd0885ef73d7249e20bfc6cb63dc"

# Mở trang web cần kiểm tra
driver.get("https://profitcentr.com/")
time.sleep(2)
login = driver.find_elements(By.CLASS_NAME, "btn.btn_second.btn_log")
if len(login) != 0 :
    login[0].click()
    email = "lamkkh9"
    pass_word = "f28oz4yd"
    username = driver.find_element(By.NAME, "username")

    username.click()
    for char in email:
        username.send_keys(char)
        time.sleep(0.25)

    password = driver.find_element(By.NAME, "password")

    password.click()
    for char in pass_word:
        password.send_keys(char)
        time.sleep(0.25)
    print(len(driver.find_elements(By.XPATH, '//div[@class="out-capcha"]')))
    if len(driver.find_elements(By.XPATH, '//div[@class="out-capcha"]')) != 0 :
        captcha(driver)
    


    driver.find_element(By.CLASS_NAME, "btn_big_green").click()




erro_sst = 0

try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//span[@id="mnu_title1"]'))
    )
    if driver.find_elements(By.XPATH, '//div[@class="usermnublock"]')[0].get_attribute("style") == "display: none;":
        element.click()
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//a[text()="YouTube"]'))
    )
    # Click vào phần tử
    element.click()
    time.sleep(4)
    stt_job = 1
    stt_job_1 = 0
    while(True):
        if len(driver.find_elements(By.XPATH, '//div[@class="out-capcha"]')) != 0 :
            captcha(driver)
            time.sleep(2)
            driver.find_elements(By.XPATH, '//span[text()="Пройти проверку"]')[0].click()
            time.sleep(5) 
            print(len(driver.find_elements(By.XPATH, '//td[@class="normal"]'))/3)
        driver.find_elements(By.XPATH, '//td[@class="normal"]')[stt_job].find_element(By.TAG_NAME, 'span').click()
        time.sleep(8)
        if len(driver.find_elements(By.XPATH, '//span[@class="youtube-error"]')) <= erro_sst :
            driver.find_elements(By.XPATH, '//div[@class="youtube-button"]')[stt_job_1].click()
            time.sleep(5)
            handles = driver.window_handles
            driver.switch_to.window(handles[1])
            time.sleep(2)
            try :
                iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "video-start")))
                driver.switch_to.frame(iframe)
                play_youtube = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'ytp-large-play-button'))
                    )
                    # Sau khi phần tử xuất hiện, click vào nó
                ytp-error-content-wrap-reason  Video unavailable
                play_youtube.click()
                driver.switch_to.default_content()
                while(True):
                    timer_element = driver.find_element(By.ID , "tmr")
                    if  timer_element.text != "0":
                        time.sleep(1)
                    else:
                        random_number = random.randint(5, 9)
                        time.sleep(random_number)
                        driver.find_element(By.XPATH, '//button[text()="Подтвердить просмотр"]').click()
                        stt_job = stt_job + 3
                        stt_job_1 = stt_job_1 + 1
                        random_number = random.randint(4, 8)
                        time.sleep(random_number)
                        driver.close()
                        driver.switch_to.window(handles[0])
                        break
            except TimeoutException:
                print("loi") 
        else :
            erro_sst = erro_sst+1 
        random_number = random.randint(4, 8)
        time.sleep(random_number)
except TimeoutException:
    print("Không thể tìm thấy phần tử sau 10 giây.")



time.sleep(1000)
