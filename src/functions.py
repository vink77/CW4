import requests


class Vacancy:
    """
    Класс для работы с вакансиями, реализован для получения нужных объектов
    """

    def __init__(self, name: str, url: str, salary_to: int, salary_from: int, description: str):
        self.name = name
        self.url = url
        self.salary_to = salary_to
        self.salary_from = salary_from
        self.description = description

    def __str__(self):
        """
        Возвращает строковое представление объекта класса vacancy.
        :return: str
        """
        return f"\nVacancy: {self.name}\nURL: {self.url}\nSalaryTo: {self.salary_to}\nSalaryFrom: {self.salary_from}\nDescription: {self.description}\n"

    def __repr__(self):
        return self.__str__()


























#
#
#def get_doc(vacancy, per_page=10, page=0):
#    params = {
#        'text': vacancy,
#        'area': 1,
#        'pages': page,
#        'per_page': per_page}
#    response = requests.get('https://api.hh.ru/vacancies', params).json()
#    return response.get("items", [])
#
#def get_vacancies(vacancy, params):
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
#
#
#
#
#
#def output(search_query_hh, top_n):
#    i = 1
#    hh = get_doc(search_query_hh, top_n)
#    for item in hh:
#        print('\n', i, ' ', item['name'], end='')
#        a = 70 - len(item['name']) - len(str(i))
#
#        if item['salary'] != None:
#            print(f"{'.' * a} зарплата от {item['salary']['from']}", end='')
#            if item['salary']['to'] != None:
#                print(f"  до {item['salary']['to']}", end='')
#
#        else:
#            print(f"{' ' * a} размер зарплаты отсутствует", end='')
#        i += 1
#
#
#    for item in sj_vacancies:
#        if filtered_words.lower() in item['profession'].lower():
#            if item['payment_from'] == 0:
#                sj_data.append(f'{item["profession"]}\nСсылка: {item["link"]}\n'
#                               f'Заработная плата: до {item["payment_to"]}\n'
#                               f'Требуемый опыт: {item["experience"]["title"]}')
#            elif item['payment_to'] == 0:
#                sj_data.append(f'{item["profession"]}\nСсылка: {item["link"]}\n'
#                               f'Заработная плата: от {item["payment_from"]}\n'
#                               f'Требуемый опыт: {item["experience"]["title"]}')
#            else:
#                sj_data.append(f'{item["profession"]}\nСсылка: {item["link"]}\n'
#                               f'Заработная плата: от {item["payment_from"]}, до {item["payment_to"]}\n'
#                               f'Требуемый опыт: {item["experience"]["title"]}')
#
#
#output("python", 30)