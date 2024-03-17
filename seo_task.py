
#hotmail|pass_hotmail|proxy|user_name|pass|payeer|pass_payeer|Secret_сode





import concurrent.futures
import os
import threading
import random
import time
import string
from bs4 import BeautifulSoup
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

def get_data():
    global stt_acc
    with lock:
        file_path = os.path.join(os.getcwd() + "\\data\\acc_seotask.txt")
        with open(file_path, "r") as file:
            data = file.readlines()
            if stt_acc < len(data):
                acc_data = data[stt_acc]
                stt_acc += 1
                return acc_data
            else:
                exit()


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








def login():
    # Cấu hình ChromeOptions và DesiredCapabilities
    chrome_options = Options()
    profile_path = os.getcwd() + '/chrome'
    #create_or_load_profile(profile_path)
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-features=TranslateUI")
    chrome_options.add_argument("--disable-2d-canvas")
    chrome_options.add_argument("--disable-prompt-on-repost")
    chrome_options.add_argument("--disable-webgl-image-chromium")
    chrome_options.add_argument("--disable-webrtc")
    chrome_options.add_argument("--disable-audio-api")
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
    chrome_options.add_argument("--window-size=1920,1080") 
    chrome_options.add_argument("--force-device-scale-factor=0.25")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    """thorium_binary_path = "C:\\Users\\ghost\\AppData\\Local\\Thorium\\Application\\thorium.exe"
    chrome_options.binary_location = thorium_binary_path
    browser_version = "120.0.6099.110"
    chrome_options.add_argument(f"--version={browser_version}")
    chrome_options.add_argument("--name=Chrome")"""
    acc = get_data()
    if len(acc.split("|")) == 3 :
        mail , pass_mail , proxy = acc.split("|")
        if proxy != "":
            if len(proxy.split(":")) == 4 :
                ip_proxy, port_proxy,user_proxy, pass_proxy = proxy.split(":")
            else:
                user_proxy = ""
                pass_proxy = ""
                ip_proxy, port_proxy = proxy.split(":")
            proxies_extension = proxies(user_proxy, pass_proxy.split("\n")[0], ip_proxy, port_proxy)
            chrome_options.add_extension(os.getcwd()+f"\\{ip_proxy}_{port_proxy}\\proxies_extension.zip")
    elif len(acc.split("|")) == 2 :
        mail , pass_mail  = acc.split("|")
    elif len(acc.split("|")) == 6 :
        mail , pass_mail , proxy , user_payeer , pass_payeer , Secret_сode  = acc.split("|")
        if proxy != "":
            if len(proxy.split(":")) == 4 :
                ip_proxy, port_proxy,user_proxy, pass_proxy = proxy.split(":")
            else:
                user_proxy = ""
                pass_proxy = ""
                ip_proxy, port_proxy = proxy.split(":")
            proxies_extension = proxies(user_proxy, pass_proxy.split("\n")[0], ip_proxy, port_proxy)
            chrome_options.add_extension(os.getcwd()+f"\\{ip_proxy}_{port_proxy}\\proxies_extension.zip")
    elif len(acc.split("|")) == 8 :
        mail , pass_mail , proxy , user_payeer , pass_payeer , Secret_сode, user_name , pass_word  = acc.split("|")
        if proxy != "":
            if len(proxy.split(":")) == 4 :
                ip_proxy, port_proxy,user_proxy, pass_proxy = proxy.split(":")
            else:
                user_proxy = ""
                pass_proxy = ""
                ip_proxy, port_proxy = proxy.split(":")
            proxies_extension = proxies(user_proxy, pass_proxy.split("\n")[0], ip_proxy, port_proxy)
            chrome_options.add_extension(os.getcwd()+f"\\{ip_proxy}_{port_proxy}\\proxies_extension.zip")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://kiemtraip.com/raw.php")
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    ip_address = soup.body.get_text()
    api_key = "3239dd0885ef73d7249e20bfc6cb63dc"
    driver.get("https://seo-task.com/login")
    time.sleep(5)
    print("["+mail+"]:"+ip_address)
    try:
    # Lấy giá trị của thuộc tính 'src' của phần tử iframe
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )
        iframe_src = iframe.get_attribute("src")
        site_key = iframe_src.split("https://google.com/recaptcha/api2/anchor?ar=1&k=")[1].split("&co=")[0]
        #print("api_key captcha : "+site_key)
        api_key = "3239dd0885ef73d7249e20bfc6cb63dc"
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
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="login"]'))
        )
        input_element.click()

        for char in mail:
            input_element.send_keys(char)
            time.sleep(0.25)      
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))
        )
        input_element.click()
        for char in pass_mail:
            input_element.send_keys(char)
            time.sleep(0.25)

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
                print("["+mail+"]:Giai thanh cong captcha v2")
                break
            else :
                if check_bypass == 15:
                    print("["+mail+"]:Khong the giai captcha v2")
                    break
                time.sleep(10)
                check_bypass =  check_bypass + 1
        driver.execute_script("document.getElementsByClassName(`g-recaptcha-response`)[0].innerHTML = " f"'{g_recaptcha_response}';")
        driver.find_elements(By.XPATH, '//button[@class="button f-spinner"]')[0].click()
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.footer-error'))
            )
        if element:
            error_text = element.text.split("\n")[0]
            if  error_text == "Данный Логин или E-mail не зарегистрирован на проекте":
                print("["+mail+"]:Email khong ton tai")
                register(driver,mail,pass_mail)
    except:
        print("Không tìm thấy phần tử sau 10 giây.")
    return driver,mail

def register(driver,mail,pass_mail):
    driver.get("https://seo-task.com/register")
    time.sleep(5)
    try:
    # Lấy giá trị của thuộc tính 'src' của phần tử iframe
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        iframe_src = iframe.get_attribute("src")
        site_key = iframe_src.split("https://google.com/recaptcha/api2/anchor?ar=1&k=")[1].split("&co=")[0]
        api_key = "3239dd0885ef73d7249e20bfc6cb63dc"
        input_element =driver.find_element(By.XPATH, '//input[@name="login"]')
        time.sleep(1)
        url = "http://api.cap.guru/in.php"
        payload = {
            "key": api_key,
            "method": "userrecaptcha",
            "googlekey": f"{site_key}",
            "pageurl": "https://seo-task.com/register",
            "json": 1
        }
        response = requests.post(url, json=payload)
        result = response.json()
        input_element.click()
        url = "https://api.name-fake.com/english-united-states/female"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        name_div = soup.find("div", class_="subj_div_45g45gg", id="copy3")
        login = name_div.text
        if len(login) > 15:
            login = login[:15]
        elif len(login) < 4:
            login = login.ljust(4, 'x')
        for char in login:
            input_element.send_keys(char)
            time.sleep(0.25)      
        input_element = driver.find_element(By.XPATH, '//input[@name="email"]')
        input_element.click()
        for char in mail:
            input_element.send_keys(char)
            time.sleep(0.25)
        input_element = driver.find_element(By.XPATH, '//input[@name="password"]')
        input_element.click()
        for char in pass_mail:
            input_element.send_keys(char)
            time.sleep(0.25)
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
            response = requests.post(url, json=payload)
            result = response.json()
            if result['status'] == 1:
                g_recaptcha_response = result['request']
                print("["+mail+"]:Giai thanh cong captcha v2")
                break
            else :
                if check_bypass == 15:
                    print("["+mail+"]:Khong the giai captcha v2")
                    break
                time.sleep(10)
                check_bypass =  check_bypass + 1
        driver.execute_script("document.getElementsByClassName(`g-recaptcha-response`)[0].innerHTML = " f"'{g_recaptcha_response}';")
        driver.find_elements(By.XPATH, '//button[@class="button f-spinner"]')[0].click()
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.footer-error'))
            )
        if element:
            error_text = element.text.split("\n")[0]
            print(error_text)
            if  error_text == "Данный Логин или E-mail не зарегистрирован на проекте":
                print("["+mail+"]:Email khong ton tai")
                register(driver,mail,pass_mail)
        # xác minh
    except:
        print("Không tìm thấy phần tử sau 20 giây.")
def start():
    driver,mail = login()
    time.sleep(5)
    stt_job = 0
    video_error = 0
    error_ip = 1
    while(True):
        if video_error == 2:  
            video_error = 0
            break
        if len(driver.find_elements(By.CLASS_NAME, 'info.info_warning'))==1 :
                break
        try:
            link_job = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'list-name'))
            )
            if len(driver.find_elements(By.CLASS_NAME, 'list-name')) == 0:
                driver.refresh()
                time.sleep(3)
                if len(driver.find_elements(By.CLASS_NAME, 'list-name')) == 0:
                    driver.quit()
                link_job = driver.find_element(By.CLASS_NAME, 'list-name')
            link_youtube_1 = link_job.get_attribute("onclick")
            link_youtube = link_youtube_1.split("ajax_func=")[1].split("'")[0]
            actions = ActionChains(driver)
            actions.move_to_element(link_job).perform()
            actions.reset_actions()
            if len(driver.find_elements(By.CLASS_NAME, 'policy_button')) != 0 :
                driver.find_element(By.CLASS_NAME, 'policy_button').click()
                time.sleep(1)
            link_job.click()
            time.sleep(5)
            if len(driver.find_elements(By.XPATH, "//div[@class='red']")) < error_ip:
                handles = driver.window_handles
                driver.switch_to.window(handles[1])
                try:
                    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "id_video")))
                except TimeoutException:
                    print('khong tim thay  frame')
                try:
                    # Chờ đợi tối đa 10 giây cho phần tử xuất hiện
                    play_youtube = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'ytp-large-play-button'))
                    )
                    # Sau khi phần tử xuất hiện, click vào nó
                    if len(driver.find_elements(By.CLASS_NAME, 'ytp-error-content-wrap-reason')) != 0:
                        video_error = video_error + 1  
                    else:
                        video_error = 0
                        play_youtube.click()
                        driver.switch_to.default_content()
                        timer_check = 0
                        while(True):
                            timer_element = driver.find_elements(By.ID , "timer")
                            if  len(timer_element) == 1:
                                time.sleep(1)
                                if timer_check == 15:
                                    driver.refresh()
                                    time.sleep(2)
                                    driver.switch_to.frame("id_video")
                                    play_youtube = WebDriverWait(driver, 20).until(
                                        EC.presence_of_element_located((By.CLASS_NAME, 'ytp-large-play-button'))
                                    )
                                    if len(driver.find_elements(By.CLASS_NAME, 'ytp-error-content-wrap-reason')) == 0:
                                        play_youtube.click()
                                    else:
                                        print(driver.find_elements(By.CLASS_NAME, 'ytp-error-content-wrap-reason')[0].text)
                                        driver.switch_to.default_content()
                                        break
                                    driver.switch_to.default_content()
                                timer_check = timer_check + 1
                            else :
                                button = WebDriverWait(driver, 10).until(
                                    EC.presence_of_element_located((By.XPATH, '//span[text()="Подтвердить просмотр"]'))
                                )
                                button.click()
                                print("["+mail+"]:Success")
                                random_number = random.randint(1, 5)
                                time.sleep(random_number)
                                break
                    driver.close()
                    driver.switch_to.window(handles[0])
                    stt_job = stt_job + 1
                except TimeoutException:
                    print("Phần tử không xuất hiện sau thời gian chờ")
            else :
                error_ip = error_ip+1
                print("["+mail+"]:failed")
        except TimeoutException :
            driver.refresh()
        random_number = random.randint(1, 20)
        time.sleep(random_number)
    stt_job = 0
    driver.get("https://seo-task.com/job_serf")
    time.sleep(5)
    error_ip = 1
    while(True):
        if len(driver.find_elements(By.CLASS_NAME, 'info.info_warning'))==1 :
                break
        try:
            link_job = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'list-name'))
            )
            if len(driver.find_elements(By.CLASS_NAME, 'list-name')) == 0:
                driver.refresh()
                time.sleep(3)
                if len(driver.find_elements(By.CLASS_NAME, 'list-name')) == 0:
                    driver.quit()
                link_job = driver.find_element(By.CLASS_NAME, 'list-name')
            link_youtube_1 = link_job.get_attribute("onclick")
            link_youtube = link_youtube_1.split("ajax_func=")[1].split("'")[0]
            actions = ActionChains(driver)
            actions.move_to_element(link_job).perform()
            if len(driver.find_elements(By.CLASS_NAME, 'policy_button')) != 0 :
                driver.find_element(By.CLASS_NAME, 'policy_button').click()
                time.sleep(1)
            link_job.click()
            actions.reset_actions()
            time.sleep(5)
            if len(driver.find_elements(By.XPATH, "//div[@class='red']")) < error_ip:
                handles = driver.window_handles
                driver.switch_to.window(handles[1])
                timer_check = 0
                while(True):
                    timer_element = driver.find_elements(By.ID , "timer")
                    if  len(timer_element) == 1:
                        time.sleep(1)
                        if timer_check == 40:
                            driver.refresh()
                            time.sleep(2)
                        timer_check = timer_check + 1
                    else :
                        time.sleep(2)
                        try:
                            button = WebDriverWait(driver, 20).until(
                                EC.presence_of_element_located((By.XPATH, "//span[text()='Подтвердить просмотр']"))
                            )
                            button.click()
                            print("["+mail+"]:Success")
                            random_number = random.randint(1, 5)
                            time.sleep(random_number)
                        except TimeoutException :
                            print("["+mail+"]:Failed")
                        break
                driver.close()
                driver.switch_to.window(handles[0])
                time.sleep(3)
            else :
                error_ip = error_ip+1
                print("["+mail+"]:Failed")
        except TimeoutException :
            driver.refresh()
        random_number = random.randint(1, 20)
        time.sleep(random_number)
    driver.get("https://seo-task.com/pay_out")
    time.sleep(2)
    #class pay-cur pay-t-min  "Укажите кошелек"
    print("["+mail+"]:Done")
    driver.quit()
max_workers = 2
stt_acc = 1
lock = threading.Lock()
def run_threads(max_workers):
    while True:  # Lặp vô hạn cho đến khi hết dữ liệu trong file
        stt_acc = 0  # Thiết lập lại stt_acc cho mỗi lần lặp
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(start, ) for _ in range(max_workers)}
            for future in concurrent.futures.as_completed(futures):
                try:
                    result = future.result()
                    print(result)
                except Exception as exc:
                    print(f"Error processing: {exc}")
        # Kiểm tra xem dữ liệu còn trong file hay không
        file_path = os.path.join(os.getcwd() + "\\data", "acc_seotask.txt")
        with open(file_path, "r") as file:
            data = file.readlines()
            if stt_acc >= len(data):  # Nếu stt_acc lớn hơn hoặc bằng tổng số dòng trong file
                break  # Dừng vòng lặp
if __name__ == "__main__":
    run_threads(max_workers)