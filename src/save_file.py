import json
import pandas as pd

class Saver:
    """Класс для сохранения информации о вакансиях в JSON и XLS -файл."""

    def __init__(self, vacancies= [], filename='my_name'):
        self.filename_json = f"./{filename}.json"
        self.filename_xls = filename
        self.vacancies = vacancies

    def write_vacancies_json(self):
        """Метод для добавления вакансий в JSON формате в файл vacancies.json"""
        print(self.vacancies)
        with open(self.filename_json, 'w', encoding='utf-8') as file:
            json.dump(self.vacancies, file, ensure_ascii=False, indent=4)

    def delete_vacancy_json(self, id):
        with open(self.filename_json, "r", encoding="utf-8") as file:
            vacancies = json.load(file)
            new_vacancies = []
            for item in vacancies:
                if str(item['id']) != str(id):
                    new_vacancies.append(item)
        with open(self.filename_json, "w", encoding="utf-8") as file:
            json.dump(new_vacancies, file, ensure_ascii=False, indent=4)



    def write_vacancies_xls(self)-> None:
        '''метод для записи в файл-xls'''
        name = []
        town = []
        firm_name = []
        url = []
        description = []
        salary_from = []
        salary_to = []

        for item in self.vacancies:
                name.append(item['name'])
                town.append(item['town'])
                firm_name.append(item['firm_name'])
                url.append(item['url'])
                description.append(item['description'])
                salary_from.append(item['salary_from'])
                salary_to.append(item['salary_to'])

        df = pd.DataFrame(
        {
                            'Name': name,
                            'town': town,
                            'firm_name': firm_name,
                            'url': url,
                            'description': description,
                            'salary_from': salary_from,
                            'salary_to': salary_to
        })
        df.to_excel(f'./{self.filename_xls}.xlsx', index=False)
    def delete_vacancy_xls(self, id):
        """Метод для удаления вакансии из файла my_name.xls по id"""

        with open(self.filename_json, "r", encoding="utf-8") as file:
            vacancies = json.load(file)
            new_vacancies = []
            for item in vacancies:
                if str(item['id']) != str(id):
                    new_vacancies.append(item)
        with open(self.filename_json, "w", encoding="utf-8") as file:
            json.dump(new_vacancies, file, ensure_ascii=False, indent=4)