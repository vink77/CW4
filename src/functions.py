
class Vacancy:
    """
    Класс для работы с вакансиями
    """
    vacancies = []
    def __init__(self, vacancies):

        self.vacancies = vacancies

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

