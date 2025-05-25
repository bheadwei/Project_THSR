import random, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from .browser import create_browser
from .ocr import CaptchaSolver
from .parser import BookingInfoParser

class THSRBot:
    def __init__(self):
        self.driver = create_browser()
        self.ac = ActionChains(self.driver)
        self.ocr = CaptchaSolver()

    def human_like_pause(self, min_sec=0.8, max_sec=2.5):
        time.sleep(random.uniform(min_sec, max_sec))

    def open_website(self):
        self.driver.get("https://www.thsrc.com.tw/")
        self.human_like_pause()
        self.ac.move_to_element(self.driver.find_element(By.CSS_SELECTOR, 'button.swal2-confirm')).click().perform()
        self.human_like_pause()
        self.ac.move_to_element(self.driver.find_element(By.CSS_SELECTOR, 'a#a_irs')).click().perform()

    def into_order_page(self):
        iframe = self.driver.find_element(By.CSS_SELECTOR, 'iframe#irsUrl')
        self.driver.get(iframe.get_attribute("src"))

    def fill_info(self):
        Select(self.driver.find_element(By.ID, "select_location01")).select_by_value("1")
        Select(self.driver.find_element(By.ID, "select_location02")).select_by_value("12")
        date_input = self.driver.find_element(By.ID, "Departdate02")
        date_input.send_keys(Keys.CONTROL, 'a', '2025/06/01')
        time_input = self.driver.find_element(By.ID, "toPortalTimeTable")
        time_input.send_keys(Keys.CONTROL, 'a', '18:00')

    def input_captcha(self):
        img = self.driver.find_element(By.ID, "BookingS1Form_homeCaptcha_passCode").screenshot_as_png
        code = self.ocr.solve(img)
        input_field = self.driver.find_element(By.ID, "securityCode")
        input_field.clear()
        input_field.send_keys(code)

    def submit_search(self):
        self.ac.move_to_element(self.driver.find_element(By.ID, "SubmitButton")).click().perform()

    def confirm_time(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.human_like_pause()
        self.ac.move_to_element(self.driver.find_element(By.NAME, "SubmitButton")).click().perform()

    def fill_passenger_info(self):
        self.driver.find_element(By.ID, "idNumber").send_keys("F129878220")
        self.ac.move_to_element(self.driver.find_element(By.NAME, "agree")).click().perform()
        self.ac.move_to_element(self.driver.find_element(By.ID, "isSubmit")).click().perform()

    def print_booking_info(self):
        parser = BookingInfoParser(self.driver)
        info = parser.parse_info()
        print("===== 訂票成功 =====")
        for key, val in info.items():
            print(f"{key} : {val}")

    def run(self):
        try:
            self.open_website()
            self.into_order_page()
            self.fill_info()
            self.input_captcha()
            self.submit_search()
            self.confirm_time()
            self.fill_passenger_info()
            self.print_booking_info()
        except Exception as e:
            raise RuntimeError(f"訂票失敗: {str(e)}")

    def quit(self):
        self.driver.quit()
