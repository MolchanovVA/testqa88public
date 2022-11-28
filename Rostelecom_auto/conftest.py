from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def open_login_page():
   pytest.driver = webdriver.Chrome('tests/chromedriver.exe')
   # Устанавливаем не явное ожидание
   pytest.driver.implicitly_wait(10)
   # Переходим на страницу авторизации
   pytest.driver.get('https://b2c.passport.rt.ru')
   # Разворачиваем браузер в полноэкранный режим
   pytest.driver.maximize_window()

   yield

   pytest.driver.quit()