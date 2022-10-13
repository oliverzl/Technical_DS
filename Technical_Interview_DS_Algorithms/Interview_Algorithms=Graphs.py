# a, b, d = depth first traversal
# a, b, c = breadth first traversal

# depth first: stack
# breadth first: queue


graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

# depth first traversal: printing


def depthFirstPrinting(graph, source):
    # source is like the starting node
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbour in graph[current]:
            stack.append(neighbour)
    # return stack # a, c, e, b, d, f  <- this order depends on a's order of neighbours.


# _________________________________________
# UNCOMMENT FUNCTION CALL: DEPTH_FIRST_PRINT
# depthFirstPrinting(graph, 'a')


# ___________________  RECURSION  _________________
def depthFirstPrintRecursion(graph, source):
    print(source)
    for neighbour in graph[source]:
        depthFirstPrintRecursion(graph, neighbour)


# _________________________________________
# UNCOMMENT FUNCTION CALL: DEPTH_FIRST_PRINT_RECURSION
# depthFirstPrintRecursion(graph, 'a')


# _____________   BREADTH FIRST PRINT _____________
#   BREADTH FIRST PRINT  (only iterative) : queue
def breadthFirstPrint(graph, source):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for neighbour in graph[current]:
            queue.append(neighbour)


# _________________________________________
# UNCOMMENT FUNCTION CALL: BREADTH_FIRST_PRINT
# breadthFirstPrint(graph, 'a')


# ____________________   HASPATH   __________________
# indication whether we can travel from source(src) to destination (dst) node. returning True or False

# DEPTH FIRST HAS_PATH RECURSION


def haspathDepth(graph, src, dst):
    if src is dst:
        return True
    for neighbour in graph[src]:
        if haspathDepth(graph, neighbour, dst):
            return True
    return False


#   _________________________________________
# UNCOMMENT FUNCTION CALL HAS_PATH_DEPTH
# print(haspathDepth(graph, 'a', 'f'))


# #  BREADTH FIRST HAS_PATH


# breadthfirstHasPath
def breadth_has_path(graph, src, dst):
    queue = [src]
    while len(queue) > 0:
        current = queue.pop(0)
        if current == dst:
            return True
        for neighbour in graph[current]:
            queue.append(neighbour)
    return False


#   _________________________________________
# UNCOMMENT FUNCTION CALL HAS_PATH_BREADTH
# print(breadth_has_path(graph, 'a', 'f'))


# ____________________   UNDIRECTED_PATH_DEPTH   __________________
# looking for path between src and destination: undirected


def undirected_path_depth(edges, nodeA, nodeB):
    graph = build_graph(edges)
    return hasPath(graph, nodeA, nodeB, set())


def hasPath(graph, src, dst, visited):
    # if src is destination return True
    if src == dst:
        return True
    # if we have visited the node before we can return False
    if src in visited:
        return False
    visited.add(src)
    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dst, visited) is True:
            return True
    return False


# below is an edge list. every pair in this list represents a connection between 2 nodes.
edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"],
]


def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


# build_graph converts the edges list into the adjacency list below. adjacency lists are like the default comfortable format.
# best to convert the edge list into an adjacency list.
# adjacency list:
# graph = {
#     i: [j, k],
#     j: [i],
#     k: [i, m, l],
#     m: [k],
#     l: [k],
#     o: [n],
#     n: [o]
# }

#   _________________________________________
# UNCOMMENT FUNCTION CALL UNDIRECTED_PATH_DEPTH
# print(undirected_path_depth(edges, 'i', 'o'))


# ____________________   CONNECTED_COMPONENTS_COUNT   __________________
# the result for the undirected graph below: 3 CONNECTED COMPONENTS: 1-2 ||| 4-5-6-7-8 ||| 3
graph_connected_components = {
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1],
}

# combine graph traversal and iterative code.


def connected_components(graph):
    visited = set()
    count = 0
    for node in graph:
        # uncomment below to see the set visited.
        # print(visited)
        if explore(graph, node, visited) is True:
            count += 1
    return count


def explore(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)
    for neighbour in graph[current]:
        explore(graph, neighbour, visited)
    return True


#   _________________________________________
# UNCOMMENT FUNCTION CALL CONNECTED_COMPONENTS_COUNT
# print(connected_components(graph_connected_components))


# timestamp 1:15:03
# ____________________   LARGEST_COMPONENT   __________________
# 2 components: 1-0-5-8(size4) ||| 4-2-3(size3)
ad_list_largest_component = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}


def largest_component(graph):
    visited = set()
    largest = 0
    for node in graph:
        size = explore_size(graph, node, visited)
        if size > largest:
            largest = size
        return largest


def explore_size(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)
    size = 1
    for neighbour in graph[node]:
        size += explore_size(graph, neighbour, visited)
    return size


#   _________________________________________
# UNCOMMENT FUNCTION CALL GRAPH_LARGEST_COMPONENT
# print(largest_component(ad_list_largest_component))


# timestamp 1:24:06 SHORTEST PATH
# taking in edgelist

shortest_path_edgelist = [
    ["w", "x"],
    ["x", "y"],
    ["z", "y"],
    ["z", "v"],
    ["w", "v"],
    ["g", "h"],
]


def build_shortest_path_ad_list(edgelist):
    graph = {}
    for item in edgelist:
        a, b = item
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


shortest_path_ad_list = build_shortest_path_ad_list(shortest_path_edgelist)

# print(shortest_path_ad_list)


# if there is a path, nodeA == nodeB, return distance.
def shortest_path(edges, nodeA, nodeB):
    graph = build_shortest_path_ad_list(edges)
    visited = set([nodeA])
    queue = [[nodeA, 0]]
    while len(queue) > 0:
        node, distance = queue.pop(0)
        if node == nodeB:
            return distance
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, distance + 1))
    return f"No path found between {nodeA} and {nodeB}."


#   _________________________________________
# UNCOMMENT FUNCTION CALL SHORTEST_PATH
print(shortest_path(shortest_path_edgelist, "w", "z"))  # 2
print(shortest_path(shortest_path_edgelist, "x", "h"))  # no path found


island_grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
]


def island_count(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited):
                count += 1
    return count


def explore(grid, r, c, visited):
    rowInBounds = 0 <= r and r < len(grid)
    colInBounds = 0 <= c and c < len(grid)
    if (not rowInBounds) or (not colInBounds):
        return False

    if grid[r][c] == "W":
        return False

    pos = r + "," + c
    if pos in visited:
        return False
    visited.append(pos)

    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)

    return True


# print(island_count(island_grid))
