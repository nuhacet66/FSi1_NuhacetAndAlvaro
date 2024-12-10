# Search methods

import search,time

ab = search.GPSProblem('A', 'B', search.romania)

print("A --> B")
# imprimir tiempo de ejecución
print("Breadth First Search")
start_time = time.time()
print(search.breadth_first_graph_search(ab).path())
# coste de la solución
print("Coste de la solución: " + str(search.breadth_first_graph_search(ab).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Depth First Search")
start_time = time.time()
print(search.depth_first_graph_search(ab).path())
# coste de la solución
print("Coste de la solución: " + str(search.depth_first_graph_search(ab).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Branch and Bound")
start_time = time.time()
print(search.b_a_b(ab).path())
# coste de la solución
print("Coste de la solución: " + str(search.b_a_b(ab).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Branch and Bound with subestimation")
start_time = time.time()
print(search.b_a_b_sub(ab).path())
# coste de la solución
print("Coste de la solución: " + str(search.b_a_b_sub(ab).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")

###############################################################################
print("###############################################################################")
oe = search.GPSProblem('O', 'E', search.romania)

print("O --> E")
# imprimir tiempo de ejecución
print("Breadth First Search")
start_time = time.time()
print(search.breadth_first_graph_search(oe).path())
# coste de la solución
print("Coste de la solución: " + str(search.breadth_first_graph_search(oe).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Depth First Search")
start_time = time.time()
print(search.depth_first_graph_search(oe).path())
# coste de la solución
print("Coste de la solución: " + str(search.depth_first_graph_search(oe).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Branch and Bound")
start_time = time.time()
print(search.b_a_b(oe).path())
# coste de la solución
print("Coste de la solución: " + str(search.b_a_b(oe).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Branch and Bound with subestimation")
start_time = time.time()
print(search.b_a_b_sub(oe).path())
# coste de la solución
print("Coste de la solución: " + str(search.b_a_b_sub(oe).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")

###############################################################################
print("###############################################################################")
gz = search.GPSProblem('G', 'Z', search.romania)

print("G --> Z")
# imprimir tiempo de ejecución
print("Breadth First Search")
start_time = time.time()
print(search.breadth_first_graph_search(gz).path())
# coste de la solución
print("Coste de la solución: " + str(search.breadth_first_graph_search(gz).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Depth First Search")
start_time = time.time()
print(search.depth_first_graph_search(gz).path())
# coste de la solución
print("Coste de la solución: " + str(search.depth_first_graph_search(gz).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Branch and Bound")
start_time = time.time()
print(search.b_a_b(gz).path())
# coste de la solución
print("Coste de la solución: " + str(search.b_a_b(gz).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Branch and Bound with subestimation")
start_time = time.time()
print(search.b_a_b_sub(gz).path())
# coste de la solución
print("Coste de la solución: " + str(search.b_a_b_sub(gz).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")

###############################################################################
print("###############################################################################")

oe = search.GPSProblem('O', 'E', search.romania)

print("A --> B")
# imprimir tiempo de ejecución
print("Breadth First Search")
start_time = time.time()
print(search.breadth_first_graph_search(oe).path())
# coste de la solución
print("Coste de la solución: " + str(search.breadth_first_graph_search(oe).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Depth First Search")
start_time = time.time()
print(search.depth_first_graph_search(oe).path())
# coste de la solución
print("Coste de la solución: " + str(search.depth_first_graph_search(oe).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Branch and Bound")
start_time = time.time()
print(search.b_a_b(oe).path())
# coste de la solución
print("Coste de la solución: " + str(search.b_a_b(oe).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Branch and Bound with subestimation")
start_time = time.time()
print(search.b_a_b_sub(oe).path())
# coste de la solución
print("Coste de la solución: " + str(search.b_a_b_sub(oe).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")

###############################################################################
print("###############################################################################")

nd = search.GPSProblem('N', 'D', search.romania)

print("A --> B")
# imprimir tiempo de ejecución
print("Breadth First Search")
start_time = time.time()
print(search.breadth_first_graph_search(nd).path())
# coste de la solución
print("Coste de la solución: " + str(search.breadth_first_graph_search(nd).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Depth First Search")
start_time = time.time()
print(search.depth_first_graph_search(nd).path())
# coste de la solución
print("Coste de la solución: " + str(search.depth_first_graph_search(nd).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Branch and Bound")
start_time = time.time()
print(search.b_a_b(nd).path())
# coste de la solución
print("Coste de la solución: " + str(search.b_a_b(nd).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Branch and Bound with subestimation")
start_time = time.time()
print(search.b_a_b_sub(nd).path())
# coste de la solución
print("Coste de la solución: " + str(search.b_a_b_sub(nd).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")

###############################################################################
print("###############################################################################")

mf = search.GPSProblem('M', 'F', search.romania)

print("M --> F")
# imprimir tiempo de ejecución
print("Breadth First Search")
start_time = time.time()
print(search.breadth_first_graph_search(mf).path())
# coste de la solución
print("Coste de la solución: " + str(search.breadth_first_graph_search(mf).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Depth First Search")
start_time = time.time()
print(search.depth_first_graph_search(mf).path())
# coste de la solución
print("Coste de la solución: " + str(search.depth_first_graph_search(mf).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Branch and Bound")
start_time = time.time()
print(search.b_a_b(mf).path())
# coste de la solución
print("Coste de la solución: " + str(search.b_a_b(mf).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")



print("Branch and Bound with subestimation")
start_time = time.time()
print(search.b_a_b_sub(mf).path())
# coste de la solución
print("Coste de la solución: " + str(search.b_a_b_sub(mf).path_cost))
print("Tiempo de ejecución:" + (str((time.time() - start_time) * 1e9) + " nanosegundos"))
print("------------------------------------")

###############################################################################
print("###############################################################################")





