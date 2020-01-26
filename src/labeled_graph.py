import time

class Graph:
    def __init__(self, adjacency_list, end_vertices):
        self.adjacency_list = adjacency_list
        self.end_vertices = end_vertices
        self.solutions = []

    def neighbors(self, index):
        return self.adjacency_list[index]
    
    def end_labels(self, labels):
        return list(map(lambda vertex: labels[vertex], self.end_vertices)) 

    def init_remaining_labels(self):
        return list(range(len(self.adjacency_list)))

    def try_label(self, label, index, remaining_labels, labels, edge_differences):
        remaining_edge_differences = \
            map(lambda i: abs(label - labels[i]) , self.neighbors(index))
        new_edge_differences = edge_differences.copy()
        for d in remaining_edge_differences:
            if d in edge_differences:
                return 0, 0, 0, False
            else:
                new_edge_differences.add(d)
        new_labels = labels + [label]
        new_remaining_labels = []
        for v in remaining_labels:
            if v != label:
                new_remaining_labels.append(v)
        return new_remaining_labels, new_labels, new_edge_differences, True
        
    def helper(self, remaining_labels, labels, edge_differences, index):
        if index >= len(self.adjacency_list):
            self.solutions.append(self.end_labels(labels))
        else:
            for v in remaining_labels:
                new_remaining_labels, new_labels, new_edge_differences, is_valid = \
                    self.try_label(v, index, remaining_labels, labels, edge_differences)
                if is_valid:
                    self.helper(new_remaining_labels, new_labels, new_edge_differences, index+1)

    def find_all_graceful_ends(self):
        t = time.time()
        self.helper(self.init_remaining_labels(), [], set(), 0)
        print(time.time() - t)

    def write_graceful_ends(self, fn):
        f = open(fn, 'w')
        for solution in self.solutions:
            s = "1 "
            for i in range(len(solution)):
                s += str(solution[i])
                if i == len(solution) - 1:
                    s += "\n"
                else:
                    s += " "
            f.write(s)
        
g_1_1_1 = Graph({0: [], 1: [0], 2: [0], 3: [0]}, [1, 2, 3])
g_2_1_1 = Graph({0: [], 1: [0], 2: [0], 3: [0], 4: [3]}, [1, 2, 4])
g_3_1_1 = Graph({0: [], 1: [0], 2: [0], 3: [0], 4: [3], 5: [4]}, [1, 2, 5])
g_4_1_1 = Graph({0: [], 1: [0], 2: [0], 3: [0], 4: [3], 5: [4], 6: [5]}, [1, 2, 6])
g_5_1_1 = Graph({0: [], 1: [0], 2: [0], 3: [0], 4: [3], 5: [4], 6: [5], 7: [6]}, [1, 2, 7])
g_6_1_1 = Graph({0: [], 1: [0], 2: [0], 3: [0], 4: [3], 5: [4], 6: [5], 7: [6], 8: [7]}, [1, 2, 8])
g_7_1_1 = Graph({0: [], 1: [0], 2: [0], 3: [0], 4: [3], 5: [4], 6: [5], 7: [6], 8: [7], 9: [8]}, [1, 2, 9])
g_8_1_1 = Graph({0: [], 1: [0], 2: [0], 3: [0], 4: [3], 5: [4], 6: [5], 7: [6], 8: [7], 9: [8], 10: [9]}, [1, 2, 10])
g_9_1_1 = Graph({0: [], 1: [0], 2: [0], 3: [0], 4: [3], 5: [4], 6: [5], 7: [6], 8: [7], 9: [8], 10: [9], 11: [10]}, [1, 2, 11])
g_10_1_1 = Graph({0: [], 1: [0], 2: [0], 3: [0], 4: [3], 5: [4], 6: [5], 7: [6], 8: [7], 9: [8], 10: [9], 11: [10], 12: [11]}, [1, 2, 12])
g_11_1_1 = Graph({0: [], 1: [0], 2: [0], 3: [0], 4: [3], 5: [4], 6: [5], 7: [6], 8: [7], 9: [8], 10: [9], 11: [10], 12: [11], 13: [12]}, [1, 2, 13])
n_1_1_graphs = [g_1_1_1, g_2_1_1, g_3_1_1, g_4_1_1, g_5_1_1, g_6_1_1, g_7_1_1, g_8_1_1, g_9_1_1, g_10_1_1, g_11_1_1]
to_do = n_1_1_graphs
fns = ['1-1-1', '2-1-1', '3-1-1', '4-1-1', '5-1-1', '6-1-1', '7-1-1', '8-1-1', '9-1-1', '10-1-1', '11-1-1']
to_do_fns = fns
fns = list(map(lambda fn: 'ends/' + fn, to_do_fns))    
for i in range(len(fns)):
    to_do[i].find_all_graceful_ends()
    to_do[i].write_graceful_ends(fns[i])
