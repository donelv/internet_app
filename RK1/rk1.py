# используется для сортировки
from operator import itemgetter

#компьютер и дисплейный класс

class Computer:
  """Компьютер"""
  def __init__(self, id, cpu, graphic_card, disp_id):
    self.id = id
    self.cpu = cpu
    self.graphic_card = graphic_card
    self.disp_id = disp_id

class DispayClass:
  """Дисплейный класс"""
  def __init__(self, id, room_number, square):
    self.id = id
    self.room_number = room_number
    self.square = square

class CompDisp:
  """
    'Компьтеры класса' для реализации 
    связи многие-ко-многим
  """
  def __init__(self, disp_id, comp_id):
        self.disp_id = disp_id
        self.comp_id = comp_id

#Компьютеры
comps = [
    Computer(1, 'Intel Core i7', 'GeForce GT710', 1),
    Computer(2, 'Intel Core i5', 'GeForce RTX3080', 1),
    Computer(3, 'Intel Core i4', 'GeForce GTX1660', 1),
    Computer(4, 'AMD Ryzen 5', 'Radeon RX590', 1),
    Computer(5, 'AMD Ryzen 7', 'Radeon RX6900', 2),
    Computer(6, 'AMD Ryzen 9', 'Radeon RX6900', 2),
    Computer(7, 'Intel Core i5', 'GeForce GTX1050', 2),
    Computer(8, 'AMD Ryzen 7', 'Radeon RX6600', 3),
    Computer(9, 'Intel Core i7', 'GeForce GTX1080',3),
    Computer(10, 'Intel Core i5', 'GeForce RTX1080', 3),
]
# Дисплейные классы
disp = [
    DispayClass(1, 'ClRoom-501', 150),
    DispayClass(2, 'ClRoom-306', 140),
    DispayClass(3, 'ClRoom-404', 170),
]

comps_disp = [
    CompDisp(1,1),
    CompDisp(1,2),
    CompDisp(1,3),
    CompDisp(1,4),

    CompDisp(2,5),
    CompDisp(2,6),
    CompDisp(2,7),

    CompDisp(3,8),
    CompDisp(3,9),
    CompDisp(3,10),
]
 
def main():
    """Основная функция"""
    # Соединение данных один-ко-многим 
    one_to_many = [
      (c.id, c.cpu, c.graphic_card, d.room_number) 
        for c in comps 
        for d in disp 
        if c.disp_id==d.id
    ]
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.room_number, cd.disp_id, cd.comp_id) 
        for d in disp 
        for cd in comps_disp 
        if d.id==cd.disp_id]
    
    many_to_many = [(c.cpu, c.graphic_card, d_room) 
        for d_room, disp_id, comp_id in many_to_many_temp
        for c in comps if c.id==comp_id]

    print('Задание Б1')
    res1 = sorted(one_to_many, key=itemgetter(1))  #Сортировка по процессорам
    print(res1)

    print('\nЗадание Б2') #Список классов с количеством компьютеров в каждом классе
    res2 = []
    # Перебираем все дисплейные классы
    for d in disp:
        # Список компьютеров класса
        d_comps = list(filter(lambda i: i[3]==d.room_number, one_to_many))
        # Если класс не пустой        
        if len(d_comps) > 0:
            res2.append((d.room_number, len(d_comps)))
        res2 = sorted(res2, key=lambda item: item[1], reverse=True)
    print(res2)

    print('\nЗадание Б3') #Список различных процессоры Intel, установленных в классах
    res3 = {}
    # Перебираем все компьютеры
    for c in comps:
        if 'Intel' in c.cpu:
            # Список классов с Intel'ом
            d_comps = list(filter(lambda i: i[0]==c.cpu, many_to_many))
            # Только номер классов
            d_comps_cpus = [x for _,_,x in d_comps]
            # Добавляем результат в словарь
            # ключ - cpu, значение - номера классов
            res3[c.cpu] = d_comps_cpus
    print(res3)
 
if __name__ == '__main__':
    main()
