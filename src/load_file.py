import json
class Loader:
    """Класс для сохранения информации о вакансиях в JSON и XLS -файл."""
    FILE_NAME = "my_name"
    def __init__(self, filename = FILE_NAME):
        self.filename_json = f"./{filename}.json"
        self.filename_xls = filename

    def get_vacancies_json(self):
        """Метод для получения вакансий из файла my_name.json"""
        with open(self.filename_json, 'r', encoding='utf-8') as file:
            text = json.load(file)
            print(text)
            return text
       #     return json.load(file)

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