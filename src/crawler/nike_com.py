from datetime import datetime, timedelta
from selenium import webdriver


class Nike:
    def __init__(self):
        self.url = 'https://www.nike.com/kr/launch/?type=upcoming'

    def get_raffle_info(self):
        today = datetime.utcnow() + timedelta(hours=9)

        driver = webdriver.Chrome('../chromedriver.exe')
        driver.get(self.url)

        shoe_list = driver.find_elements_by_class_name('card-link.d-sm-b')
        month_element_list = driver.find_elements_by_class_name('headline-4')
        month_list = [month_element.text.replace('월', '') for month_element in month_element_list]

        date_element_list = driver.find_elements_by_class_name('headline-1')
        date_list = [date_element.text for date_element in date_element_list]

        raffle_date_list = [str(today.year) + '.' + month.zfill(2) + '.' + date.zfill(2) for month, date in
                            zip(month_list, date_list)]
