from pprint import pprint
from requests_html import HTMLSession

#Написать функцию которая на  вход принимает ключевое слово и название домена. 
#А на выходе возвращает позицию домена по этому слову.
#Обьявляем функцию
def position(keyword, domain):
    session = HTMLSession()
    resp = session.get(f'https://www.google.com/search?q={keyword}&num=10&hl=en')
    
    links = resp.html.xpath('//h3/a/@href')
    domains = [x.split('/')[2] for x in links if 'http' in x]
    #Ищем введеный ранее домен в списке domains
    for x in domains:
    #если мы нашли его и он точно соответствует
        if x == domain:
        #возвращаем его индекс(который и будет его позицией)
            return domains.index(x)
            #Если его нет в топ-10 Google(указано в переменной num=), то выдаем другой return
    return "Этого домена нет в топ-10 Google"
    #Зацикливаем действие через While True
while True:
    domain = input("Введите ваш домен или exit чтобы выйти: ")
    #Условие если человек ввел не домен, а exit , то он выходит.
    if 'exit' in domain:
        break
    keyword = input("Введите ваше ключевое слово: ")
    #выводим функцию(ключ и домен должны быть точно также обьявлены как в функции)
    print (position(keyword, domain))
