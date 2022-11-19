from selenium import webdriver
from settings import email, password
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(autouse=True)
def login():
   pytest.driver = webdriver.Chrome('chromedriver.exe')
   # Устанавливаем не явное ожидание
   pytest.driver.implicitly_wait(10)
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   # Разворачиваем браузер в полноэкранный режим
   pytest.driver.maximize_window()
   # Вводим email
   pytest.driver.find_element(By.ID, "email").send_keys(email)
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys(password)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   yield

   pytest.driver.quit()