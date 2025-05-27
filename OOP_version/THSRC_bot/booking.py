import random, time
from .gui import PassengerInfoForm
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from .browser import create_browser
from .ocr import CaptchaSolver
from .parser import BookingInfoParser
import json
import os

class THSRCBot:
    def __init__(self):
        self.driver = create_browser()
        self.ac = ActionChains(self.driver)
        self.ocr = CaptchaSolver()

    def human_like_pause(self, min_sec=0.8, max_sec=2.5):
        time.sleep(random.uniform(min_sec, max_sec))
    
    def get_user_input(self):
        form = PassengerInfoForm()
        if form.result:
            self.date = form.result["date"]
            self.time = form.result["time"]
            self.amount = form.result["amount"]
            self.id_number = form.result["id_number"]
            self.email = form.result["email"]
            self.start_station = form.result["start_station"]
            self.arrive_station = form.result["arrive_station"]
    def open_website(self):
        self.driver.get("https://www.thsrc.com.tw/")
        self.ac.move_to_element(self.driver.find_element(By.CSS_SELECTOR, 'button.swal2-confirm')).click().perform()
        self.ac.move_to_element(self.driver.find_element(By.CSS_SELECTOR, 'a#a_irs')).click().perform()

    def into_order_page(self):
        iframe = self.driver.find_element(By.CSS_SELECTOR, 'iframe#irsUrl')
        self.driver.get(iframe.get_attribute("src"))

    def fill_info(self):
        
        Select(self.driver.find_element(By.CSS_SELECTOR, "select#select_location01")).select_by_value(f"{self.start_station}")
        Select(self.driver.find_element(By.CSS_SELECTOR, "select#select_location02")).select_by_value(f"{self.arrive_station}")
        Select(self.driver.find_element(By.CSS_SELECTOR, "select#adultTicket")).select_by_value(f"{self.amount}F")
        self.driver.execute_script(f"document.getElementById('Departdate02').value = '{self.date}';")
        # self.human_like_pause()
        self.driver.execute_script(f"document.getElementById('toPortalTimeTable').value = '{self.time}';")
        # self.human_like_pause()
        

    def input_captcha(self):
        img = self.driver.find_element(By.CSS_SELECTOR, "img#BookingS1Form_homeCaptcha_passCode").screenshot_as_png
        code = self.ocr.solve(img)
        input_field = self.driver.find_element(By.CSS_SELECTOR, "input#securityCode")
        input_field.clear()
        input_field.send_keys(code)
        

    def submit_search(self):
        self.ac.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "input#SubmitButton")).click().perform()

    def confirm_time(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # self.human_like_pause()
        self.ac.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "input[name=SubmitButton]")).click().perform()

    def fill_passenger_info(self):
        self.driver.find_element(By.CSS_SELECTOR, "input#idNumber").send_keys(f"{self.id_number}")
        self.driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys(f"{self.email}")
        self.ac.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "input[name=agree]")).click().perform()
        # self.human_like_pause()
        self.ac.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "input#isSubmit")).click().perform()

    def print_booking_info(self):
        parser = BookingInfoParser(self.driver)
        info = parser.parse_info()
        print("===== 訂票成功 =====")
        for key, value in info.items():
            print(f"{key} : {value}")
        orderID = info.get("訂單編號|order number", "unknown")
        orderfolder = "orderfolder"
        if not os.path.exists(orderfolder):
            os.makedirs(orderfolder)
        filename = os.path.join(orderfolder, f"訂單編號-{orderID}.json")
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(info, f, ensure_ascii=False, indent=4)
    def run(self):
        self.get_user_input()
        self.open_website()
        self.into_order_page()
        self.fill_info()
        self.input_captcha()
        self.submit_search()
        self.confirm_time()
        self.fill_passenger_info()
        self.print_booking_info()
        

    def quit(self):
        self.driver.quit()
