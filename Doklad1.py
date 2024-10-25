from collections import defaultdict

def topological_sort(graph):
#   incial start
  in_degree = defaultdict(int)
  for vertex in graph:
    for neighbor in graph[vertex]:
      in_degree[neighbor] += 1
  queue = [vertex for vertex in graph if in_degree[vertex] == 0]
  result = []
# inincial end
# Kahn start
  while queue:
    vertex = queue.pop(0)
    result.append(vertex)
    for neighbor in graph[vertex]:
      in_degree[neighbor] -= 1
      if in_degree[neighbor] == 0:
        queue.append(neighbor)
# Kahn end

  return result

def topological_sort_to_edges(graph):

  arr = topological_sort(graph)
# Into edges start
  l = []

  for v in arr:
    for u in graph[v]:
      if (v, u) not in l:
        l.append((v, u))
# Into edges end
# Print the edges
  print(l)

# Example usage:
graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}

topological_sort_to_edges(graph)



