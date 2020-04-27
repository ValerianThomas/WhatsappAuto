"""
A simple selenium test example written by python
"""
import os
import time
import atexit
import qrcode
import unittest

from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


web_driver = None

MAIN_URL = 'https://web.whatsapp.com'

def get_driver_cached():
        """Start web driver"""
        global web_driver
        if not web_driver:
            chrome_options = Options()
            chrome_options.add_argument('--no-sandbox')
            if not os.environ.get('NO_HEADLESS'):
                chrome_options.add_argument("--headless")
            chrome_options.add_argument('--disable-gpu')
            driver_url = ChromeDriverManager().install()
            web_driver = webdriver.Chrome(driver_url, options=chrome_options)
        return web_driver


def clear_driver():
    global web_driver
    if web_driver:
        web_driver.close()
        web_driver = None

atexit.register(clear_driver)

class DriverClass:
    
    def __init__(self):
        self.driver = get_driver_cached()
    
    def build_query_string(self, params):
        if not params:
            return ''
        query_string = '?'
        for param_name, param_value in params:
            query_string += f'{param_name}={param_value}&'
        return query_string
    
    def go_to(self, url, path='', params=None):
        url = f'{url}/{path}{self.build_query_string(params)}'
        self.driver.get(url)
    
    def get_element(self, css_selector, wait_time=10):
        return WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)),
            message='Cannot find element %s' % (css_selector)
        )

    def get_by_xpath(self, xpath, wait_time=2):
        return WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, xpath)),
            message='Cannot find element by xpath %s' % (xpath)
        )


class WhatsappMessaging (DriverClass):
    '''
    Class that holds the  whatsapp messaging  automation
    '''
    def __init__(self):
        self.super()

    def get_login_qr_code(self, qr_class_name: str = '._11ozL') -> Image:
        '''
        Method to open the driver on whatsapp web then to generate
        the QR code to signin as a user of choice.

        : qr_class_name: css class name of div containing the qr code
        : return: return a PIL Image with the qr code.
        '''
        self.driver.go_to(MAIN_URL)
        time.sleep(3)
        get_qr = driver.get_element(qr_class_name)
        qr_string = get_qr.get_attribute('data-ref')
        return qrcode.make(qr_string)
    
    def send_message_to_contact(self, contact: str, message: str) ->  None:
        '''
        Method to search a contact and send a message.
            
        : contact: name of the contact
        : message: message to send to the contact
        '''

        # Search and select the user
        search_user.send_keys(contact)
        search_user.send_keys(u'\ue007')
        time.sleep(2)

        # Select the text input in the footer
        footer = driver.get_element('footer')
        text_input = footer.find_element_by_class_name('selectable-text')

        # Write and send the  message
        text_input.send_keys(message)
        send_button =  footer.find_elements_by_css_selector("span[data-icon='send']")[0]
        send_button.click()

    def return_on_main(self) ->  None:
        '''
        Method to return to main menu after an instruction is finished.
        '''
        self.driver.go_to(MAIN_URL)

