
class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, vacancies):

        self.vacancies = vacancies

    def output_vacancies(self):
        for item in self.vacancies:
            s = f"Описание: {item['description']}"
            s1 = s.split(' ')
            s3=[]
            num1 =150
            l=num1
            for i in s1:
                s3.append(i)
                if len(''.join(s3))>l:
                    l+=num1
                    s3.append('\n')
            print(f"\nid: {item['id']}\n"
                f"Должность: {item['name']}\n"
                f"Город :{item['town']}\n"
                f"Фирма: {item['firm_name']}\n"
                f"URL: {item['url']}\n"
                f"Зарплата от: {item['salary_from']} до: {item['salary_to']}")
            print(' '.join(s3))

    def sort_list(self,sort_pool):

        # сортировка списка "vacancies" по <от>

        print(self.vacancies)
        sorting = sorted(self.vacancies, key=lambda x: x[sort_pool], reverse=True)
        print("sorting", sorting)
        return sorting

