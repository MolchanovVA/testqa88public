from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_without_data(email="", password=''):
    """ Проверяем что запрос api ключа возвращает статус 403, когда мы отправляем пустые поля"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403


def test_get_api_key_without_password(email=valid_email, password=''):
    """ Проверяем что запрос api ключа возвращает статус 403, когда мы оставляем поле пароль пустым"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403


def test_get_api_key_without_email(email="", password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 403, когда мы отправляем поле Email пустым"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403


def test_get_api_key_with_invalid_password(email=valid_email, password="999"):
    """ Проверяем что запрос api ключа возвращает статус 403, когда мы отправляем не верный пароль"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403


def test_add_new_pet_simple_without_any_data(name='', animal_type='',
                                             age=''):
    """Проверяем что можно добавить питомца без данных"""
    """На данный момент это баг. Возвращается статус 200, должна возвращаться ошибка,
     поля name, animal_type, age - обязательные"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 200


def test_add_new_pet_simple_without_name(name='', animal_type='двортерьер',
                                         age='4'):
    """Проверяем что можно добавить питомца без имени"""
    """На данный момент это баг. Возвращается статус 200, должна возвращаться ошибка,
     поля name, animal_type, age - обязательные"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 200


def test_add_new_pet_simple_without_animal_type(name='Барбоскин', animal_type='',
                                                age='4'):
    """Проверяем что можно добавить питомца без типа животного"""
    """На данный момент это баг. Возвращается статус 200,
     должна возвращаться ошибка, поля name, animal_type, age - обязательные"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 200


def test_add_new_pet_simple_without_age(name='Барбоскин', animal_type='двортерьер',
                                        age=''):
    """Проверяем что можно добавить питомца без возраста"""
    """На данный момент это баг. Возвращается статус 200,
     должна возвращаться ошибка, поля name, animal_type, age - обязательные"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 200


def test_successful_update_self_pet_info_without_data(name='', animal_type='', age=''):
    """Проверяем возможность обновления информации о питомце с пустыми полями"""
    """На данный момент это баг. Возвращается статус 200,
     должна возвращаться ошибка, поля name, animal_type, age - обязательные"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status != 200
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_successful_update_self_pet_info_without_animal_type(name='Дракоша', animal_type='', age='665'):
    """Проверяем возможность обновления информации о питомце с пустым полем animal_type"""
    """На данный момент это баг. Возвращается статус 200,
     должна возвращаться ошибка, поля name, animal_type, age - обязательные"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status != 200
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_successful_update_self_pet_info_without_age(name='Дракоша', animal_type='покемон', age=''):
    """Проверяем возможность обновления информации о питомце с пустым полем age"""
    """На данный момент это баг. Возвращается статус 200, должна возвращаться ошибка, 
    поля name, animal_type, age - обязательные"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status != 200
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_successful_update_self_pet_info_without_name(name='', animal_type='покемон', age='3'):
    """Проверяем возможность обновления информации о питомце с пустым полем name"""
    """На данный момент это баг. Возвращается статус 200, должна возвращаться ошибка, 
    поля name, animal_type, age - обязательные"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status != 200
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_add_new_photo_wrong_format(pet_photo='images/бульбазавр.png'):
    """Проверяем что можно добавить питомцу в неверном формате"""
    """Статуса ошибки в документации не описано, приходит статус 500"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key. Запрашиваем список питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/бульбазавр.png")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Получаем ID Добавляем фото
    _, pet_id = _, my_pets['pets'][0]['id']
    status, result = pf.add_photo(auth_key, pet_id, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 200
