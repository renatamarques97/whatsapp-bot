# -*- coding: utf-8 -*-

from selenium import webdriver
import time

class Bot:
    def __init__(self):
        self.message = "O valor disponível na caixinha é x"
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

    def SendMessage(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        group = self.driver.find_element_by_xpath(f"//span[@title='Renata Marques']")
        time.sleep(3)
        group.click()
        chat_box = self.driver.find_element_by_class_name('_13mgZ')
        time.sleep(3)
        chat_box.click()
        chat_box.send_keys(self.message)
        send_button = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(3)
        send_button.click()
        time.sleep(3)

wbot = Bot()
wbot.SendMessage()

