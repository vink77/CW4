from abc import ABC,abstractmethod
import requests

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


    def search(self, request_job, city):
        town_hh = [1, 2, 1229]
        params = {
            'text': request_job,
            'area': town_hh[city-1],
            'pages': 0,
            'per_page': self.num_vacancies}
        response = requests.get(self.url, params).json()

        #if response.status_code == 200:
        result = []
        salary_from = salary_to =0
        for item in response['items']:
            salary = item.get('salary', {})
            if salary == None:
                salary_from = 0
                salary_to = 0
            elif item['salary']['from'] == None:
                salary_from = 0
            elif item['salary']['to'] == None:
                salary_to = 0
            else:
                salary_from = salary.get('from')
                salary_to = salary.get('to')
            result.append({
                    "id": item["id"],
                    "name": item['name'],
                    "town": item['area']['name'],
                    "firm_name": item['employer']['name'],
                    "url": item['url'],
                    "description": item['snippet']['requirement'][0:20],
                    "salary_to": salary_to,
                    "salary_from": salary_from}
            )
        return result

class SJApi(API):
    def __init__(self, url = 'https://api.superjob.ru/2.0/vacancies' ):
        self.url = url
        super().__init__(url)

    def search(self, request_job, city):
       # api_key: str = os.getenv('Sjob_API_KEY')
        dict_town_sj = {1: "москва", 2: "Санкт-Петербург", 3: "кемерово"}
        #town_sj = dict_town_sj[city]

        headers = {
            'X-Api-App-Id':
                'v3.r.137478329.0484df93bd0dbe1d4ec473961f0e68359d16d3f6.0ab6ee7c38c6375a5deb84c35464cc67b7b4c44b'
        }

        params = {
            "keywords": [request_job],
            "count": self.num_vacancies,
            "town": dict_town_sj[city]
        }


        response = requests.get(self.url, headers=headers, params=params).json()
        result = []
        for item in response['objects']:
            result.append({
                    "id": item['id'],
                    "name": item['profession'],
                    "town": item['town']['title'],
                    "firm_name": item['firm_name'],
                    "url":item['link'],
                    "description":item['vacancyRichText'][0:20],
                    "salary_to":item['payment_to'],
                    "salary_from":item['payment_from']}
            )
        return result
