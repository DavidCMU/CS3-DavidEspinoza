from collections import deque

def main():
    Weighted_graph = graph()
    Weighted_graph.edge("Carrissan Union", "Barjoran", 14)
    Weighted_graph.edge("Carrissan Union", "Romluan empire",42)
    Weighted_graph.edge("Romluan empire", "borg", 33)
    Weighted_graph.edge("Romluan empire", "United fedration of planets", 53)
    Weighted_graph.edge("United fedration of planets", "Barjoran", 22)
    Weighted_graph.edge("United fedration of planets", "Kingon empire", 87)
    Weighted_graph.edge("Barjoran", "Tholian Assembly", 80)
    Weighted_graph.edge("Kingon empire", "borg", 41)
    Weighted_graph.edge("borg", "Tholian Assembly", 10)
    Weighted_graph.showGraph()

    user_input = input("Please choose a point to start from and ill give you the depth first search for the node you choose \n")
    dfs = Weighted_graph.dfs(user_input)
    print("depth first: " + str(dfs)+ "\n")

    user_input = input("Please choose a point to start from and ill give you the Breadth first search for the other node you choose \n")
    bfs = Weighted_graph.bfs(user_input)
    print("breadth first search: " + str(bfs)+ "\n")
    

class graph():
    def __init__(self):
        self.graph = {}
    
    def vertex(self, V1):
        if V1 not in self.graph:
            self.graph[V1] = {}

    def edge(self, V1, V2, Weight):
        self.vertex(V1)
        self.vertex(V2)
        self.graph[V1][V2] = Weight
        self.graph[V1] = dict(sorted(self.graph[V1].items(), key=lambda item: item[1]))
        self.graph[V2][V1] = Weight
        self.graph[V2] = dict(sorted(self.graph[V2].items(), key=lambda item: item[1]))

    def showGraph(self):
        for vertex in self.graph:
            print(f"{vertex} Connections: {self.graph[vertex]}")

    def dfs(self, start, visted = None, result= None):
        if visted is None:
            visted = set()
        if result is None:
            result = []

        visted.add(start)
        result.append(start)

        for u in self.graph.get(start, {}):
            if u not in visted:
                self.dfs(u, visted, result)
        return result

    def bfs(self, start):
        visted = set([start])
        graph_queue = deque([start])
        result = []
        while graph_queue:
            vertex = graph_queue.popleft()
            result.append(vertex)
            for x in self.graph.get(vertex, {}):
                if x not in visted:
                    visted.add(x)
                    graph_queue.append(x)
        return result

main()