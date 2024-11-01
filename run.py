# Search methods

import search,time

ab = search.GPSProblem('A', 'B', search.romania)
# imprimir tiempo de ejecución
print("Breadth First Search")
start_time = time.time()
print(search.breadth_first_graph_search(ab).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Breadth First Search")
start_time = time.time()
print(search.depth_first_graph_search(ab).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Breadth First Search")
start_time = time.time()
print(search.b_a_b(ab).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Breadth First Search")
start_time = time.time()
print(search.b_a_b_sub(ab).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
