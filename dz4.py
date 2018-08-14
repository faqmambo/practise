from pprint import pprint
from requests_html import HTMLSession

session = HTMLSession()

method = 'domain_keywords'

token = 'ваш токен'

se = 'g_ua'
key = input('Введите ключевое слово: ')
domain = ""
# Зацикли свою программу, так чтобы она работала снова.
while domain != "1":
    domain = input("Введите ваш домен или '1' чтобы выйти: ")
    #Сделать обработку ошибок try-except в момент, 
    # когда пользователь ввел неправильные данные (не домен) на вход твоего скрипта.
    try:
        if domain != "1":
            api_url = f'http://api.serpstat.com/v3/{method}/?query={domain}&token={token}&se={se}'
            response = session.get(api_url)
            data = response.json()
            # Используй для этого цикл for, который будет итерировать данные, приходящие из API.
            for x in data['result']['hits']:
                # Отобразить в консоль все ключевые слова для домена,
                keyword = x.get('keyword')
                # позиция ключа в выдаче
                position = x.get('position')
                # позиция ключа в выдаче
                frequency = x.get('region_queries_count')
            # Сделать для этих ключевых слов дополнительную фильтрацию, например 
            # поиск вхождения какого-то слова, применяя if-else.
                if key in keyword:
                    print (keyword, position, frequency)
        except:
            print("Это не домен\n")
            break
