# Search methods

import search,time

ab = search.GPSProblem('A', 'B', search.romania)

print("A --> B")
# imprimir tiempo de ejecución
print("Breadth First Search")
start_time = time.time()
print(search.breadth_first_graph_search(ab).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Depth First Search")
start_time = time.time()
print(search.depth_first_graph_search(ab).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Branch and Bound")
start_time = time.time()
print(search.b_a_b(ab).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Branch and Bound with subestimation")
start_time = time.time()
print(search.b_a_b_sub(ab).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")

###############################################################################
print("###############################################################################")

oe = search.GPSProblem('O', 'E', search.romania)

print("O --> E")
# imprimir tiempo de ejecución
print("Breadth First Search")
start_time = time.time()
print(search.breadth_first_graph_search(oe).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Depth First Search")
start_time = time.time()
print(search.depth_first_graph_search(oe).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Branch and Bound")
start_time = time.time()
print(search.b_a_b(oe).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Branch and Bound with subestimation")
start_time = time.time()
print(search.b_a_b_sub(oe).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")

###############################################################################
print("###############################################################################")

gz = search.GPSProblem('G', 'Z', search.romania)

print("G --> Z")
# imprimir tiempo de ejecución
print("Breadth First Search")
start_time = time.time()
print(search.breadth_first_graph_search(gz).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Depth First Search")
start_time = time.time()
print(search.depth_first_graph_search(gz).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Branch and Bound")
start_time = time.time()
print(search.b_a_b(gz).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Branch and Bound with subestimation")
start_time = time.time()
print(search.b_a_b_sub(gz).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")

###############################################################################
print("###############################################################################")

nd = search.GPSProblem('N', 'D', search.romania)

print("N --> D")
# imprimir tiempo de ejecución
print("Breadth First Search")
start_time = time.time()
print(search.breadth_first_graph_search(nd).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Depth First Search")
start_time = time.time()
print(search.depth_first_graph_search(nd).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Branch and Bound")
start_time = time.time()
print(search.b_a_b(nd).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Branch and Bound with subestimation")
start_time = time.time()
print(search.b_a_b_sub(nd).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")

###############################################################################
print("###############################################################################")

mf = search.GPSProblem('M', 'F', search.romania)

print("M --> F")
# imprimir tiempo de ejecución
print("Breadth First Search")
start_time = time.time()
print(search.breadth_first_graph_search(mf).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Depth First Search")
start_time = time.time()
print(search.depth_first_graph_search(mf).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Branch and Bound")
start_time = time.time()
print(search.b_a_b(mf).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")



print("Branch and Bound with subestimation")
start_time = time.time()
print(search.b_a_b_sub(mf).path())
print("Tiempo de ejecución:" + (str(time.time() - start_time) + " segundos"))
print("------------------------------------")

