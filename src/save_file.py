import json
import pandas as pd


class JsonSaver:
    """Класс для сохранения информации о вакансиях в JSON и XLS -файл."""
    FILE_NAME = "my_name"
    def __init__(self, filename = FILE_NAME):
        self.filename_json = f"{filename}.json"
        self.filename_xls = filename

    def write_vacancies_json(self, vacancies):
        """Метод для добавления вакансий в JSON формате в файл vacancies.json"""

        with open(self.filename_json, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def delete_vacancy_json(self, id):
        with open(self.filename_json, "r", encoding="utf-8") as file:
            vacancies = json.load(file)
            new_vacancies = []
            for item in vacancies:
                if str(item['id']) != str(id):
                    new_vacancies.append(item)
        with open(self.filename_json, "w", encoding="utf-8") as file:
            json.dump(new_vacancies, file, ensure_ascii=False, indent=4)

    def get_vacancies(self):
        """Метод для получения вакансий из файла my_name.json"""
        with open(self.filename, 'w+', encoding='utf-8') as file:
            return json.load(file)

    def write_vacancies_xls(self, vacancies)-> None:
        """Метод для добавления вакансий в .xls формате в файл my_name.xls"""
        name = []
        town = []
        firm_name = []
        url = []
        description = []
        salary_from = []
        salary_to = []

        for item in vacancies:
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

