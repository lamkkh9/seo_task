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
from extension import proxies


import os, shutil, time, requests, random

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
profile_path = os.getcwd() + '/chrome'
create_or_load_profile(profile_path)
chrome_options.add_argument(f'--user-data-dir={profile_path}')
proxy = "171.240.240.194:40301"
# Ẩn cửa sổ trình duyệt
#chrome_options.add_argument("--headless")
#chrome_options.add_argument('--proxy-server=%s' % proxy)
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

file_name = os.getcwd()+f"/proxies_extension.zip"
if os.path.exists(file_name):
    os.remove(file_name)


proxies_extension = proxies("HPXu1B", "A7crFz3U0P", "31.12.95.70", "3000")
chrome_options.add_extension(proxies_extension)
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
driver.get("https://seo-task.com/register")
time.sleep(5)


import random
import string






def login():
    try:
    # Lấy giá trị của thuộc tính 'src' của phần tử iframe
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )
        
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        iframe_src = iframe.get_attribute("src")
        site_key = iframe_src.split("https://google.com/recaptcha/api2/anchor?ar=1&k=")[1].split("&co=")[0]
        print("api_key captcha : "+site_key)
        api_key = "3239dd0885ef73d7249e20bfc6cb63dc"
        input_element =driver.find_element(By.XPATH, '//input[@name="login"]')
        time.sleep(1)
        url = "http://api.cap.guru/in.php"
        payload = {
            "key": api_key,
            "method": "userrecaptcha",
            "googlekey": f"{site_key}",
            "pageurl": "https://seo-task.com/login",
            "json": 1
        }
        response = requests.post(url, json=payload)
        result = response.json()
        input_element.click()
        first_names = ['John', 'Emma', 'Michael', 'Sophia', 'William', 'Olivia', 'James', 'Ava', 'Alexander', 'Isabella']
        last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
        punctuation = ['.','_']
        # Chọn một tên và họ ngẫu nhiên từ danh sách
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        
        special_character = random.choice(punctuation)
        login = f"{first_name}{special_character}{last_name}"
        
        if len(login) > 15:
            login = login[:15]
        elif len(login) < 4:
            login = login.ljust(4, 'x')
        
        email = "lamkkh9@hotmail.com"
        pass_word = "xGaujk12@"

        for char in login:
            input_element.send_keys(char)
            time.sleep(0.25)      
        print(login)
        
        input_element = driver.find_element(By.XPATH, '//input[@name="email"]')
        input_element.click()
        for char in email:
            input_element.send_keys(char)
            time.sleep(0.25)
        print(email)
        
        input_element = driver.find_element(By.XPATH, '//input[@name="password"]')
        input_element.click()
        for char in pass_word:
            input_element.send_keys(char)
            time.sleep(0.25)
        print(pass_word)
        check_bypass = 0
        id_captcha = result['request']
        while(True):
            url = "http://api.cap.guru/res.php"
            payload = {
                "key": api_key,
                "action": "get",
                "id": f"{id_captcha}",
                "json": 1
            }
            # Отправка POST-запроса
            response = requests.post(url, json=payload)
            # Печать ответа от сервера
            result = response.json()
            if result['status'] == 1:
                g_recaptcha_response = result['request']
                print("Giai thanh cong captcha v2")
                break
            else :
                if check_bypass == 15:
                    print("Khong the giai captcha v3")
                    break
                time.sleep(10)
                check_bypass =  check_bypass + 1
       
        driver.execute_script("document.getElementsByClassName(`g-recaptcha-response`)[0].innerHTML = " f"'{g_recaptcha_response}';")
        driver.find_elements(By.XPATH, '//button[@class="button f-spinner"]')[0].click()
    except:
        print("Không tìm thấy phần tử sau 20 giây.")

login()





time.sleep(10000)