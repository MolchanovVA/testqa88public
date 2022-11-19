from selenium.webdriver.common.by import By
import pytest


def test_all_pets(login):
    pytest.driver.implicitly_wait(10)
    # Проверяем, что мы на главной странице
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # Получаем список картинок
    pytest.driver.implicitly_wait(10)
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    # Получаем список имен питомцев
    pytest.driver.implicitly_wait(10)
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    # Получаем описание питомцев
    pytest.driver.implicitly_wait(10)
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0