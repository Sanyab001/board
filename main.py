"""
Кратчайший путь фигуры 'Конь' на шахматной доске из
клетки 'd4' в клетку 'f7'
"""

letters = 'abcdefgh'
numbers = '12345678'

graph = dict()
# перебор сочетаний для обозначения клеток
for l in letters:
    for n in numbers:
        graph[l + n] = set()


# проверим существует ли клетка куда можем ходить (не за границей доски)

def add_edge(v1, v2):
    graph[v1].add(v2)
    graph[v2].add(v1)


for i in range(8):
    for j in range(8):
        v1 = letters[i] + numbers[j]
        if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i + 2] + numbers[j + 1]
            add_edge(v1, v2)

        if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i - 2] + numbers[j + 1]
            add_edge(v1, v2)

        if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i + 1] + numbers[j + 2]
            add_edge(v1, v2)

        if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i - 1] + numbers[j + 2]
            add_edge(v1, v2)

from collections import deque
distance = {v: None for v in graph}
parents = {v: None for v in graph}

start_vertex = 'd4'
end_vertex = 'f7'

distance[start_vertex] = 0
# создадим очередь с начальным элементом
queue = deque([start_vertex])

while queue:  # если длинна очереди 0, то вайцл не пройдет
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        if distance[neigh_v] is None:  # значит еще там небыли
            distance[neigh_v] = distance[cur_v] + 1
            parents[neigh_v] = cur_v
            queue.append(neigh_v)

path = [end_vertex]
parent = parents[end_vertex] #берем предка
while parent is not None:
    path.append(parent)
    parent = parents[parent]

print(path[::-1])