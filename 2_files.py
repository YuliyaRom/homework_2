"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

with open('referat.txt','r',encoding='utf-8') as f_in:
    content = f_in.read()
    print('Длина строки:',len(content))
    print('Количество слов:',len(content.split(' ')))
with open('referat2.txt','w',encoding='utf-8') as f_out:
     f_out.write(content.replace('.','!'))

