import time
from selenium import webdriver


def sendToStepik(task_link, answer):
  browser = webdriver.Chrome()
  browser.get('https://stepik.org/catalog?auth=login')
  time.sleep(3)
  login = browser.find_element_by_id('id_login_email')
  login.send_keys('g-unit_m@mail.ru')
  password = browser.find_element_by_id('id_login_password')
  password.send_keys('12345678qwerty')
  enter = browser.find_element_by_class_name('sign-form__btn')
  enter.click()
  time.sleep(3)
  browser.get(task_link)
  browser.implicitly_wait(4)
  time.sleep(2)
  browser.execute_script("window.scrollBy(0, 200);")
  time.sleep(4)
  browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/article[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/textarea[1]').send_keys(answer)
  time.sleep(5)
  browser.find_element_by_class_name('submit-submission').click()
  time.sleep(20)
