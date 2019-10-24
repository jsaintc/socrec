import networkx as nx
from networkx.drawing.nx_pydot import write_dot
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_node("Alice")
G.add_node("Bob")
G.add_node("Chuck")
G.add_node("Dave")
G.add_node("Eugene")
G.add_node("Faye")
G.add_edge("Bob", "Alice")
G.add_edge("Bob", "Chuck")
G.add_edge("Dave", "Alice")
G.add_edge("Eugene", "Alice")
G.add_edge("Chuck", "Faye")
G.add_edge("Chuck", "Dave")
G.add_edge("Faye", "Bob")

options = {
	'with_labels':False,
	'node_color': 'black',
	'node_size': 100,
	'width': 3}

#nx.write_graphml(G,'test2.graphml')
write_dot(G,'test.dot')
plt.subplot(221)
nx.draw(G, **options)
plt.subplot(222)
nx.draw_circular(G, **options)
plt.subplot(223)
nx.draw_random(G, **options)
plt.subplot(224)
nx.draw_spectral(G, **options)
plt.show()
