import math


def read_data(data):
    n = int(math.sqrt(len(data)))
    readed_data = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            readed_data[i][j] = data[i * n + j]
    return readed_data


def reverse_graph(data, n):
    readed_data = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            readed_data[i][j] = data[j][i]
    return readed_data


def dfs(graph, n, start, start_weight, difference):
    edges = {start_weight}

    def dfs_main(start):
        used.add(start)
        for index, node_weight in enumerate(graph[start]):
            if index not in used and index != start:
                edges.add(node_weight)
                if (max(edges) - min(edges)) <= difference:
                    dfs_main(index)
                else:
                    edges.remove(node_weight)
    used = set()
    dfs_main(start)
    return used


def find_answer(graph, reversed_graph, n, max_difference):
    answer_found = False
    answers = set()
    for diff in range(max_difference):
        copy_graph = graph[0].copy()[1:]
        for start_weight in copy_graph:
            answer = dfs(graph, n, 0, start_weight, diff)
            if len(answer) == n:
                reverse_answer = dfs(reversed_graph, n, 0, start_weight, diff)
                if len(reverse_answer) == n:
                    print("Answer: " + str(diff))
                    answers.add(diff)
                    answer_found = True
            if answer_found:
                break
        if answer_found:
            break


if __name__ == '__main__':
    input_data = str.split(input("Please enter nodes: "), ",")
    input_data = [int(value) for value in input_data]
    input_set = set(input_data)
    graph = read_data(input_data)
    n = len(graph)
    reversed_graph = reverse_graph(graph, n)
    max_edge = max(input_set)
    min_edge = min(input_set)
    max_difference_between_edges = max_edge - min_edge + 1
    find_answer(graph, reversed_graph, n, max_difference_between_edges)
