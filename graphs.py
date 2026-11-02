

from networkx import DiGraph, draw
from matplotlib.pyplot import show

digraph = DiGraph(directed=True)

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
            print('Данной вершины нет в списке')
            continue
        return v
        
        
while True:
    node = get_valid_node('Введите название вершины (для остановки напишите "."):', nodes) #Ожидаем ввод пользователя
    if node is None:
        break
    else:
        nodes.append(node) #Добавляем в глобальную переменную введённую вершину    
        digraph.add_node(node) #обновим логику, добавив вершину
        numbered_nodes =  [f"{i}.{n}" for i, n in enumerate(nodes, start=1)] #Далее создаём нумерованный список
        print('Вы ввели:', ', '.join(numbered_nodes))#выводим нумерованный список
print('ПОСТРОЕНИЕ ГРАФА')
while True:
    edge_start = input('Введите вершину, из которой будет построен путь (для остановки введите "."):').strip()
    if edge_start == '.': #Проверяем, не хочет ли он остановиться
        break
    elif edge_start.replace(" ", "").replace("-", "").isalpha(): 
        if edge_start in nodes:
            edge_finish = input('Введите вершину, в которую будет построен путь (для остановки введите "."):').strip()
            if edge_finish == '.':
                break
            elif edge_finish.replace(" ", "").replace("-", "").isalpha():
                if edge_finish in nodes:
                    digraph.add_edge(edge_start, edge_finish)
                else:
                    print('Такой вершины нет:', ', '.join(numbered_nodes))
            else:
                print('Похоже Вы использовали недопустимые символы')
        else:
            print('Такой вершины нет:', ', '.join(numbered_nodes))
    else:
        print('Похоже Вы использовали недопустимые символы')
    
#Отрисовка
draw(digraph, with_labels=True)
#Вывод для пользователя
result = ", ".join(nodes)
print(f"Вы ввели:{result}")

show()

