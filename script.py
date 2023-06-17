import networkx as nx
import matplotlib.pyplot as plt

def add_edge(a, b, graph, G):
    if (b in graph[a]) or (b >= len(graph)):
        return
    graph[a].append(b)
    G.add_edge(a,b)

def init_graph(n, G):
    graph = [i for i in range(n)]
    for i in range (0,n):
        graph[i] = []
        G.add_node(i)
    return graph

def check_route_for_node(node, graph, visited):
    for x in graph[node]:
        if not visited[x]:
            visited[x] = True
            check_route_for_node(x, graph, visited)
           

def get_all_route(graph):
    n = len(graph)
    route = [i for i in range(n)]
    for i in range (0,n):
        route[i] = []
    for i in range(0, n):
        visited = [False for i in range(n)]
        check_route_for_node(i, graph, visited)
        for j in range(0, n):
            if visited[j]:
                route[i].append(j)
    return route

def draw_graph(G, filename):
    nx.draw_circular(G,
            node_color='red',
            node_size=1000,
            with_labels=True)
    plt.savefig(filename)
    plt.close()

def find_max(routegraph, a, b):
    res = False
    for node in routegraph[a]:
        if node in routegraph[b]:
            if not res:
                res = node
            elif res in routegraph[node] and node not in routegraph[res]:
                res = node
            elif node in routegraph[res] and res not in routegraph[node]:
                res = res
            else:
                res = "two max"
    return res

def find_min(routegraph, a, b):
    res = False
    n = len(routegraph)
    for i in range(0,n):
        if a in routegraph[i] and b in routegraph[i]:
            if not res:
                res = i
            elif res in routegraph[i] and i not in routegraph[res]:
                res = i
            elif i in routegraph[res] and res not in routegraph[i]:
                res = res
            else:
                res = 'two min'
    return res

def check_cycles(routegraph, n):
    for i in range(0,n):
        if i in routegraph[i]:
            return True
    return False

def beautiful_print(res):
    print('|  edge  |  max  |  min  |')
    for line in res:
        print('|  ' + line['edge'] + ' |   ' + str(line['max']) + '   |   ' + str(line['min']) + '   |')

def check_graph(graph, routegraph):
    res = []
    pred = True
    n = len(graph)
    if check_cycles(routegraph,n):
        print("Есть цикл")
        return False
    for i in range(0,n - 1):
        for j in range(i + 1, n):
            if j in routegraph[i] or i in routegraph[j] or i == j:
                continue
            max = find_max(routegraph, i, j)
            min = find_min(routegraph, i, j)
            res.append({'edge' : '(' + str(i) + ':' + str(j) +')', 'max' : max, 'min' : min})
            if type(min) is bool or type(max) is bool or min == 'two min' or max == 'two max':
                pred = False
    beautiful_print(res)
    return pred

if __name__ == "__main__":
    
    G = nx.DiGraph()
    n = 6 #int(input())
    graph = init_graph(n, G)
    
    add_edge(1, 0, graph, G)
    add_edge(2, 1, graph, G)
    add_edge(3, 2, graph, G) 
    add_edge(3, 4, graph, G)
    add_edge(5, 3, graph, G)
    add_edge(5, 4, graph, G)
    add_edge(5, 0, graph, G)
    add_edge(5, 1, graph, G)

    routegraph = get_all_route(graph)

    if check_graph(graph, routegraph):
        print("\nРешетка")
    else:
        print("\nНе решетка")