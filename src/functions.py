import json


class Vacancy:
    """
    Класс для работы с вакансиями
    """
    vacancies = []
    def __init__(self, vacancies):

        self.vacancies = vacancies

    #   def __str__(self):
    #       """
    #       Возвращает строковое представление объекта класса vacancy.
    #       :return: str
    #       """
    #       return f"\nДолжность: {self.name}\nГород :{self.town}\nФирма: {self.firm_name}\nURL: {self.url}\nЗарплата от: {self.salary_from} до: {self.salary_to}\nОписание: {self.description}\n"
    #  def __repr__(self):
    #     return self.__str__()
    def output_vacancies(self):
        for item in self.vacancies:
            print(f"\nid: {item['id']}\n"
                f"Должность: {item['name']}\n"
                f"Город :{item['town']}\n"
                f"Фирма: {item['firm_name']}\n"
                f"URL: {item['url']}\n"
                f"Зарплата от: {item['salary_from']} до: {item['salary_to']}\n"
                f"Описание: {item['description']}")

    def sort_list(self,sort_pool):

        # сортировка списка "vacancies" по <от>

        print(self.vacancies)
        sorting = sorted(self.vacancies, key=lambda x: x[sort_pool], reverse=True)
        print("sorting", sorting)
        return sorting


# def get_vacancies(vacancy, params):
#        """Метод для получения вакансий в формате JSON"""
#
##    headers = {"X-Api-App-Id": API_SECRET_KEY}
##        for page in range(10):
##            time.sleep(1)
##            params = {
##                "keyword": str(input()),
##                "page": page,
##                "per_page": "100"
##            }
##        response = requests.get("https://api.superjob.ru/2.0/vacancies/",
##                                params=params,
##                                headers=headers)
##        if not response.status_code == HTTPStatus.OK:
##            return f'Ошибка! Статус-код: {response.status_code}'
##        return response.json()['objects']