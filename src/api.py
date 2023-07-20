from abc import ABC,abstractmethod
from src.functions import Vacancy
import requests, os

class API(ABC):
    def __init__(self, url, num_vacancies = 30):
        self.url = url
        self.num_vacancies = num_vacancies

    @abstractmethod
    def search(self, request_job):
        pass


class HHApi(API):
    result =[]
    def __init__(self, url = 'https://api.hh.ru/vacancies' ):
        self.url = url
        super().__init__(url)

    def  search(self, request_job):
        params = {
            'text': request_job,
            'area': 1,
            'pages': 0,
            'per_page': self.num_vacancies}
        response = requests.get(self.url, params).json()

        #if response.status_code == 200:
        result = []
        for item in response['items']:
            salary = item.get('salary', {})
            result.append(
                Vacancy(
                    name=item['name'],
                    url=item['url'],
                    description=item['snippet']['requirement'],
                    salary_to=salary.get('to') if salary is not None else None,
                    salary_from=salary.get('from') if salary is not None else None
                )
            )
        print(result)
        return result
        #else:
         #   print('Ошибка при запросе данных о вакансиях')
          #  return None


class SJApi(API):
    def __init__(self, url = 'https://api.superjob.ru/2.0/vacancies' ):
        self.url = url
        super().__init__(url)

    def  search(self, request_job):
        api_key: str = os.getenv('Sjob_API_KEY')
        headers = {'X-Api-App-Id': api_key}


        params = {
            "keywords": [1, request_job],
            "count": self.num_vacancies,
        }


        response = requests.get(self.url, headers=headers, params=params).json()
        print('\n', response)
        result = []
        for item in response['objects']:
            result.append(
                Vacancy(
                    name=item['profession'],
                    url=item['client']['link'],
                    description=item['vacancyRichText'],
                    salary_to=item['payment_to'],
                    salary_from=item['payment_from'],
                )
            )
        print(result)
        return result
