import networkx as nx
import matplotlib.pyplot as plt

def generate_random_d_regular_graph(N, d, plot = False):
    G = nx.generators.random_graphs.random_regular_graph(d, N)
    if plot:
        plt.figure('Random {}-regular graph with {} nodes'.format(d, N))
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color='#850D0C',
                                node_size=200)
        nx.draw_networkx_labels(G, pos, font_color='w', font_size=8)
        nx.draw_networkx_edges(G, pos,  edge_color='#F44B4A', arrows=True)
        #plt.show()
    return nx.to_numpy_array(G)

def generate_multiplex_random_d_regular_graph(N, d, L, plot = False):
    G = []
    for l in range(L):
        G.append(generate_random_d_regular_graph(N, d, plot))
    return G

def generate_barabasi_albert_graph(N, m, plot = False):
    G = nx.generators.random_graphs.barabasi_albert_graph(N, m)
    if plot:
        plt.figure("Random Barabasi-Albert graph with {} nodes (m={})".format(N, m))
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color='#19499C',
                               node_size=200)
        nx.draw_networkx_labels(G, pos, font_color='w', font_size=8)
        nx.draw_networkx_edges(G, pos, edge_color='#60A2D3', arrows=True)
        #plt.show()
    return nx.to_numpy_matrix(G)

def generate_multiplex_barabasi_albert_graph(N, m, L, plot = False):
    G = []
    for l in range(L):
        G.append(generate_barabasi_albert_graph(N, m, plot))
    return G