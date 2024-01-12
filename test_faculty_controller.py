import allure
from requests import Response
from VersionController.api import FacultyController
from VersionController.models import CreateFaculty
from schemas.schemas import valid_schema_faculty

BASE_URL = 'http://192.168.0.27:8080'


class TestFacultyController:
    @allure.feature('Faculty')
    @allure.story('Получение факультета по корректному id')
    def test_get_faculty_correct(self):
        response = FacultyController(url=BASE_URL).get_faculty(id='1', schema=valid_schema_faculty)
        with allure.step("Проверка кода ответа == 200"):
            assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
        with allure.step("Провека респонса"):
            response = response.json()

    @allure.feature('Faculty')
    @allure.story('Создание факультета с корректными данными')
    def test_post_faculty_correct(self):
        payload = CreateFaculty.random()
        response = FacultyController(url=BASE_URL).create_faculty(body=payload, schema=valid_schema_faculty)
        with allure.step("Код ответа:"):
            assert response.status_code == 201, f"Неверный код ответа, получен {response.status_code}"
        response = response.json()
        assert response["name"] == payload["name"]
        assert response["shortName"] == payload["shortName"]
        id = response["id"]
        get_response = FacultyController(url=BASE_URL).get_faculty(id=id, schema=valid_schema_faculty)
        with allure.step("Код ответа:"):
            assert get_response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
        get_response = get_response.json()
        assert get_response["name"] == payload["name"]
        assert get_response["shortName"] == payload["shortName"]
        with allure.step("Тест пройден успешно"):
            return

    @allure.feature('Faculty')
    @allure.story('Создание факультета с латиницей в названии')
    def test_post_faculty_incorrect_name_latin(self):
        payload = CreateFaculty.random_eng()
        response = FacultyController(url=BASE_URL).create_faculty(body=payload, schema=valid_schema_faculty)
        with allure.step("Код ответа:"):
            assert response.status_code >= 400 and response.status_code <= 499, f"Неверный код ответа, получен {response.status_code}"
        response = response.json()
        assert response["name"] == payload["name"]
        assert response["shortName"] == payload["shortName"]
        id = response["id"]

        get_response = FacultyController(url=BASE_URL).get_faculty(id=id, schema=valid_schema_faculty)
        with allure.step("Код ответа:"):
            assert get_response.status_code == 404, f"Неверный код ответа, получен {response.status_code}"
        with allure.step("Тест пройден успешно"):
            return

    @allure.feature('Faculty')
    @allure.story('Создание факультета с цифрами в названии')
    def test_post_faculty_incorrect_name_latin(self):
        payload = CreateFaculty.random_incorrect_numbers()
        response = FacultyController(url=BASE_URL).create_faculty(body=payload, schema=valid_schema_faculty)
        with allure.step("Код ответа: "):
            assert response.status_code >= 400 and response.status_code <= 499, f"Неверный код ответа, получен {response.status_code}"
        response = response.json()
        assert response["name"] == payload["name"]
        assert response["shortName"] == payload["shortName"]
        id = response["id"]

        get_response = FacultyController(url=BASE_URL).get_faculty(id=id, schema=valid_schema_faculty)
        with allure.step("Код ответа:"):
            assert get_response.status_code == 404, f"Неверный код ответа, получен {response.status_code}"
        with allure.step("Тест пройден успешно"):
            return

    @allure.feature('Faculty')
    @allure.story('Создание факультета со специальным символами в названии факультета')
    def test_post_faculty_incorrect_name_special_chars(self):
        payload = CreateFaculty.random_incorrect_special_chars()
        response = FacultyController(url=BASE_URL).create_faculty(body=payload, schema=valid_schema_faculty)
        with allure.step("Код ответа: "):
            assert response.status_code >= 400 and response.status_code <= 499, f"Неверный код ответа, получен {response.status_code}"
        response = response.json()
        assert response["name"] == payload["name"]
        assert response["shortName"] == payload["shortName"]
        id = response["id"]

        get_responce = FacultyController(url=BASE_URL).get_faculty(id=id, schema=valid_schema_faculty)
        with allure.step("Код ответа:"):
            assert get_responce.status_code == 404, f"Неверный код ответа, получен {response.status_code}"
        with allure.step("Тест пройден успешно"):
            return

    @allure.feature('Faculty')
    @allure.story('Создание факультета с разными кодировками в названии факультета')
    def test_post_faculty_unicode_chars(self):
        payload = CreateFaculty.random_unicode()
        response = FacultyController(url=BASE_URL).create_faculty(body=payload, schema=valid_schema_faculty)
        with allure.step("Код ответа: "):
            assert response.status_code >= 400 and response.status_code <= 499, f"Неверный код ответа, получен {response.status_code}"
        response = response.json()
        assert response["name"] == payload["name"]
        assert response["shortName"] == payload["shortName"]
        id = response["id"]

        get_responce = FacultyController(url=BASE_URL).get_faculty(id=id, schema=valid_schema_faculty)
        with allure.step("Код ответа:"):
            assert get_responce.status_code == 404, f"Неверный код ответа, получен {response.status_code}"
        with allure.step("Тест пройден успешно"):
            return

    # -- для сокращенного названия --

    @allure.feature('Faculty')
    @allure.story('Создание факультета с пустым сокращенным названием')
    def test_post_faculty_incorrect_empty_shortname(self):
        payload = CreateFaculty.empty_shortName()
        response = FacultyController(url=BASE_URL).create_faculty(body=payload, schema=valid_schema_faculty)
        with allure.step("Код ответа: "):
            assert response.status_code >= 400 and response.status_code <= 499, f"Неверный код ответа, получен {response.status_code}"
        response = response.json()
        assert response["name"] == payload["name"]
        assert response["shortName"] == payload["shortName"]
        id = response["id"]

        get_responce = FacultyController(url=BASE_URL).get_faculty(id=id, schema=valid_schema_faculty)
        with allure.step("Код ответа:"):
            assert get_responce.status_code == 404, f"Неверный код ответа, получен {response.status_code}"
        with allure.step("Тест пройден успешно"):
            return

    @allure.feature('Faculty')
    @allure.story('Создание факультета с пустым названием факультета')
    def test_post_faculty_incorrect_empty_name(self):
        payload = CreateFaculty.empty_name()
        response = FacultyController(url=BASE_URL).create_faculty(body=payload, schema=valid_schema_faculty)
        with allure.step("Код ответа: "):
            assert response.status_code >= 400 and response.status_code <= 499, f"Неверный код ответа, получен {response.status_code}"
        response = response.json()
        assert response["name"] == payload["name"]
        assert response["shortName"] == payload["shortName"]
        id = response["id"]

        get_responce = FacultyController(url=BASE_URL).get_faculty(id=id, schema=valid_schema_faculty)
        with allure.step("Код ответа:"):
            assert get_responce.status_code == 404, f"Неверный код ответа, получен {response.status_code}"
        with allure.step("Тест пройден успешно"):
            return

    # -- удалить факультет --

    @allure.feature('Faculty')
    @allure.story('Удаление факультета со с корректными данными')
    def test_delete_faculty_with_correct_data(self):
        # Создание факультета с корректными данными
        payload = CreateFaculty.random()
        response = FacultyController(url=BASE_URL).create_faculty(body=payload, schema=valid_schema_faculty)
        with allure.step("Проверка кода ответа при создании факультета: "):
            assert response.status_code == 201, f"Неверный код ответа, получен {response.status_code}"
        response = response.json()
        assert response["name"] == payload["name"]
        assert response["shortName"] == payload["shortName"]
        id = response["id"]

        get_response = FacultyController(url=BASE_URL).delete_faculty(id=id, schema=valid_schema_faculty)
        with allure.step("Код ответа:"):
            assert get_response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
        with allure.step("Проверка удаления вызовом get-запроса: "):
            get_response = FacultyController(url=BASE_URL).get_faculty(id=id, schema=valid_schema_faculty)
            assert get_response.status_code == 404, f"Неверный код ответа, получен {get_response.status_code}"
        with allure.step("Тест пройден успешно"):
            return

    @allure.feature('Faculty')
    @allure.story('Удаление факультета с корректными данными')
    def test_delete_faculty_with_correct_data(self):
        # Создание факультета с корректными данными
        payload = CreateFaculty.random()
        response = FacultyController(url=BASE_URL).create_faculty(body=payload, schema=valid_schema_faculty)
        with allure.step("Проверка кода ответа при создании факультета: "):
            assert response.status_code == 201, f"Неверный код ответа, получен {response.status_code}"
        response = response.json()
        assert response["name"] == payload["name"]
        assert response["shortName"] == payload["shortName"]
        id = response["id"]

        get_response = FacultyController(url=BASE_URL).delete_faculty(id=id, schema=valid_schema_faculty)
        with allure.step("Код ответа:"):
            assert get_response.status_code == 200, f"Неверный код ответа, получен {get_response.status_code}"
        with allure.step("Проверка удаления вызовом get-запроса: "):
            get_response = FacultyController(url=BASE_URL).get_faculty(id=id, schema=valid_schema_faculty)
            assert get_response.status_code == 404, f"Неверный код ответа, получен {get_response.status_code}"
        with allure.step("Тест пройден успешно"):
            return


    @allure.feature('Faculty')
    @allure.story('Удаление несуществующего факультета')
    def test_delete_unknown_faculty_data(self):
        # Создание факультета с корректными данными
        payload = CreateFaculty.random()
        response = FacultyController(url=BASE_URL).create_faculty(body=payload, schema=valid_schema_faculty)
        with allure.step("Проверка кода ответа при создании факультета: "):
            assert response.status_code == 201, f"Неверный код ответа, получен {response.status_code}"
        response = response.json()
        assert response["name"] == payload["name"]
        assert response["shortName"] == payload["shortName"]
        id = response["id"] + 1

        get_response = FacultyController(url=BASE_URL).delete_faculty(id=id, schema=valid_schema_faculty)
        with allure.step("Код ответа:"):
            assert get_response.status_code >= 400 and get_response.status_code <= 499, f"Неверный код ответа, получен {get_response.status_code}"
        with allure.step("Тест пройден успешно"):
            return


    # -- update факультет --

    @allure.feature('Faculty')
    @allure.story('Изменение факультета с корректными данными')
    def test_put_faculty_correct(self):
        # Создание факультета с корректными данными
        payload = CreateFaculty.random()
        response = FacultyController(url=BASE_URL).create_faculty(body=payload, schema=valid_schema_faculty)
        with allure.step("Проверка кода ответа при создании факультета для изменения: "):
            assert response.status_code == 201, f"Неверный код ответа, получен {response.status_code}"
        response = response.json()
        assert response["name"] == payload["name"]
        assert response["shortName"] == payload["shortName"]
        id = response["id"]

        payload_new = CreateFaculty.random()

        get_responce = FacultyController(url=BASE_URL).update_faculty(id=id, body=payload_new, schema=valid_schema_faculty)
        with allure.step("Код ответа:"):
            assert get_responce.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
        with allure.step("Проверка изменения вызовом get-запроса: "):
            get_response = FacultyController(url=BASE_URL).get_faculty(id=id, schema=valid_schema_faculty)
            response = response.json()
            assert get_response["name"] == payload_new["name"]
            assert get_response["shortName"] == payload_new["shortName"]
            id = response["id"]

            assert get_response.status_code == 200, f"Неверный код ответа, получен {get_response.status_code}"
        with allure.step("Тест пройден успешно"):
            return


    @allure.feature('Faculty')
    @allure.story('Изменение факультета с некорректными данными')
    def test_put_faculty_correct(self):
        # Создание факультета с некорректными данными
        payload = CreateFaculty.random()
        response = FacultyController(url=BASE_URL).create_faculty(body=payload, schema=valid_schema_faculty)
        with allure.step("Проверка кода ответа при создании факультета для изменения: "):
            assert response.status_code == 201, f"Неверный код ответа, получен {response.status_code}"
        response = response.json()
        assert response["name"] == payload["name"]
        assert response["shortName"] == payload["shortName"]
        id = response["id"]

        payload_new = CreateFaculty.random_incorrect_special_chars()

        get_response = FacultyController(url=BASE_URL).update_faculty(id=id, body=payload_new, schema=valid_schema_faculty)
        with allure.step("Код при обновлении на неправильные данные ответа:"):
            assert get_response.status_code == 201, f"Неверный код ответа, получен {get_response.status_code}"

        with allure.step("Тест пройден успешно"):
            return


    # -- get факультета --


    # условимся со всеми чмошниками. что id==1 есть
    @allure.feature('Faculty')
    @allure.story('Получение существующего факультета с корректными данными')
    def test_get_faculty_correct(self):
        get_response = FacultyController(url=BASE_URL).get_faculty(id='1', schema=valid_schema_faculty)
        with allure.step("Код ответа:"):
            assert get_response.status_code == 200, f"Неверный код ответа, получен {get_response.status_code}"
        with allure.step("Тест пройден успешно"):
            return


    # условимся со всеми чмошниками. что id==99999 нет
    @allure.feature('Faculty')
    @allure.story('Получение несуществующего факультета с корректными данными')
    def test_get_faculty_nonexistent(self):
        get_response = FacultyController(url=BASE_URL).get_faculty(id='99999', schema=valid_schema_faculty)
        with allure.step("Код ответа:"):
            assert get_response.status_code == 404, f"Неверный код ответа, получен {get_response.status_code}"
        with allure.step("Тест пройден успешно"):
            return


    @allure.feature('Faculty')
    @allure.story('Получение факультета с некорректными данными')
    def test_get_faculty_incorrect(self):
        get_response = FacultyController(url=BASE_URL).get_faculty(id='АРЛХАРБАРЕ', schema=valid_schema_faculty)
        with allure.step("Код ответа:"):
            assert get_response.status_code == 400, f"Неверный код ответа, получен {get_response.status_code}"
        with allure.step("Тест пройден успешно"):
            return




