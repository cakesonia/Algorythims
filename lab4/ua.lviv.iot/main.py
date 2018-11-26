import math


# parse data
def process_data(data):
    n = int(math.sqrt(len(data)))
    processed_data = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            processed_data[i][j] = data[i * n + j]

    return processed_data


# reverse data to check
def reverse_data(data, n):
    processed_data = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            processed_data[i][j] = data[j][i]

    return processed_data


# main DFS function
def dfs_function(graph, n, start, start_weight, difference):
    edges = {start_weight}

    def dfs(start):
        used.add(start)

        for index, node_weight in enumerate(graph[start]):

            if index not in used and index != start:
                edges.add(node_weight)

                if (max(edges) - min(edges)) <= difference:
                    dfs(index)
                else:
                    edges.remove(node_weight)

    used = set()
    dfs(start)

    return used


# main algorithm function
def difficult_algo(graph, reversed_graph, n, max_difference):
    answer_found = False
    answers = set()

    for difference in range(max_difference):

        copy_graph = graph[0].copy()[1:]

        for start_weight in copy_graph:
            # print("Route with weight " + str(start_weight))
            answer = dfs_function(graph, n, 0, start_weight, difference)
            # print(answer)

            if len(answer) == n:
                # print("Checking route with weight " + str(start_weight))
                reverse_answer = dfs_function(reversed_graph, n, 0, start_weight, difference)
                # print(reverse_answer)

                if len(reverse_answer) == n:
                    print("!!!FIND!!!")
                    print("Answer: " + str(difference))
                    answers.add(difference)
                    answer_found = True

            if answer_found:
                break

        if answer_found:
            break

    print(answers)


if __name__ == '__main__':
    # Process input
    input_data = str.split(input("Please enter nodes: "), ",")
    input_data = [int(value) for value in input_data]

    # Input values
    input_set = set(input_data)
    graph = process_data(input_data)
    n = len(graph)
    reversed_graph = reverse_data(graph, n)

    # Getting max and min
    max_edge = max(input_set)
    min_edge = min(input_set)

    max_difference_between_edge = max_edge - min_edge + 1

    difficult_algo(graph, reversed_graph, n, max_difference_between_edge)