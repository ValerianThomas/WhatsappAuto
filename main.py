
# from  whatsapp.driver_class import DriverClass
# driver = DriverClass()

# driver.go_to('https://web.whatsapp.com')
# time.sleep(3)
# get_qr = driver.get_element('._11ozL')
# qr_string = get_qr.get_attribute('data-ref')
# img = qrcode.make(qr_string)
# img.show()
# time.sleep(15)
# search_user = driver.get_element('.selectable-text')
# search_user.click()
# time.sleep(2)
# search_user.send_keys('Sara')
# search_user.send_keys(u'\ue007')
# time.sleep(2)
# footer = driver.get_element('footer')
# # using selenium selector as those are  selenium objects
# text_input = footer.find_element_by_class_name('selectable-text')
# text_input.send_keys('Big bisous')
# send_button =  footer.find_elements_by_css_selector("span[data-icon='send']")[0]

# # writting and sending the message

# send_button.click()
# driver.go_to('https://web.whatsapp.com')