import math


def make_matrix_adj(data):
    n = int(math.sqrt(len(data)))
    matrix = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = data[i * n + j]
    return matrix


def reverse_graph(data, n):
    readed_data = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            readed_data[i][j] = data[j][i]
    return readed_data


def dfs(graph, length_graph, start, start_weight, difference):
    edges = {start_weight}
    used = set()
    return dfs_main(start, used, edges, difference)


def dfs_main(start, used, edges, difference):
    used.add(start)
    for index, node_weight in enumerate(graph[start]):
        if index not in used and index != start:
            edges.add(node_weight)
            if (max(edges) - min(edges)) <= difference:
                dfs_main(index, used, edges, difference)
            else:
                edges.remove(node_weight)
    return used


def find_answer(graph, reversed_graph, length, max_difference):
    answer_found = False
    answers = set()
    for difference in range(max_difference):
        copy_graph = graph[0].copy()[1:]
        for start_weight in copy_graph:
            answer = dfs(graph, length, 0, start_weight, difference)
            if len(answer) == length:
                reverse_answer = dfs(reversed_graph, length, 0, start_weight, difference)
                if len(reverse_answer) == length:
                    print("Answer: " + str(difference))
                    answers.add(difference)
                    answers_file = open("answers.txt", 'w')
                    for ans in answers:
                        answers_file.write(str(ans) + "\n")
                    answer_found = True
            if answer_found:
                break
        if answer_found:
            break


if __name__ == '__main__':
    for line in open("profes.txt"):
        data_from_file = line.split(",")
    converted_to_int = []
    for v in data_from_file:
        converted_to_int.append(int(v))
    input_set = set(converted_to_int)
    graph = make_matrix_adj(converted_to_int)
    graph_length = len(graph)
    reversed_graph = reverse_graph(graph, graph_length)
    max_edge = max(input_set)
    min_edge = min(input_set)
    max_difference_between_edges = max_edge - min_edge + 1
    find_answer(graph, reversed_graph, graph_length, max_difference_between_edges)
