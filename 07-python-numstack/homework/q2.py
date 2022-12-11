import networkx as nx
import matplotlib.pyplot as plt

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

@my_timer
def large_clique_size_heuristic(G: nx.Graph):
  # Find the cliques in the graph
  cliques = nx.find_cliques(G)

  # Find the size of the largest clique
  max_size = 0
  for clique in cliques:
      max_size = max(max_size, len(clique))

  # Returns the size of the largest clique
  return max_size

@my_timer
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

# Compare the two given functions and calculates the approximation ratio between them, for a given number of experiments
def compare_functions(accurate_func: callable, heuristic_func:callable, num_of_experiments: int):
  results = {}

  for t in range(1, num_of_experiments+1):
    # Create a random graph with t*10 nodes
    num_of_nodes = t*10
    edge_probability = 0.5
    G = nx.gnp_random_graph(num_of_nodes, edge_probability)

    print('num of nodes:', num_of_nodes)

    max_size_heuristic = heuristic_func(G)
    # Print the size of the largest clique
    # print("Size of largest clique:", max_size_heuristic)

    max_size_accurate = accurate_func(G)
    # Print the size of the largest clique
    # print("Size of largest clique (accurate):", max_size_accurate)

    # Caulculates the approximation ratio of the algorithem 
    approximation_ratio = max_size_heuristic / max_size_accurate * 100
    # Store the results in a dictionary in the format: {num_of_nodes: approximation_ratio}
    results[num_of_nodes] = approximation_ratio

  return results


def main():
  # # Create the graph
  # G = nx.Graph()
  # G.add_edges_from([('a', 'b'), ('a', 'c'), ('b', 'c')])

  accurate_func = large_clique_size_accurate
  heuristic_func = large_clique_size_heuristic
  num_of_experiments = 15
  results = compare_functions(accurate_func, heuristic_func, num_of_experiments)
  print(results)
  plot(results)


if __name__ == "__main__":
  main()

