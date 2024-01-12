# api requests
import allure
import requests
from jsonschema import validate

class VersionController:
    def __init__(self, url):
        self.url = url

    CRUD_VERSIONS = '/versions'
    FIND_VERSION_BY_DEPT ='/versions/findByDep'

    def get_version(self, id, schema:dict):
        response = requests.get(f"{self.url}{self.CRUD_VERSIONS}/{id}")
        validate(instance=response.json(), schema=schema)
        return response

    def update_version(self, body:dict, id, schema:dict):
        response = requests.put(f"{self.url}{self.CRUD_VERSIONS}/{id}", json=body)
        validate(instance=response.json(), schema=schema)
        return response

    def delete_version(self, id, schema:dict):
        response = requests.delete(f"{self.url}{self.CRUD_VERSIONS}/{id}")
        validate(instance=response.json(), schema=schema)
        return response

    def get_versions(self):
        return requests.get(f"{self.url}{self.CRUD_VERSIONS}")

    def create_version(self, body:dict, schema:dict):
        response = requests.post(f"{self.url}{self.CRUD_VERSIONS}", json=body)
        validate(instance=response.json(), schema=schema)
        return response

    def get_version_by_dept(self, deptId, schema:dict):
        response = requests.get(f"{self.url}{self.FIND_VERSION_BY_DEPT}/{deptId}")
        validate(instance=response.json(), schema=schema)
        return response

class DepartmentController:
    def __init__(self, url):
        self.url = url

    DEPARTMENTS = '/departments'
    FACULTIES = '/faculties'

    def get_department(self, id, schema:dict):
        response = requests.get(f"{self.url}{self.DEPARTMENTS}/{id}")
        if (schema!=""):
            validate(instance=response.json(), schema=schema)
        return response

    def update_department(self, body:dict, id, schema:dict):
        response = requests.put(f"{self.url}{self.DEPARTMENTS}/{id}", json=body)
        validate(instance=response.json(), schema=schema)
        return response

    def delete_department(self, id, schema:dict):
        response = requests.delete(f"{self.url}{self.DEPARTMENTS}/{id}")
        validate(instance=response.json(), schema=schema)
        return response

    def get_departments(self):
        return requests.get(f"{self.url}{self.DEPARTMENTS}")

    def create_department(self, body:dict, schema:dict, id):
        response = requests.post(f"{self.url}{self.FACULTIES}/{id}/{self.DEPARTMENTS}", json=body)
        validate(instance=response.json(), schema=schema)
        return response

class FacultyController:
    def __init__(self, url):
        self.url = url

    FACULTIES = '/faculties'

    def get_faculty(self, id, schema: dict):
        response = requests.get(f"{self.url}{self.FACULTIES}/{id}")
        validate(instance=response.json(), schema=schema)
        with allure.step(f'GET request to: {self.url}{self.FACULTIES}/{id}'):
            return response

    def update_faculty(self, body: dict, id, schema: dict):
        response = requests.put(f"{self.url}{self.FACULTIES}/{id}", json=body)
        validate(instance=response.json(), schema=schema)
        with allure.step(f'UPDATE request to: {self.url}{self.FACULTIES}/{id} \n body:{body}'):
            return response

    def delete_faculty(self, id, schema: dict):
        response = requests.delete(f"{self.url}{self.FACULTIES}/{id}")
        validate(instance=response.json(), schema=schema)
        with allure.step(f'DELETE request to: {self.url}{self.FACULTIES}/{id}'):
            return response

    def get_faculties(self):
        response = requests.get(f"{self.url}{self.FACULTIES}")
        with allure.step(f'GET request to: {self.url}{self.FACULTIES}'):
            return response

    def create_faculty(self, body: dict, schema: dict):
        response = requests.post(f"{self.url}{self.FACULTIES}", json=body)
        validate(instance=response.json(), schema=schema)
        with allure.step(f'POST request to: {self.url}{self.FACULTIES} \n body:{body}'):
            return response
