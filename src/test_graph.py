import itertools

class DirectedGraph:
   
    def __init__(self, adjacency_list, graceful_ends):
        # Accepts an undirected adjacency list
        self.adjacency_list = adjacency_list
        self.num_vertices = len(adjacency_list)
        self.graceful_ends = graceful_ends
        self.graceful_labelings = []

    def find_all_graceful_labelings(self):
        possible_labels = list(itertools.permutations(range(self.num_vertices)))
        graceful_labelings = []
        for labeling in possible_labels:
            edge_differences = {} 
            for v in range(self.num_vertices):
                neighbors = self.adjacency_list[v]
                for w in neighbors:
                    d = abs(labeling[v] - labeling[w])
                    if d not in edge_differences:
                        edge_differences[d] = 1
                    else:
                        edge_differences[d] += 1
            is_graceful = True
            for d in edge_differences.keys():
                if edge_differences[d] != 2:
                    is_graceful = False
            if is_graceful:
                self.graceful_labelings.append(list(map(lambda l: labeling[l], self.graceful_ends)))
            
    def __str__(self):
        return str(self.graceful_labelings)

'''
g_1_1_1 = DirectedGraph({0: [1, 2, 3], 1: [0], 2: [0], 3: [0]}, [1, 2, 3])
g_1_1_1.find_all_graceful_labelings()
print(len(g_1_1_1.graceful_labelings))
g_2_1_1 = DirectedGraph({0: [1, 2, 3], 1: [0], 2: [0], 3: [0, 4], 4: [3]},  [1, 2, 4])
g_2_1_1.find_all_graceful_labelings()
print(len(g_2_1_1.graceful_labelings))
g_3_1_1 = DirectedGraph({0: [1, 2, 3], 1: [0], 2: [0], 3: [0, 4], 4: [3, 5], 5: [4]}, [1, 2, 5])
g_3_1_1.find_all_graceful_labelings()
print(len(g_3_1_1.graceful_labelings))
g_4_1_1 = DirectedGraph({0: [1, 2, 3], 1: [0], 2: [0], 3: [0, 4], 4: [3, 5], 5: [4, 6], 6: [5]}, [1, 2, 6])
g_4_1_1.find_all_graceful_labelings()
print(len(g_4_1_1.graceful_labelings))
g_5_1_1 = DirectedGraph({0: [1, 2, 3], 1: [0], 2: [0], 3: [0, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6]}, [1, 2, 7])
g_5_1_1.find_all_graceful_labelings()
print(len(g_5_1_1.graceful_labelings))
g_6_1_1 = DirectedGraph({0: [1, 2, 3], 1: [0], 2: [0], 3: [0, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [7]}, [1, 2, 8])
g_6_1_1.find_all_graceful_labelings()
print(len(g_6_1_1.graceful_labelings))
g_7_1_1 = DirectedGraph({0: [1, 2, 3], 1: [0], 2: [0], 3: [0, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [7, 9], 9: [8]}, [1, 2, 9])
g_7_1_1.find_all_graceful_labelings()
print(len(g_7_1_1.graceful_labelings))
'''


class UndirectedGraph:
    def __init__(self, adjacency_list, graceful_ends):
        self.adjacency_list = adjacency_list
        self.graceful_ends = graceful_ends
        self.n_vertices = len(adjacency_list)
        self.solutions = []

    def find_all_graceful_labelings(self):
        all_labelings = list(itertools.permutations(range(self.n_vertices)))
        for labeling in all_labelings:
            edge_differences = set()
            repeat = False
            for v in range(self.n_vertices):
                neighbors = self.adjacency_list[v]
                for w in neighbors:
                    d = abs(labeling[v] - labeling[w])
                    if d in edge_differences:
                        repeat = True
                    else:
                        edge_differences.add(d)
                if repeat:
                    break
            if not repeat:
                self.solutions.append(map(lambda l: labeling[l], self.graceful_ends))

g_1_1_1 = UndirectedGraph({0: [], 1: [0], 2: [0], 3: [0]}, [1, 2, 3])
g_2_1_1 = UndirectedGraph({0: [], 1: [0], 2: [0], 3: [0], 4: [3]}, [1, 2, 4])
g_3_1_1 = UndirectedGraph({0: [], 1: [0], 2: [0], 3: [0], 4: [3], 5: [4]}, [1, 2, 5])
g_4_1_1 = UndirectedGraph({0: [], 1: [0], 2: [0], 3: [0], 4: [3], 5: [4], 6: [5]}, [1, 2, 6])
g_5_1_1 = UndirectedGraph({0: [], 1: [0], 2: [0], 3: [0], 4: [3], 5: [4], 6: [5], 7: [6]}, [1, 2, 7])
g_6_1_1 = UndirectedGraph({0: [], 1: [0], 2: [0], 3: [0], 4: [3], 5: [4], 6: [5], 7: [6], 8: [7]}, [1, 2, 8])
g_7_1_1 = UndirectedGraph({0: [], 1: [0], 2: [0], 3: [0], 4: [3], 5: [4], 6: [5], 7: [6], 8: [7], 9: [8]}, [1, 2, 9])
graphs = [g_1_1_1, g_2_1_1, g_3_1_1, g_4_1_1, g_5_1_1, g_6_1_1, g_7_1_1]
for g in graphs:
    g.find_all_graceful_labelings()
    print(len(g.solutions))
