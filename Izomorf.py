import numpy as np
from networkx.algorithms.isomorphism.isomorph import graph_could_be_isomorphic as isomorphic

# Створення рандомної матриці для графу
matrix = np.random.randint(2, size=(5, 5))

# Створення матриці суміжності для графа
graph = nx.from_numpy_matrix(matrix)
adj_matrix = nx.adjacency_matrix(graph).todense()

# Створення другої матриці суміжності
matrix_2 = np.random.randint(2, size=(5, 5))
graph_2 = nx.from_numpy_matrix(matrix_2)
adj_matrix_2 = nx.adjacency_matrix(graph_2).todense()

# Пошук ізоморфізму між графами
isomorphic(graph, graph_2)

if isomorphic(graph, graph_2):
    print("Графи є ізоморфними")
else:
    print("Графи не є ізоморфними")
