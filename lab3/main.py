vertexes = set()


def read_from_file():
    with open('tribes.txt') as f:
        data = f.readlines()
    graph = {}

    length = data.__len__()
    for i in range(1, length):
        nums = [int(n) for n in data[i].split()]
        graph = add_value(graph, nums[0], nums[1])
        graph = add_value(graph, nums[1], nums[0])
        vertexes.add(nums[0])
        vertexes.add(nums[1])

    return graph, length


def add_value(graph, x, y):
    try:
        z = graph[x]
    except KeyError:
        graph[x] = set()
    graph[x].add(y)
    return graph


def odd(vertex, parity):
    if vertex % 2 == 1:
        parity[0] += 1
    else:
        parity[1] += 1
    return parity


def dfs(graph, start_vertex, parity):
    parity = odd(start_vertex, parity)
    try:
        vertexes.remove(start_vertex)
    except:
        pass
    for vertex in graph[start_vertex]:
        if vertex in vertexes:
            dfs(graph, vertex, parity)


def dfs_main(graph):
    tribes = []
    while vertexes:
        parity = [0, 0]
        dfs(graph, int(vertexes.pop()), parity)
        tribes.append(parity)
    return tribes


def count_pairs(tribes):
    count = 0
    length = tribes.__len__()
    for i in range(0, length):
        for j in range(i, length):
            if i != j:
                x = tribes[i][0] * tribes[j][1] + tribes[i][1] * tribes[j][0]
                count += x
    return count


if __name__ == '__main__':
    graph, length = read_from_file()
    tribes = dfs_main(graph)
    count = count_pairs(tribes)
    print(count)
