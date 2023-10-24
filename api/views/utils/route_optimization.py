import networkx as nx


## Pasos del algoritmo completo
# 1. Encontrar todas las tiendas que deben ser visitadas
# 2. Encontrar todos los clientes que deben ser visitados
# Las tiendas y clientes serán objetos del estilo:
# {
#  "id": 1,
#  "lat": 1.234,
#  "long": 1.234,
# }
# 3. Crear el grafo de clientes
def create_graph(clients):
    G = nx.Graph()
    for i in range(len(clients)):
        for j in range(i + 1, len(clients)):
            cliente1 = clients[i]
            cliente2 = clients[j]
            distancia = euclidean_distance(cliente1, cliente2)
            G.add_edge(cliente1["id"], cliente2["id"], weight=distancia)
    return G


def euclidean_distance(client1, client2):
    return (
        (client1["lat"] - client2["lat"]) ** 2
        + (client1["long"] - client2["long"]) ** 2
    ) ** 0.5


# 4. Calcular el árbol de expansión mínimo
def minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G, algorithm="prim")


# 5. Buscar los posibles nodos de partida
def possible_start_nodes(tree, clients):
    if len(clients) == 1:
        return clients
    min_grado = min(tree.degree(nodo) for nodo in tree.nodes())
    nodes_id = [nodo for nodo in tree.nodes() if tree.degree(nodo) == min_grado]
    return list(filter(lambda client: client["id"] in nodes_id, clients))


# 6. Ver que nodo de partida es el que está más cercano a una tienda, con esto se obtiene el nodo de partida para recorrer los clientes
def get_start_node(possible_nodes, groceries):
    if len(possible_nodes) == 1:
        return possible_nodes[0]
    min_distance = float("inf")
    start_node = None
    for node in possible_nodes:
        for grocery in groceries.keys():
            distance = euclidean_distance(node, groceries[grocery])
            if distance < min_distance:
                min_distance = distance
                start_node = node
    return start_node


def get_clients_path(start_node, edges):
    if len(edges) == 0:
        return [start_node]
    # get the path using the start node and the tree
    path = [start_node]
    while len(edges) > 1:
        start_node = path[-1]
        for u, v in edges:
            if u == start_node:
                path.append(v)
                start_node = v
                # remove the edge from the edges list
                edges.remove((u, v))
            elif v == start_node:
                path.append(u)
                start_node = u
                # remove the edge from the edges list
                edges.remove((u, v))
    last_edge = edges[0]
    if last_edge[0] == path[-1]:
        path.append(last_edge[1])
    else:
        path.append(last_edge[0])
    return path


def get_path(path, order, clients):
    start_node_id = path[0]
    start_node = list(filter(lambda client: client["id"] == start_node_id, clients))[0]
    groceries_name = list(order.keys())
    store_path = []
    while groceries_name:
        min_distance = float("inf")
        next_node = None
        for grocery_name in groceries_name:
            grocery = order[grocery_name]
            distance = euclidean_distance(start_node, grocery)
            if distance < min_distance:
                min_distance = distance
                next_node = grocery
                grocery_name_to_remove = grocery_name
        # remove the grocery from the groceries list

        groceries_name.remove(grocery_name_to_remove)
        store_path.append(next_node["id"])
        start_node = next_node
    return store_path[::-1]


def find_path(clients, orders):
    if len(clients) == 0 or len(orders) == 0:
        return [], []
    graph = create_graph(clients)
    tree = minimum_spanning_tree(graph)
    possible_nodes = possible_start_nodes(tree, clients)
    start_node = get_start_node(possible_nodes, orders)
    clients_path = get_clients_path(start_node["id"], list(tree.edges()))
    store_path = get_path(clients_path, orders, clients)
    return clients_path, store_path


def get_groups(order_size_arr, max_space):
    # [{id: ID, size: size, set: False}, ...]

    # iterate input array, add set for each element to false and sort by size
    # set is used to check if the element has been used in a group
    arr = list(
        map(
            lambda x: {"id": x.id, "size": x.total_capacity, "set": False},
            order_size_arr,
        )
    )
    arr.sort(key=lambda x: x["size"])

    # iterate through the array, start from the smallest and largest element
    start = 0
    end = len(order_size_arr) - 1
    possible_group = []
    groups = []
    last_value = 0
    while start < end:
        # if the sum of the two elements is less than the max space, add them to the possible group and set their set to true
        if arr[start]["size"] + arr[end]["size"] + last_value <= max_space:
            if arr[start]["set"] == False:
                possible_group.append([arr[start]["id"], arr[start]["size"]])
                arr[start]["set"] = True

            if arr[end]["set"] == False:
                possible_group.append([arr[end]["id"], arr[end]["size"]])
                arr[end]["set"] = True
            # if the sum of the two elements is greater than the max space, move the end pointer to the right
            last_value += arr[start]["size"]
            start += 1
        # if the sum of the two elements is greater than the max space, move the end pointer to the left
        # append the possible group to the groups array and reset the possible group
        else:
            end -= 1
            groups.append(possible_group) if possible_group != [] else None
            last_value = 0
            possible_group = []
    # if the start and end pointer are the same, add the possible group to the groups array
    if start == start:
        groups.append(possible_group) if possible_group != [] else None
    # Finally, iterate through the array and add the elements that have not been set to the groups array
    for num in arr:
        if num["set"] == False:
            groups.append([num["id"], num["size"]])
    return groups
