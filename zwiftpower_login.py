from bs4 import BeautifulSoup
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class ZwiftPowerReader:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())


        self.driver.get('https://zwiftpower.com')

        btn = self.driver.find_elements_by_id('login')[0].find_elements_by_class_name('btn')[0]
        btn.click()

        username_input = self.driver.find_elements_by_id('username')[0]
        username_input.send_keys(os.environ['ZWIFTPOWER_USERNAME'])
        password_input = self.driver.find_elements_by_id('password')[0]
        password_input.send_keys(os.environ['ZWIFTPOWER_PASSWORD'])
        btn = self.driver.find_elements_by_id('submit-button')[0]
        btn.click()


    def read_profile(self, zwift_id):
        self.driver.get('https://zwiftpower.com/profile.php?z={zwift_id}'.format(zwift_id=zwift_id))
        return BeautifulSoup(self.driver.page_source, 'html.parser')


if __name__ == '__main__':
    zp = ZwiftPowerReader()
    zwift_id = 11526
    profile = zp.read_profile(zwift_id)
    print(profile)
