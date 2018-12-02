vertexes = set()


def read_from_file():
    with open('tribes.txt') as f:
        data = f.readlines()
    graph = {}

    length = len(data)
    for i in range(1, length):
        nums = [int(n) for n in data[i].split()]
        graph = add_value(graph, nums[0], nums[1])
        graph = add_value(graph, nums[1], nums[0])
        vertexes.add(nums[0])
        vertexes.add(nums[1])

    return graph, length


def add_value(graph, x, y):
    try:
        graph[x]
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


def dfs_main(given_graph):
    tribes_list = []

    def dfs(tribes, start_vertex, parity):
        parity = odd(start_vertex, parity)
        try:
            vertexes.remove(start_vertex)
        except:
            pass
        for vertex in tribes[start_vertex]:
            if vertex in vertexes:
                dfs(tribes, vertex, parity)
    while vertexes:
        parity = [0, 0]
        dfs(given_graph, int(vertexes.pop()), parity)
        tribes_list.append(parity)
    return tribes_list


def count_pairs(different_tribes):
    count = 0
    tribe_list = len(different_tribes)
    for i in range(0, tribe_list):
        for j in range(i, tribe_list):
            if i != j:
                x = different_tribes[i][0] * different_tribes[j][1] + different_tribes[i][1] * different_tribes[j][0]
                count += x
    return count


if __name__ == '__main__':
    graph, length = read_from_file()
    tribes = dfs_main(graph)
    count = count_pairs(tribes)
    print(count)
