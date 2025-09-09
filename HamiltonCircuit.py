#Program: HamiltonCircuit.py
#Purpose: given a graph, the program will print out if it has a Hamilton circuit or not
#Inputs: none
#Outputs: prints if the graph has a Hamilton circuit or not
#Author: Ruth Higgason
#Creation: 

def has_hamiltonian_circuit(graph):
  n = len(graph)

  # Check if the graph has at least 3 vertices
  if n < 3:
      print("Graph does not have a Hamiltonian circuit (insufficient vertices).")
      return False

  # Check if each vertex has a degree of at least n/2
  for vertex, edges in enumerate(graph):
      if len(edges) < n/2:
          print("Graph does not have a Hamiltonian circuit (Dirac's condition not satisfied).")
          return False

  print("Graph has a Hamiltonian circuit (Dirac's condition satisfied).")
  return True

# Example usage:
# Represent the graph as an adjacency list
graph = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
has_hamiltonian_circuit(graph)
