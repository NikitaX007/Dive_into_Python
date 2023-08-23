# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.

MAX_WEIGTH = 5_000
things = ['Ложка', 'Чашка', 'Тарелка', 'Нож', 'Палатка', 'Футболка',
          'Спортивки', 'Боксеры', 'Зубные_принадлежности', 'Одеяло']
weights = [50, 250, 380, 150, 3_550, 300, 280, 180, 70, 1_670]

my_dict = {}
for num, thing in enumerate(things):
    my_dict[thing] = weights[num]

weight = 0
things_in = []
for key, value in my_dict.items():
    weight += value
    if weight <= MAX_WEIGTH:
        things_in.append(key)
    else:
        weight -= value
print(things_in)