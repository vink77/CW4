import json

import openpyxl
import pandas as pd

class JsonSaver:
    """Класс для сохранения информации о вакансиях в JSON и XLS -файл."""
    FILE_NAME = "my_name"
    def __init__(self,vacancies, filename = FILE_NAME):
        self.filename_json = f"./{filename}.json"
        self.filename_xls = filename
        self.vacancies = vacancies

    def write_vacancies_json(self):
        """Метод для добавления вакансий в JSON формате в файл vacancies.json"""

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

    def get_vacancies_json(self):
        """Метод для получения вакансий из файла my_name.json"""
        with open(self.filename_json, 'w+', encoding='utf-8') as file:
            return json.load(file)

    def get_vacancies_xls(self):
        """Метод для получения вакансий из файла my_name.json"""
        book = openpyxl.load_workbook(filename=self.filename_xls)
        sheet = book.active
        sheet.column_dimensions['A'].width=50

       # json_str1 = top_players.get()
       # json_str = json_str1.to_json(orient="records")
        print(type(top_players),top_players)
        for row in top_players:
            print(row)

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