class Graph:


    def __init__(self):
        self.adjlist = {}

    def add_node(self,node_a):
        self.adjlist[node_a]=[]

    def add_edge(self,node_a,node_b):
        if node_a not in self.adjlist.keys():
            self.add_node(node_a)
        if node_b not in self.adjlist.keys():
            self.add_node(node_b)
        if node_b not in self.adjlist[node_a]:
            self.adjlist[node_a].append(node_b)
        if node_a not in self.adjlist[node_b]:
            self.adjlist[node_b].append(node_a)

    def print_graph(self):
        print(self.adjlist)


    def short_path(self,node_start,node_end, path=[]):

        new = self.find_all_path(node_start,node_end,path)
        # print("new" ,new)
        flag  = 0
        list_flag = []
        for j in new:
            # print(j)
            for item in j:
                flag = flag + 1
                if flag == len(j):
                    list_flag.append(flag)
                    flag=0



        # print(list_flag)
        count = 0
        min_flag=list_flag[0]
        for i in list_flag:
            if min_flag>=i:
                min_flag = i
                count=count+1

        # print(min_flag)
        # print(count)

        print()
        print()
        return "Short_Way",new[count]
        # print(new[count])






    def is_connected(self,node_a):
        if node_a not in self.adjlist.keys():
            print("Error")
        else:
            print("Node",[node_a],"is connected to -->",self.adjlist[node_a])












    def find_all_path(self,node_start,node_end,path = []):

        path = path + [node_start]
        print(path)
        if node_start==node_end:
            return [path]
        paths = []
        for node in self.adjlist[node_start]:
            if node not in path:
                temp_paths=self.find_all_path(node,node_end,path)
                # print('temp_paths',temp_paths)
                for item in temp_paths:
                    paths.append(item)

        
        return paths




    def find_path(self,node_start,node_end,path= []):
        path = path + [node_start]
        # print(path)
        if node_start==node_end:
            return path

        for node in self.adjlist[node_start]:
            if node not in path:
                temp_path = self.find_path(node,node_end,path)

                if temp_path:

                    return temp_path


g = Graph()

g.add_node("a")
g.add_node("b")
g.add_node("c")
g.add_node("d")
g.add_node("e")
g.add_node("m")
g.add_node("f")


g.add_edge("a", "c")
g.add_edge("c", "b")
g.add_edge("a", "b")
g.add_edge("d", "e")
g.add_edge("e", "c")
g.add_edge("a", "d")
g.add_edge("e", "m")
g.add_edge("d", "f")

# g.print_graph()
print()
# print(g.find_all_path("a", "b"))
# print(g.short_path("a","f"))
print()
g.is_connected("a")
# g.find_all_path("a","f")


