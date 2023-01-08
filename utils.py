import json
import pickle
from __queue import Queue


def read_file_hh(file):
    '''функция для чтения файла'''
    try:
        with open(file, 'r', encoding='utf-8') as f:
            files = json.load(f)
            result = []
            for i in files:
                if i.get('salary') is None:
                    result.append({'name': i.get('name'), 'href': i.get('alternate_url'),
                                   'salary': 0})
                elif i.get('salary').get('to') is not None:
                    result.append({'name': i.get('name'), 'href': i.get('alternate_url'),
                                   'salary': int(i.get('salary').get('to'))})
                elif i.get('salary').get('from') is not None:
                    result.append({'name': i.get('name'), 'href': i.get('alternate_url'),
                                   'salary': int(i.get('salary').get('from'))})
    except IOError:
        print("File df_sj.py could not be opened")
    return result


def read_file_js(file):
    '''функция для чтения файла'''
    try:
        with open(file, 'r', encoding='utf-8') as f:
            files = json.load(f)
            result = []
            for i in files:
                result.append({'name': i.get('profession'), 'href': i.get('link'),
                               'salary': int(i.get('payment_from'))})
    except IOError:
        print("File df_sj.py could not be opened")
    return result


def insert(data):
    '''функция для записи  результата в файл'''
    try:
        with open("res.pickle", "wb") as f:
            pickle.dump(data, f)

    except IOError:
        print("Error")
    return data


#ОЧЕРЕДЬ
def get_companies_list(vacancy_list):
    q = Queue()

    for vacancy in vacancy_list:
        q.enqueue(vacancy)

    company_list = set()

    for _ in range(len(vacancy_list)):
        vacancy = q.dequeue()
        name = vacancy.get('name')
        company_list.add(name)

    return company_list

