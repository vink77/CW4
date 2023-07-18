import requests


def get_doc(vacancy,per_page=10, page=0):
    params = {
        'text': vacancy,
        'area': 1,
        'pages': page,
        'per_page': per_page}
    response = requests.get('https://api.hh.ru/vacancies', params).json()
    return response.get("items", [])

def output(search_query, top_n):
    i = 1
    hh = get_doc(search_query, top_n)
    for item in hh:
        print('\n', i, ' ', item['name'], end='')
        a = 70 - len(item['name']) - len(str(i))

        if item['salary'] != None:
            print(f"{'.' * a} зарплата от {item['salary']['from']}", end='')
            if item['salary']['to'] != None:
                print(f"  до {item['salary']['to']}", end='')

        else:
            print(f"{' ' * a} размер зарплаты отсутствует", end='')
        i += 1