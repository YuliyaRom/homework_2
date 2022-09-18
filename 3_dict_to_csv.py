"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv
people = [{'name': 'Vasya', 'age': 24, 'job': 'journalist'},
              {'name': 'Masha', 'age': 35, 'job': 'writer'},
              {'name': 'Den', 'age': 27, 'job': 'doctor'},
              {'name': 'Asya', 'age': 33, 'job': 'teacher'}]
with open('people.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, people[0].keys(), delimiter=';')
    writer.writeheader()
    for person in people:
        writer.writerow(person)