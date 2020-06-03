import networkx as nx
import matplotlib.pyplot as plt
import networkx.drawing

def draw_graph(graph,highlight_nodes = []):
    highlight_nodes_ids = list(map(lambda x:x['id'],highlight_nodes))
    plt.subplot(121)
    G = nx.Graph()
    for node in graph.values():
        G.add_node(node["id"])
        for joined_node in node["joins"]:
            G.add_edge(node["id"],joined_node["id"])
    color_map = []
    for n in G:
        if n in highlight_nodes_ids:
            color_map.append("green")
        else:
            color_map.append("red")
    pos = nx.spring_layout(G)
    plt.subplot(121)
    print(nx.draw(G,pos,node_color=color_map, with_labels=True, font_weight='bold'))
    plt.show()
