import time
import yaml
import calendar
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.crawler.nike_com import Nike

if __name__ == '__main__':
    today = datetime.utcnow() + timedelta(hours=9)

    driver = webdriver.Chrome('../chromedriver.exe')
    nike = Nike()
    nike.get_raffle_info()