from src.api import *
from save_file import *
from load_file import *
from functions import *
import os


class Job():
    """Класс взаимодействия с пользователем"""
    hh_api = HHApi()
    sj_api = SJApi()
    file_name = 'my_name'
    while True:
        print(f"\n{' '*8}ОСНОВНОЕ МЕНЮ")
        print("1. найти и вывести список вакансий")
        print("2. МЕНЮ работыс  файлом json")
        print("3. МЕНЮ работы с файлом xlsx")
        print("4. МЕНЮ фильтров ")
        print("5. выйти")
        choiсe = input("Ваш выбор - ")
        if choiсe == '1':
            result_all = []

            platforms = [HHApi(), SJApi()]
            search_query = input("Введите должность для поиска: ")
            city = int(input("Выберите город поиска /1 - Москва, 2-Санкт-Петербург, 3- Кемерово, 4- Новосибирск/ : "))
            #top_n = int(input("Введите количество вакансий для вывода в топ N: "))

            for item in platforms:
                result = item.search(search_query, city)
                result_all.extend(result)
            vacancy = Vacancy(result_all)
            vacancy.output_vacancies()

        if choiсe == "2":
            while True:
                print(f"\n{' '*8} МЕНЮ работы с файлом {file_name}.json")
                print("1. сохранить вакансии в файл json")
                print("2. удалить вакансию из файла json")
                print("3. показать вакансии из файла json")
                print("4. задать имя файла json")
                print("5. удалить файл json")
                print("6. выход в основное меню")
                choiсe_file = input("     Ваш выбор: ")
                if choiсe_file == "1":
                    write = Saver(result_all, file_name)
                    write.write_vacancies_json()
                if choiсe_file == "2":
                    id = input("id для удаления ")
                    write.delete_vacancy_json(id)
                if choiсe_file == "3":
                    if os.path.isfile(f'./{file_name}.json'):
                        result_all = Loader(file_name)
                        Vacancy(result_all.get_vacancies_json()).output_vacancies()
                    else:
                        print("Такой файл не найден!")
                if choiсe_file == "4":
                    file_name = input("Введите имя файла без расширения :")
                if choiсe_file == "5":
                    if os.path.isfile(f'./{file_name}.json'):
                        os.remove(f'./{file_name}.json')
                        print(f"файл {file_name}.json удалён ")
                    else:
                        print("Такой файл не найден!")
                if choiсe_file == "6":
                    break
        if choiсe == "3":
            while True:
                print(f"\n{' ' * 8} МЕНЮ работы с файлами .xls")
                print("1. сохранить вакансии в файл xls")
                print("2. удалить вакансию из файла xls")
                print("3. показать вакансии из файла xls")
                print("4. задать имя файла xls")
                print("5. выход в основное меню")
                choiсe_file = input("     Ваш выбор: ")
                if choiсe_file == "1":
                    write = Saver(result_all,file_name)
                    write.write_vacancies_xls()
                if choiсe_file == "2":
                    pass
                if choiсe_file == "3":
                    pass
                if choiсe_file == "4":
                    pass

                if choiсe_file == "6":
                    break

        if choiсe == "4":
            print(f"\n{' ' * 8} МЕНЮ работы с фильтрами")
            print("1. Упорядочить список по зарплате < до >")
            print("2. Упорядочить список по зарплате < до >")
            print("3. Показать список вакансий с зарплатой 100 - 150 т.р")
            print("4. Показать список вакансий с зарплатой 0 - 100 т.р")
            print("5. выход в основное меню")
            choiсe_filter = input("     Ваш выбор: ")
            if choiсe_filter == "1" or choiсe_filter == "2":
                dict_choice = {"1": "salary_from",  "2": 'salary_to'}
                result_all = vacancy.sort_list(dict_choice[choiсe_filter])
                vacancy = Vacancy(result_all)
                vacancy.output_vacancies()
            if choiсe_filter == "3":
                pass
            if choiсe_filter == "4":
                pass
            if choiсe_filter == "5":
                break

                 # if not filtered_vacancies:
            #    print("Нет вакансий, соответствующих заданным критериям.")
            # return

        if choiсe == '5':
            break

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
