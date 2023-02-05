from datetime import datetime
import json
#from numbers import numbers_form


def getting_operations():
    list_operations = []
    """
    Функция получает вложенный словарь операций
    """
    with open('operation.json', 'rt',encoding="UTF-8") as file:
        data = json.load(file)
        for i in range(len(data)):
            if "state" not in data[i]:
                continue
            else:
                list_operations.append(data[i])
    return list_operations


def correct_format(text):
    """
     Функция подгоняет даты в нужный формат для фильтрации

    """
    c = []
    d = []

    for i in text:
        if i['state'] == 'EXECUTED':


          k = i['date'].split('T')
          c.append(k[0])
    c.remove('')


    for i in c:

        k = datetime.fromisoformat(i)
        d.append(k)
    return d

class Event:

    def __init__(self, title="", date=datetime.now()):
        self.title = title
        self.date = date

    def __repr__(self):
        return f"Event({self.date}, {self.title}"


events = [

]

c = []
def get_last5(data):

   """ функция возвращает последние 5 дат из списка операция в виде строки год-месяц-день"""




   for i in data:
       events.append(Event('Событие',i))
   events.sort(key=lambda event: event.date)
   for i in events[-5:len(events)]:
       k = i.date.strftime('%Y,%m,%d')
       d = k.split(',')
       a = '-'.join(d)
       c.append(a)
   return c

#get_last5(correct_format(getting_operations()))
def searching(text):
   # k = get_last5(correct_format(getting_operations()))

    """Функция соспоставляет список дат с списком всех операций и формирует отдельный список содержащий 5 последних операций"""


    full_operations = []
    for i in getting_operations():
        b = i['date'].split('T')
        if b[0] in text:
            full_operations.append(i)
    return full_operations
#searching(get_last5(correct_format(getting_operations())))


def form():
    """
    Функция передаёт список дат операций в правильном формате(через точку)
    """
    dates = []
    operations = searching(get_last5(correct_format(getting_operations())))

    for i in operations:
              #print(i)
      c = i['date'].split('T')
      v = c[0].split('-')
      b = '.'.join(v)
      dates.append(b)
    return dates
def name():
    """
    Функция передаёт номер счёта с каторого сделан перевод
    """
    description = []
    operations = searching(get_last5(correct_format(getting_operations())))
    for i in operations:
        description.append(i['description'])
    return description




def string():
    from_ = []
    data = searching(get_last5(correct_format(getting_operations())))
    p = []
    star = '*'
    for i in data:
        if 'from' in i:
            c = i['from'].split(' ')
            if len(c) == 3:
                p.append(c[2])
            else:
                p.append(c[1])

    for i in p:

        if len(i) == 16:

            from_.append(f'{i[:4]} {i[4:6]}{star * 2} {star * 4} {i[-4:]}')
        elif len(i) == 20:

            from_.append(f'{i[:4]} {i[4:6]}{star * 2} {star * 4} {star * 4} {i[-4:]}')
    return  from_

def to():
    """
    Функция передаёт номер счёта на который был перевод
    """
    to_ = []

    operations = searching(get_last5(correct_format(getting_operations())))
    for i in operations:
        k = i['to'].split(' ')
        to_.append(f'{k[0]} **{k[1][-4:]}')
    return to_[0]

def summ():


























