import re

from matplotlib.pyplot import show, title
from networkx import DiGraph, draw, spring_layout



class GraphBuilder:
    #Константы
    PROMPT_NODE = "Введите название вершины (для остановки напишите '.''): "
    PROMPT_EDGE_FROM = "Введите вершину, из которой будет построен путь (для остановки напишите '.'):"
    PROMPT_EDGE_TO = "Введите вершину, в которую будет построен путь (для остановки напишите '.')"

    MSG_INVALID_CHARS = ("Имя вершины должно содержать только буквы пробелы или дефисы. "
                         "\nНапример: 'Москва', 'Нью-Йорк'")
    MSG_NOT_FOUND = "Данной вершины нет в списке:{}"
    MSG_DUPLICATE = "Вершина с таким именем уже существует."
    
    NAME_PATTERN = re.compile(r"[А-Яа-яЁеa-zA-Z]+([- ][А-Яа-яЁеa-zA-Z]+)*")

    def __init__(self):
        self.graph = DiGraph()
        self.nodes = []

    def normalize_name(self, name: str) -> str:
        return name.replace(' ', '').replace('-', '').lower()

    def is_valid_format(self, name: str) -> bool:
        return bool(self.NAME_PATTERN.fullmatch(name.strip()))

    def get_numbered_list(self) -> str:
        return ", ".join([f"{i + 1}. {n}" for i, n in enumerate(self.nodes)])

    def input_nodes(self):
        print('ВВОД ВЕРШИН')
        while True:
            node = input(self.PROMPT_NODE).strip()
            if node == '.':
                break

            if not self.is_valid_format(node):
                print(self.MSG_INVALID_CHARS)
                continue

            normalized = self.normalize_name(node)
            if any(normalized == self.normalize_name(n) for n in self.nodes):
                print(self.MSG_DUPLICATE)
                continue

            self.nodes.append(node)
            self.graph.add_node(node)
            print(f"Вы ввели: {self.get_numbered_list()}")

    def get_valid_choice(self, promt: str) -> str | None:
        while True:
            choice = input(promt).strip()
            if choice == '.':
                return None
            if choice not in self.nodes:
                print(self.MSG_NOT_FOUND.format(self.get_numbered_list()))
                continue
            return choice
        
    def input_edges(self):
        if not self.nodes:
            print("Список вершин пуст. Построение рёбер пропущено.")
            return

        print('ПОСТРОЕНИЕ ГРАФА')
        while True:
            start = self.get_valid_choice(self.PROMPT_EDGE_FROM)
            if start is None:
                break

            finish = self.get_valid_choice(self.PROMPT_EDGE_TO)
            if finish is None:
                break

            self.graph.add_edge(start, finish)
            print(f"Создано ребро: {start} -> {finish}")

    def draw_graph(self):
        if not self.graph.nodes:
            print("Граф пуст, рисовать нечего.")
            return
        
        pos = spring_layout(self.graph)
        draw(self.graph, pos, with_labels=True, node_color='lightblue',
             node_size=2500, font_size=10, arrowsize=20)
        title("Ваш ориентированный граф")
        show()

    def run(self):
        self.input_nodes()
        self.input_edges()
        self.draw_graph()
        print(f"Итоговый список вершин: {', '.join(self.nodes)}")

if __name__ == "__main__":
     app = GraphBuilder() 
     app.run()        
