import allure
from VersionController.api import FacultyController
from VersionController.models import CreateFaculty
from schemas.schemas import valid_schema_faculty

BASE_URL = 'http://192.168.0.27:8080'

class TestFacultyController:
    @allure.feature('Faculty')
    @allure.story('Получение факультета по id')
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
        with allure.step("Тест пройден успешно"):
            return



