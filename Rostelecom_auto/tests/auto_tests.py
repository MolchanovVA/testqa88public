from selenium.webdriver.common.by import By
import pytest
from settings import valid_phone, email, valid_login, valid_ls, password,long_phone, short_phone, not_valid_password

def test_design(open_login_page):

    # Проверяем, что страница разделена на 2 части
    assert pytest.driver.find_element(By.ID, 'page-left')
    assert pytest.driver.find_element(By.ID, 'page-right')
    # Проверяем, что кнопки Номер, Почта, Логин, Лицевой счет, поле Логина, поле Пароль находятся в левой части
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//div[@id="t-btn-tab-phone"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//div[@id="t-btn-tab-mail"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//div[@id="t-btn-tab-login"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//div[@id="t-btn-tab-ls"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//input[@id="username"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//input[@id="password"]')
    # Проверяем, что Логотип и вспомогательная информация находятся в правой части
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-right"]//div[@class="what-is-container__logo-container"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-right"]//div[@class="what-is"]')

def test_design_phone(open_login_page):

    # Нажимаем кнопку Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()

    assert pytest.driver.find_element(By.XPATH, '//span[text()="Мобильный телефон"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Пароль"]')

def test_design_email(open_login_page):

    # Нажимаем кнопку Почта
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что в поле Логина теперь Электронная почта
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Электронная почта"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Пароль"]')

def test_design_login(open_login_page):

    # Нажимаем кнопку Логин
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что в поле Логина теперь "Логин"
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Логин"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Пароль"]')

def test_design_ls(open_login_page):

    # Нажимаем кнопку Лицевой счет
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что в поле Логина теперь "Лицевой счет"
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Лицевой счёт"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Пароль"]')

def test_change_tab_phone(open_login_page):

    # Нажимаем кнопку Почта
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(10)
    # Вводим номер телефона
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_phone)
    # Нажимаем на поле Пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').click()
    # Проверяем, что таб переключился на логин по номеру телефона
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Мобильный телефон"]')

def test_change_tab_email(open_login_page):

    # Нажимаем кнопку Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.implicitly_wait(10)
    # Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(email)
    # Нажимаем на поле Пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').click()
    # Проверяем, что таб переключился на логин по mail
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Электронная почта"]')

def test_change_tab_email(open_login_page):

    # Нажимаем кнопку Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.implicitly_wait(10)
    # Вводим Логин
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_login)
    # Нажимаем на поле Пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').click()
    # Проверяем, что таб переключился на авторизацию по логину
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Логин"]')

def test_change_tab_ls(open_login_page):

    # Нажимаем кнопку Почта
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(10)
    # Вводим валидный лицевой счет
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_ls)
    # Нажимаем на поле Пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').click()
    # Проверяем, что таб переключился на логин по Лицевому счету
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Лицевой счёт"]')

def test_login_email(open_login_page):

    # Нажимаем кнопку Почта
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(10)
    # Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(email)
    # Вводим password
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(password)
    # Нажимаем на кнопку Войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что мы зашли в личный кабинет
    assert pytest.driver.find_element(By.XPATH, '//h3[text()="Учетные данные"]')
    # Выходим из учетной записи
    pytest.driver.find_element(By.ID, 'logout-btn').click()

def test_login_phone(open_login_page):

    # Нажимаем кнопку Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.implicitly_wait(10)
    # Вводим номер телефона
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_phone)
    # Вводим password
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(password)
    # Нажимаем на кнопку Войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что мы зашли в личный кабинет
    assert pytest.driver.find_element(By.XPATH, '//h3[text()="Учетные данные"]')
    # Выходим из учетной записи
    pytest.driver.find_element(By.ID, 'logout-btn').click()

def test_login_login(open_login_page):

    # Нажимаем кнопку Логин
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.implicitly_wait(10)
    # Вводим Логин
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_login)
    # Вводим password
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(password)
    # Нажимаем на кнопку Войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что мы зашли в личный кабинет
    assert pytest.driver.find_element(By.XPATH, '//h3[text()="Учетные данные"]')
    # Выходим из учетной записи
    pytest.driver.find_element(By.ID, 'logout-btn').click()

def test_login_ls(open_login_page):

    # Нажимаем кнопку Лицевой счет
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest.driver.implicitly_wait(10)
    # Вводим Логин
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_ls)
    # Вводим password
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(password)
    # Нажимаем на кнопку Войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что мы зашли в личный кабинет
    assert pytest.driver.find_element(By.XPATH, '//h3[text()="Учетные данные"]')
    # Выходим из учетной записи
    pytest.driver.find_element(By.ID, 'logout-btn').click()

def test_btn_forgot_password(open_login_page):

    # Нажимаем кнопку Забыл пароль
    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что переадресация на страницу восстановления пароля
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Восстановление пароля"]')

def test_btn_terms_of_use(open_login_page):

    # Нажимаем кнопку Пользовательское соглашение
    pytest.driver.find_element(By.XPATH, '//a[text()="пользовательского соглашения"]').click()
    # Переключаемся на новую вкладку
    window_after = pytest.driver.window_handles[1]
    pytest.driver.switch_to.window(window_after)
    # Проверяем, что переадресация на страницу Публичная оферта
    assert pytest.driver.find_element(By.XPATH, '//title[text()="User agreement"]')

def test_empty_phone(open_login_page):

    # Нажимаем кнопку Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    # Нажимаем кнопку Войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что появилась подсказка об ошибке ввода
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Введите номер телефона"]')

def test_empty_email(open_login_page):

    # Нажимаем кнопку Почта
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    # Нажимаем кнопку Войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что появилась подсказка об ошибке ввода
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Введите адрес, указанный при регистрации"]')

def test_empty_login(open_login_page):

    # Нажимаем кнопку Логин
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    # Нажимаем кнопку Войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что появилась подсказка об ошибке ввода
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Введите логин, указанный при регистрации"]')

def test_empty_ls(open_login_page):

    # Нажимаем кнопку Логин
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    # Нажимаем кнопку Войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что появилась подсказка об ошибке ввода
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Введите номер вашего лицевого счета"]')

def test_long_phone(open_login_page):

    # Нажимаем кнопку Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    # Вводим номер телефона
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(long_phone)
    # Проверяем, что в поле только разрешенное количество символов
    assert pytest.driver.find_element(By.XPATH, '//input[@value="79817375520"]')

def test_short_phone(open_login_page):

    # Нажимаем кнопку Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    # Вводим номер телефона
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(short_phone)
    # Нажимаем на поле Пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').click()
    # Проверяем, что появилась подсказка Неверный формат телефона
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Неверный формат телефона"]')

def test_kapcha(open_login_page):

    count = 0
    while count < 5:

        # Нажимаем кнопку Почта
        pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
        # Вводим email
        pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(email)
        # Вводим password
        pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(not_valid_password)
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        # Ищем капчу и если ее нету, то еще раз вводим неверные данные
        try:
            if pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]'):
                break
        except:
            count += 1

    # Проверяем, что появилась Капча
    assert pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')