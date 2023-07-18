import requests
from functions import *
from save_file import *




@classmethod
class Job():
    while True:
        print("\n1.найти вакансию")
        print("2.сохранить в файл")
        print("3.выйти")
        choiсe = input("Ваш выбор - ")

        if choiсe == '1':
            platforms = ["HeadHunter", "SuperJob"]
            search_query = input("Введите поисковый запрос: ")
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            output(search_query,top_n)

            #filter_words = input("\nВведите ключевые слова для фильтрации вакансий: ").split()
            #filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)

            #if not filtered_vacancies:
            #    print("Нет вакансий, соответствующих заданным критериям.")
            # return

            #     sorted_vacancies = sort_vacancies(filtered_vacancies)
            #     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
            #     print_vacancies(top_vacancies)

        if choiсe == "2":
            file_xls = input('Введите имя файла: ')
            save_xls()


        if choiсe == '3':
            break


# Функция для взаимодействия с пользователем


# Создание экземпляра класса для работы с API сайтов с вакансиями
# hh_api = HeadHunterAPI()
# superjob_api = SuperJobAPI()
#
## Получение вакансий с разных платформ
# hh_vacancies = hh_api.get_vacancies("Python")
# superjob_vacancies = superjob_api.get_vacancies("Python")

# Создание экземпляра класса для работы с вакансиями
#vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.",
 #                 "Требования: опыт работы от 3 лет...")

# Сохранение информации о вакансиях в файл
#json_saver = JSONSaver()
#json_saver.add_vacancy(vacancy)
#json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
#json_saver.delete_vacancy(vacancy)
