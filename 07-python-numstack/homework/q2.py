import networkx as nx

def large_clique_size_heuristics(G: nx.Graph):
  # Find the cliques in the graph
  cliques = nx.find_cliques(G)

  # Find the size of the largest clique
  max_size = 0
  for clique in cliques:
      max_size = max(max_size, len(clique))

  # Returns the size of the largest clique
  return max_size


def large_clique_size_accurate(G: nx.Graph):
  # Initialize the maximum clique size to 0
  max_size = 0
  
  def bron_kerbosch(R, P, X):
      nonlocal max_size
      
      if len(P) == 0 and len(X) == 0:
          # We have found a clique
          max_size = max(max_size, len(R))
      else:
          for v in P:
              bron_kerbosch(R + [v],
                            [u for u in P if u in G[v]],
                            [u for u in X if u in G[v]])
              P.remove(v)
              X.append(v)
  
  # Find the cliques in the graph
  bron_kerbosch([], list(G.nodes()), [])
  
  # Return the size of the largest clique
  return max_size


# Create the graph
G = nx.Graph()
G.add_edges_from([('a', 'b'), ('a', 'c'), ('b', 'c')])

G2 = nx.gnp_random_graph(200, 0.5)
print(G2)

max_size = large_clique_size_heuristics(G2)
# Print the size of the largest clique
print("Size of largest clique:", max_size)

max_size_accurate = large_clique_size_accurate(G2)
# Print the size of the largest clique
print("Size of largest clique (accurate):", max_size_accurate)
