import networkx as nx
import matplotlib.pyplot as plt
import doctest

# Measures the run time of the fiven function
# Credit to @erelsgl: https://github.com/erelsgl-at-ariel/research-5783/blob/main/03-python-oop/code/1.decorator.ipynb
def my_timer(orig_func: callable):
    import time

    def wrapper(*args, **kwargs):
        time_before = time.time()
        result = orig_func(*args, **kwargs)
        time_after = time.time()
        print(
            f'my_timer: {orig_func.__name__} ran in: {time_after-time_before} sec')
        return result

    return wrapper

# Plots a line plot to visualize the relationship between the number of nodes and the approximation ratio
def plot(results: dict):
  num_of_nodes = dict.keys(results)
  ratio = dict.values(results)

  # Create a line plot 
  plt.plot(num_of_nodes, ratio)

  # Add labels and title to the plot
  plt.xlabel('Number of Nodes')
  plt.ylabel('Approximation Ratio')
  plt.title('Number of Nodes vs. Approximation Ratio')

  # Show the plot
  plt.show()

# @my_timer
def large_clique_size_heuristic(G: nx.Graph):
  """
  Find the size of a large clique in a graph (using networkx library).
  A clique is a subset of nodes in which each pair of nodes is adjacent.
  This function is a heuristic for finding the size of a large clique in the graph.
  https://networkx.org/documentation/stable/reference/algorithms/generated/networkx
  .algorithms.approximation.clique.large_clique_size.html#networkx.algorithms.approximation.clique.large_clique_size

Examples:
  >>> G1 = nx.Graph()
  >>> G1.add_edges_from([('a', 'b')])
  >>> large_clique_size_heuristic(G1)
  2

  >>> G2 = nx.Graph()
  >>> G2.add_edges_from([('a', 'b'), ('a', 'c'), ('b', 'c')])
  >>> large_clique_size_heuristic(G2)
  3
  """
  # Find the cliques in the graph
  cliques = nx.find_cliques(G)

  # Find the size of the largest clique
  max_size = 0
  for clique in cliques:
      max_size = max(max_size, len(clique))

  # Returns the size of the largest clique
  return max_size

# @my_timer
def large_clique_size_accurate(G: nx.Graph):
  """
  enumeration algorithm for finding all maximal cliques in an undirected graph. 
  That is, it lists all subsets of vertices with the two properties that each pair 
  of vertices in one of the listed subsets is connected by an edge, and no listed subset 
  can have any additional vertices added to it while preserving its complete connectivity. 
  https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm

  Examples:
  >>> G1 = nx.Graph()
  >>> G1.add_edges_from([('a', 'b')])
  >>> large_clique_size_accurate(G1)
  2

  >>> G2 = nx.Graph()
  >>> G2.add_edges_from([('a', 'b'), ('a', 'c'), ('b', 'c')])
  >>> large_clique_size_accurate(G2)
  3
  """
  # Initialize the maximum clique size to 0
  max_size = 0
  
  def bron_kerbosch(R, P, X):
    # Declare that the variable is not local
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

# Compare the two given functions and calculates the approximation ratio between them, for a given number of experiments
def compare_functions(accurate_func: callable, heuristic_func:callable, num_of_experiments: int):
  results = {}

  for t in range(1, num_of_experiments+1):
    # Create a random graph with t*10 nodes
    num_of_nodes = t*10
    edge_probability = 0.5
    G = nx.gnp_random_graph(num_of_nodes, edge_probability)

    max_size_heuristic = heuristic_func(G)
    # Print the size of the largest clique
    # print("Size of largest clique:", max_size_heuristic)

    max_size_accurate = accurate_func(G)
    # Print the size of the largest clique
    # print("Size of largest clique (accurate):", max_size_accurate)

    # Caulculates the approximation ratio of the algorithem 
    approximation_ratio = max_size_heuristic / max_size_accurate
    # Store the results in a dictionary in the format: {num_of_nodes: approximation_ratio}
    results[num_of_nodes] = approximation_ratio

  return results

# The function runs a simulation between both of the functions and plots the results
def simulation(num_of_experiments: int):
  accurate_func = large_clique_size_accurate
  heuristic_func = large_clique_size_heuristic
  results = compare_functions(accurate_func, heuristic_func, num_of_experiments)
  print(results)
  plot(results)


def main():
  (failures, tests) = doctest.testmod(report=True)
  print("{} failures, {} tests".format(failures, tests))
  simulation(num_of_experiments=30)


if __name__ == "__main__":
  main()

