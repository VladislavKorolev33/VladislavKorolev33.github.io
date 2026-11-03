

from networkx import DiGraph, draw
from matplotlib.pyplot import show

digraph = DiGraph()

#Список вершин для пользователя
print('ВВОД ВЕРШИН')
nodes = []
numbered_nodes =  [] #Далее создаём нумерованный список, который будем обновлять

def get_valid_node(promt:str, nodes : list) -> str | None:
    while True:
        v = input(promt).strip()

        if v == '.':
            return None
        
        clear_v = v.replace(' ', '').replace('-', '')
        if not clear_v.isalpha():
            print("Похоже вы использовали недопустимые символы")
            continue

        if v not in nodes:
            print('Данной вершины нет в списке:', ', '.join(numbered_nodes))
            continue
        return v
        
        
while True:
    node = input('Введите название вершины (для остановки напишите "."): ') #Ожидаем ввод пользователя
    if node == '.':
        break
    else:
        if node.replace(" ", "").replace("-", "").isalpha():
            if node not in nodes: #если вершина (новая) и содержит (только буквы и дефисы)/(буквы и пробелы) то подходит
                nodes.append(node) #Добавляем в глобальную переменную введённую вершину    
                digraph.add_node(node) #обновим логику, добавив вершину
                numbered_nodes =  [f"{i}.{n}" for i, n in enumerate(nodes, start=1)] #создаём нумерованный список
                print('Вы ввели:', ', '.join(numbered_nodes))#выводим нумерованный список
            else:
                print(f'Используйте другое название для вершины. Ваши вершины: {numbered_nodes}')
        else:
            print('Вы использовали недопустимые символы')
print('ПОСТРОЕНИЕ ГРАФА')
while True:
    edge_start = get_valid_node('Введите вершину, из которой будет построен путь (для остановки напишите "."): ', nodes)
    if edge_start is None: #Проверяем, не хочет ли он остановиться
        break 
    else:
        edge_finish = get_valid_node('Введи вершину, в которую будет построен путь (для остановки напишите "."): ', nodes)
        if edge_finish is None:
                break
        else:
            digraph.add_edge(edge_start, edge_finish)
    
#Отрисовка
draw(digraph, with_labels=True)
#Вывод для пользователя
result = ", ".join(nodes)
print(f"Вы ввели:{result}")

show()

