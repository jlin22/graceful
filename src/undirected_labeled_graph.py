from itertools import permutations
class Graph:
    def __init__(self, adjacency_list, end_vertices):
        self.adjacency_list = adjacency_list
        self.end_vertices = end_vertices
        self.solutions = []

    def neighbors(self, index):
        return self.adjacency_list[index]
    
    def end_labels(self, labels):
        return list(map(lambda vertex: labels[vertex], self.end_vertices))

    def is_graceful_label(self, label):
        edge_differences = {}
        for index in range(len(self.adjacency_list)):
            new_edge_differences = list(map(lambda i: abs(label[i] - label[index]), self.neighbors(index)))
            for d in new_edge_differences:
                if d not in edge_differences:
                    edge_differences[d] = 1
                elif edge_differences[d] == 1:
                    edge_differences[d] = 2
                else:
                    return False
        return True
                                        
    def find_all_graceful_ends(self):
        all_labels = permutations(list(range(len(self.adjacency_list))))
        for label in all_labels:
            if self.is_graceful_label(label):
                self.solutions.append(self.end_labels(label))
        
g_1_1_1 = Graph({0: [1, 2, 3], 1: [0], 2: [0], 3: [0]}, [1, 2, 3])
g_1_1_1.find_all_graceful_ends()
print(len(g_1_1_1.solutions))
g_2_1_1 = Graph({0: [1, 2, 3], 1: [0], 2: [0], 3: [0, 4], 4: [3]}, [0, 1, 2, 3, 4])
g_2_1_1.find_all_graceful_ends()
print(len(g_2_1_1.solutions))
print(g_2_1_1.solutions)
g_3_1_1 = Graph({0: [1, 2, 3], 1: [0], 2: [0], 3: [0, 4], 4: [3, 5], 5: [4]}, [1, 2, 5])
g_3_1_1.find_all_graceful_ends()
print(len(g_3_1_1.solutions))
g_4_1_1 = Graph({0: [1, 2, 3], 1: [0], 2: [0], 3: [0, 4], 4: [3, 5], 5: [4, 6], 6: [5]}, [0, 1, 2, 3, 4, 5, 6])
g_4_1_1.find_all_graceful_ends()
print(len(g_4_1_1.solutions))
print(g_4_1_1.solutions)
g_6_1_1 = Graph({0: [1, 2, 3], 1: [0], 2: [0], 3: [0, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [7]}, [1, 2, 8])
g_6_1_1.find_all_graceful_ends()
print(len(g_6_1_1.solutions))

