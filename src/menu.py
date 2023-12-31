from src.api import HHApi, SJApi
from save_file import Saver
from load_file import Loader
from functions import Vacancy
import os


class Job():
    """Класс взаимодействия с пользователем"""
    SALARY_FROM = 100000  # Константы зарплат для фильтров
    SALARY_TO = 150000  # Константы зарплат для фильтров
    hh_api = HHApi()
    sj_api = SJApi()
    file_name = 'my_name'
    result_all = []
    while True:
        print(f"\n{' ' * 8}ОСНОВНОЕ МЕНЮ\n\
1. найти и вывести список вакансий с ресурсов HH.ru и SuperJob.ru\n\
2. МЕНЮ работыс  файлом json\n\
3. МЕНЮ работы с файлом xlsx\n\
4. МЕНЮ фильтров \n\
5. выйти")
        choiсe = input("Ваш выбор - ")
        if choiсe == '1':
            result_all = []
            platforms = [HHApi(), SJApi()]
            search_query = input("Введите должность для поиска: ")
            city = 0
            while city not in ["1", "2", "3", "4"]:
                city = str(
                    input("Выберите город поиска /1 - Москва, 2-Санкт-Петербург, 3- Кемерово, 4- Новосибирск/ : "))
            city = int(city)
            for item in platforms:
                result = item.search(search_query, city)
                result_all.extend(result)
            vacancy = Vacancy(result_all)
            vacancy.output_vacancies()
        if choiсe == "2":
            while True:
                print(f"\n{' ' * 8} МЕНЮ работы с файлом {file_name}.json\n\
1. сохранить вакансии в файл json\n\
2. удалить вакансию из файла json по id\n\
3. показать вакансии из файла json\n\
4. задать имя файла json\n\
5. удалить файл json\n\
6. выход в основное меню")
                choiсe_file = input("     Ваш выбор: ")
                if choiсe_file == "1":
                    write = Saver(result_all, file_name)
                    write.write_vacancies_json()
                    if os.path.isfile(f'./{file_name}.json'):
                        print(f"файл {file_name}.json сохранен!")
                if choiсe_file == "2":  # удалить вакансию из файла json
                    id = input("id для удаления ")
                    write.delete_vacancy_json(id)
                if choiсe_file == "3":  # показать вакансии из файла json
                    if os.path.isfile(f'./{file_name}.json'):
                        result_all = Loader(file_name)
                        Vacancy(result_all.get_vacancies_json()).output_vacancies()
                    else:
                        print("Такой файл не найден!")
                if choiсe_file == "4":  # задать имя файла json
                    file_name = input("Введите имя файла без расширения :")
                if choiсe_file == "5":  # удалить файл json
                    if os.path.isfile(f'./{file_name}.json'):
                        os.remove(f'./{file_name}.json')
                        print(f"файл {file_name}.json удалён ")
                    else:
                        print("Такой файл не найден!")
                if choiсe_file == "6":
                    break
        if choiсe == "3":
            while True:
                print(f"\n{' ' * 8} МЕНЮ работы с файлом {file_name}.xlsx\n\
1. сохранить вакансии в файл xls\n\
2. удалить вакансию из файла xls по id\n\
3. показать вакансии из файла xls\n\
4. задать имя файла xls\n\
5. удалить файл xls\n\
6. выход в основное меню")
                choiсe_file = input("     Ваш выбор: ")
                if choiсe_file == "1":
                    write = Saver(result_all, file_name)
                    write.write_vacancies_xls()
                    if os.path.isfile(f'./{file_name}.xlsx'):
                        print(f"файл {file_name}.xlsx сохранен!")
                if choiсe_file == "2":
                    if os.path.isfile(f'./{file_name}.xlsx'):
                        id = input("id для удаления ")
                        result = Loader(file_name)
                        Saver(result.get_vacancies_xls()).delete_vacancy_xls(id)
                if choiсe_file == "3":  # показать вакансии из файла xlsx
                    if os.path.isfile(f'./{file_name}.xlsx'):
                        result_all = Loader(file_name)
                        Vacancy(result_all.get_vacancies_xls()).output_vacancies()
                if choiсe_file == "4":
                    file_name = input("Введите имя файла без расширения :")
                if choiсe_file == "5":  # удалить файл xlsx
                    if os.path.isfile(f'./{file_name}.xlsx'):
                        os.remove(f'./{file_name}.xlsx')
                        print(f"файл {file_name}.xlsx удалён ")
                if choiсe_file == "6":
                    break
        if choiсe == "4":
            if result_all != []:
                print(f"\n{' ' * 8} МЕНЮ работы с фильтрами\n\
1. Упорядочить список по зарплате < ОТ >\n\
2. Упорядочить список по зарплате < ДО >\n\
3. Показать список вакансий с зарплатой {SALARY_FROM} - {SALARY_TO} руб.\n\
4. Показать список вакансий с зарплатой 0 - {SALARY_FROM} руб.\n\
5. Удалить из списка вакансии без указания зарплаты\n\
6. выход в основное меню")
                choiсe_filter = input("     Ваш выбор: ")
                if choiсe_filter == "1" or choiсe_filter == "2":
                    dict_choice = {"1": "salary_from", "2": 'salary_to'}
                    vacancy = Vacancy(result_all)
                    result_all = vacancy.sort_list(dict_choice[choiсe_filter])
                    Vacancy(result_all).output_vacancies()
                if choiсe_filter == "3":
                    vacancy = Vacancy(result_all)
                    result_all = vacancy.filter_salary(SALARY_FROM, SALARY_TO)
                    Vacancy(result_all).output_vacancies()
                if choiсe_filter == "4":
                    vacancy = Vacancy(result_all)
                    result_all = vacancy.filter_salary(0, SALARY_FROM)
                    Vacancy(result_all).output_vacancies()
                if choiсe_filter == "5":
                    vacancy = Vacancy(result_all)
                    result_all = vacancy.filter_salary_zero()
                    Vacancy(result_all).output_vacancies()
                if choiсe_filter == "6":
                    pass
            else:
                print('Необходимо сначала получить список вакансий!!')
        if choiсe == '5':
            break
