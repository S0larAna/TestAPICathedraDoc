import allure
from requests import Response
from VersionController.api import DepartmentController
from VersionController.models import CreateDepartment
from schemas.schemas import valid_schema_department

BASE_URL = 'http://192.168.0.17:8080'


class TestDepartmentController:
    @allure.feature('Department')
    @allure.story('Получение кафедры по корректному id')
    def test_get_faculty_correct(self):
        response = DepartmentController(url=BASE_URL).get_department(id='1', schema=valid_schema_department)
        with allure.step("Проверка кода ответа == 200"):
            assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
        with allure.step("Провека респонса"):
            response = response.json()

    @allure.feature('Department')
    @allure.story('Получение кафедры по некорректному id')
    def test_get_faculty_incorrect(self):
        response = DepartmentController(url=BASE_URL).get_department(id='аааа', schema=valid_schema_department)
        with allure.step("Проверка кода ответа == 400"):
            assert response.status_code == 400, f"Неверный код ответа, получен {response.status_code}"
        with allure.step("Провека респонса"):
            response = response.json()
        return

    @allure.feature('Department')
    @allure.story('Получение кафедры по несуществующему id')
    def test_get_faculty_nonexistent(self):
        response = DepartmentController(url=BASE_URL).get_department(id='10000', schema="")
        with allure.step("Проверка кода ответа == 404"):
            assert response.status_code == 404, f"Неверный код ответа, получен {response.status_code}"
        return

    @allure.feature('Department')
    @allure.story('Создание кафедры с корректными данными')
    def test_get_faculty_nonexistent(self):
        payload = CreateDepartment.random()
        response = DepartmentController(url=BASE_URL).create_department(body=payload, schema=valid_schema_department, id="1")
        with allure.step("Проверка кода ответа == 201"):
            assert response.status_code == 201, f"Неверный код ответа, получен {response.status_code}"
        return