from src.api import *
from save_file import *
from functions import *


class Job():
    hh_api = HHApi()
    sj_api = SJApi()
    while True:
        print("\n1. найти и показать список вакансий")
        print("2. сохранить в файл json")
        print("3. сохранить в файл xlsx")
        print("4. Упорядочить список по зарплате < от >")
        print("5. Упорядочить список по зарплате < до >")
        print("6. выйти")
        choiсe = input("Ваш выбор - ")

        if choiсe == '1':
            platforms = [HHApi(), SJApi()]
            search_query = input("Введите должность для поиска: ")
            search_query = "энергетик"
            city = int(input("Выберите город поиска /1 - Москва, 2- Санкт-Питербург, 3- Кемерово/ : "))
            # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            top_n = 20
            result_all = []
            for i in platforms:
                vac = i
                result = vac.search(search_query, city)
                result_all.append(result)
            vacancy = Vacancy()
            vacancy.output_vacancies(result_all)

        if choiсe == "2":
            write = JsonSaver()
            write.write_vacancies_json(result_all)

        if choiсe == "3":
            write = JsonSaver()
            write.write_vacancies_xls(result_all)

            # filter_words = input("\nВведите ключевые слова для фильтрации вакансий: ").split()
            # filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)

            # if not filtered_vacancies:
            #    print("Нет вакансий, соответствующих заданным критериям.")
            # return

            #     sorted_vacancies = sort_vacancies(filtered_vacancies)
            #     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
            #     print_vacancies(top_vacancies)

        #     if choiсe == "2":
        #         file_xls = input('Введите имя файла: ')
        #         save_xls()

        if choiсe == '6':
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
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.",
#                 "Требования: опыт работы от 3 лет...")

# Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
# json_saver.delete_vacancy(vacancy)
