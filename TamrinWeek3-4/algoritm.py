class Graph:
    """
    simple graph
    """

    def __init__(self):
        self.adjList = {}
        self.configuration = 1

    def add_node(self, node_a):
        self.adjList[node_a] = []

    def add_edge(self, node_a, node_b):
        if node_a not in self.adjList.keys():
            self.add_node(node_a)

        if node_b not in self.adjList.keys():
            self.add_node(node_b)
        if node_b not in self.adjList[node_a]:
            self.adjList[node_a].append(node_b)
        if node_a not in self.adjList[node_b]:
            self.adjList[node_b].append(node_a)

    def print_graph(self):
        print(self.adjList)

    

    def find_all_paths(self, start_node, end_node, path=[]):
        path = path + [start_node]
        if start_node == end_node:
            return [path]
        paths = []
        for node in self.adjList[start_node]:
            if node not in path:
                temp_paths = self.find_all_paths(node,
                                                 end_node,
                                                 path)
                for item in temp_paths:
                    paths.append(item)
        return paths

    


g = Graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)

g.add_edge(1, 5)
g.add_edge(1, 2)
g.add_edge(1,4)
g.add_edge(2,3)
g.add_edge(4,3)
g.add_edge(5, 1)



First = len(g.find_all_paths(1, 2))
second = len(g.find_all_paths(1, 3))
third = len(g.find_all_paths(1, 4))
forth = len(g.find_all_paths(1, 5))

sum = First+second+third+forth+1

print(f'OutPut: {sum}')




