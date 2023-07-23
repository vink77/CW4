import json


class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self):

    #    self.num = num
    #    self.name = vacancies['name']
    #    self.town = vacancies['town']
    #    self.firm_name = vacancies['firm_name']
    #    self.url = vacancies['url']
    #    self.salary_to = vacancies['salary_to']
    #    self.salary_from = vacancies['salary_from']
    #    self.description = vacancies['escription']

    #   def __str__(self):
    #       """
    #       Возвращает строковое представление объекта класса vacancy.
    #       :return: str
    #       """
    #       return f"\nДолжность: {self.name}\nГород :{self.town}\nФирма: {self.firm_name}\nURL: {self.url}\nЗарплата от: {self.salary_from} до: {self.salary_to}\nОписание: {self.description}\n"
    #  def __repr__(self):
    #     return self.__str__()
    def output_vacancies (self, vacancies):
        for item in vacancies:
            print(item)
        # print( f"\nДолжность: {item['name']}\nГород :{self.town}\nФирма: {self.firm_name}\nURL: {self.url}\nЗарплата от: {self.salary_from} до: {self.salary_to}\nОписание: {self.description}\n")

#  def sort_list(execut_list):
#       # сортировка списка "EXECUTTED" по дате
#       sorting = sorted(execut_list, key = lambda x: x["date"],reverse = True)
#       return sorting


#
#
# def get_doc(vacancy, per_page=10, page=0):
#    params = {
#        'text': vacancy,
#        'area': 1,
#        'pages': page,
#        'per_page': per_page}
#    response = requests.get('https://api.hh.ru/vacancies', params).json()
#    return response.get("items", [])
#
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