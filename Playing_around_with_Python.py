print("Hello world!")
nodes = []
nodes.append('Москва')
numbered_nodes =  [f"{i}.{n}" for i, n in enumerate(nodes, start=1)] #Далее создаём нумерованный список
print(numbered_nodes)
    