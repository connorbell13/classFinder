from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ratingBot:

    def __init__ (self):
       #ignoring ssl verifications through chrome webdriver options

        self.driver=webdriver.Chrome()
        teacher='Jason Yalim'
        self.driver.get('https://www.ratemyprofessors.com/search.jsp?queryoption=HEADER&queryBy=teacherName&schoolName=Arizona+State+University&schoolID=45&query=jennie+si')
        sleep(4)
        driver.get('/html/body/div[10]/button[1]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="searchr"]').send_keys(teacher)

mybot=ratingBot()