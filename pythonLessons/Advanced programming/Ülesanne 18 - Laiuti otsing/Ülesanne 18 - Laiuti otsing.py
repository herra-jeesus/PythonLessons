"""
Ülesanne 18 - Laiuti otsing
Juhend: https://courses.cs.ttu.ee/w/images/5/52/2014_Loeng_19_-_BFS.pdf
"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

import networkx
import random

def bfs1(source, target, graph):
	"""
	Kasutatakse järjekorda (queue) järgmise tipu valikuks ja ei jäta meelde
	tippe, mis on juba läbi käidud või mida on juba nähtud. 
	"""

    queue = [source]
    nodesSearched = 0
    
    while True:
        nodesSearched += 1
        node = queue.pop(0)
        if node == target: break
        queue += graph[node]

    return nodesSearched

def bfs2(source, target, graph):
	"""
	Kasutatakse järjekorda järgmise tipu valikuks ja hulka (set), et jätta
	meelde tipud, mis on juba läbi käidud.
	"""
    queue = [source]
    visited = set()
    nodesSearched = 0
    
    while queue != []:
        nodesSearched += 1
        node = queue.pop(0)
        while queue != [] and node in visited:
            node = queue.pop(0)
        if node not in visited:
            queue += graph[node]

        visited.add(node)
        if target in visited: break

    return nodesSearched

def bfs3(source, target, graph):
	"""
	Kasutatakse järjekorda järgmise tipu valikuks ja hulka, et jätta meelde
	tipud, mida on juba nähtud ja mis on järjekorda mingil hetkel lisatud.
	Iga otsingualgoritm peaks tagastama läbivaadatud tippude arvu.
	"""
    queue = [source]
    seen = set()
    nodesSearched = 0
    
    while queue != []:
        nodesSearched += 1
        node = queue.pop(0)
        while queue != [] and node in seen:
            node = queue.pop(0)
        if node not in seen:
            queue += graph[node]

        seen.add(node)
        seen |= set(graph[node])
        if target in seen: break

    return nodesSearched

def main():
    random.seed()
    print("| algorithm \t| total nodes \t| nodes searched")

    for i in range(3, 10):
        print()
        G = networkx.fast_gnp_random_graph(2**i, random.uniform(0.0, 0.3), 142443)
        graph = networkx.to_dict_of_lists(G)
        tests1 = []
        tests2 = []
        tests3 = []

        for n in range(100):
            while True:
                source = random.randrange(0, len(graph))
                target = random.randrange(0, len(graph))
                if source != target: break

            # Test for path
            try:
                test = networkx.shortest_path(G, source, target)
                path_exists = True
            except networkx.NetworkXNoPath:
                path_exists = False

            if path_exists:
                tests1.append(bfs1(source, target, graph))
            else: # Path doesn't exist
                tests1.append(len(graph))

            tests2.append(bfs2(source, target, graph))
            tests3.append(bfs3(source, target, graph))

        print("| {0} \t\t| {1} \t\t| {2}".format("bfs1", 2**i, sum(tests1)))
        print("| {0} \t\t| {1} \t\t| {2}".format("bfs2", 2**i, sum(tests2)))
        print("| {0} \t\t| {1} \t\t| {2}".format("bfs3", 2**i, sum(tests3)))

if __name__ == "__main__":
    main()