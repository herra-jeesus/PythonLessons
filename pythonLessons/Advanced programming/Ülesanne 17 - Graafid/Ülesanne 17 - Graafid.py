"""
Ülesanne 17 - Graafid
Juhend: https://courses.cs.ttu.ee/w/images/f/fc/2014_Loeng_Graafid.pdf
"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

from matplotlib import pyplot
import networkx

def main():
	# Graph generation
    G = networkx.fast_gnp_random_graph(23, 0.142357, 142357)
    pos = networkx.spring_layout(G)

    # Shortest path
    path = networkx.shortest_path(G, source=1, target=7)
    path_edges = list(zip(path, path[1:]))

    # Drawing
    networkx.draw_networkx(G, pos)
    networkx.draw_networkx_nodes(G, pos, nodelist=path, node_color='g')
    networkx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='g', width=10)

    # Axis off, unneccessary.
    pyplot.axis('on')
    pyplot.show()

if __name__ == "__main__":
    main()