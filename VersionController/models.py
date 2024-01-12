from faker import Faker
import random
from datetime import datetime

faker = Faker("ru_RU")
fakerEng = Faker()

faculty_correct_payload = {
    "name": "Факультет компьютерных технологий и прикладной математики",
    "shortName": "ФКТиПМ"
}

faculty_words = ["факультет", "биологии", "философии", "астрономии", "математики"]

department_words = ["Философии", "Астрономии", "Психологии", "Математики", "Компьютерных технологий"]


class CreateVersion:
    @staticmethod
    def random():
        date = str(datetime.now().strftime("%Y-%m-%dT%H:%M:%S.907Z"))
        versionNumber = str(random.randint(0, 10000))
        academicYear = str(random.randint(2018, 2023))
        umu = bool(random.getrandbits(1))
        return {"date": date, "versionNumber": versionNumber, "academicYear": academicYear, "umu": umu}

class CreateDepartment:
    @staticmethod
    def random():
        word_count = random.randint(1, 4)
        number = str(random.randint(1, 10000))
        name = faker.sentence(nb_words=word_count, ext_word_list=department_words)
        shortName = faker.word()
        academicYear = str(random.randint(2018, 2023))
        umu = bool(random.getrandbits(1))
        return {"number": number, "name": name, "shortName": shortName}


class CreateFaculty:
    @staticmethod
    def random():
        word_count = random.randint(1, 5)
        name = faker.sentence(nb_words=word_count, ext_word_list=faculty_words)
        shortName = faker.word()
        return {"name": name, "shortName": shortName}

    @staticmethod
    def random_eng():
        word_count = random.randint(1, 5)
        name = fakerEng.sentence(nb_words=word_count, ext_word_list=faculty_words)
        shortName = fakerEng.word()
        return {"name": name, "shortName": shortName}

    @staticmethod
    def random_incorrect_special_chars():
        char_count = random.randint(1, 20)
        name = ''.join([random.choice('!@#$%^&*()_') for n in range(char_count)])
        shortName = ''.join([random.choice('!@#$%^&*()_') for n in range(char_count)])
        return {"name": name, "shortName": shortName}

    @staticmethod
    def empty_shortName():
        word_count = random.randint(1, 5)
        name = faker.sentence(nb_words=word_count, ext_word_list=faculty_words)
        return {"name": name, "shortName": ""}

    @staticmethod
    def empty_name():
        shortName = faker.word()
        return {"name": "", "shortName": shortName}

    @staticmethod
    def random_incorrect_numbers():
        name = random.randint(0, 100000)
        shortName = faker.word()
        return {"name": name, "shortName": shortName}

    @staticmethod
    def random_long_name():
        word_count = random.randint(10000, 100000000000)
        name = faker.sentence(nb_words=word_count, ext_word_list=faculty_words)
        shortName = faker.word()
        return {"name": name, "shortName": shortName}

    @staticmethod
    def random_unicode():
        char_count = random.randint(1, 20)
        name = ''.join([random.choice('ÆĆĆĆÆĕŵĠŒ') for n in range(char_count)])
        shortName = ''.join([random.choice('ÆĆĆĆÆĕŵĠŒ') for n in range(char_count)])
        return {"name": name, "shortName": shortName}