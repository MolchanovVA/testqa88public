from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import numpy


def test_my_pets(login):
    # Нажимаем на кнопку "Мои питомцы"
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()

    # Собираем информацию о питомцах
    # Получаем фото питомцев
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//th/img'))
    )
    images = pytest.driver.find_elements(By.XPATH, '//th/img')
    # Получаем обеъекты с именами
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//tr/td[1]'))
    )
    names = pytest.driver.find_elements(By.XPATH, '//tr/td[1]')
    # Получаем список с породой
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//tr/td[2]'))
    )
    character = pytest.driver.find_elements(By.XPATH, '//tr/td[2]')
    # Получаем список с возрастом
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//tr/td[3]'))
    )
    age = pytest.driver.find_elements(By.XPATH, '//tr/td[3]')

    # Получаем блок в котором есть общее количество питомцев
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]'))
    )
    pets_full = pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]')
    # Разбиваем список по частям
    numbers = pets_full.text.split('\n')
    # Получаем строку, в которой есть количество питомцев
    num = numbers[1]
    # Получаем количество питомцев, обрезая строку
    num_2 = int(num[10:])

    # Создаем список имен
    list_of_names = []
    # Заполняем список имен
    for i in range(len(names)):
        list_of_names.append(names[i].text)
    # Создаем массив с именами чтобы убрать повторы
    array_names = numpy.array(list_of_names)

    # Создаем список с именами, породой и возрастом
    list_of_pets = []
    for i in range(len(names)):
        list_of_pets.append(f'{names[i].text}, {character[i].text}, {age[i].text}')
    # Создаем массив с именами, породой и возрастом
    array_pets = numpy.array(list_of_pets)

    # Проверяем, что общее количество питомцев на странице совпадает с количеством карточек питомцев
    assert num_2 == len(names)
    # Проверяем что хотя бы у половины питомцев есть фото.
    assert (f"{len(images)} >= {num_2 / 2} ")
    # Проверяем У всех питомцев разные имена
    assert len(list_of_names) == len(array_names)
    # Проверяем У всех питомцев есть имя, возраст и порода
    for i in range(len(names)):
        assert names[i].text != '' and character[i].text != '' and age[i].text != ''
    # Сравниваем, что нет питомцев, у которых одинаковые имя, порода и возраст
    assert len(list_of_pets) == len(array_pets)
