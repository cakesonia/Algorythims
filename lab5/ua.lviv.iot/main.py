import collections
import functools


class memoized(object):
    """Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).
   """

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__

    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)


@memoized
def fun(cur_letter, count):
    if cur_letter in letter_graph.keys():
        for obj in letter_graph[cur_letter]:
            count = fun(obj, count)
    if (cur_letter == (str(height - 1) + str(width - 1))) or (cur_letter == ("0" + str(width - 1))):
        count += 1
    return count


def search_start():
    total_paths = 0
    for start_brick in range(height):
        total_paths += fun('0' + str(start_brick), 0)
    return total_paths


def read_data_from_file():
    lst = []
    try:
        with open('ijones.in') as ijones:
            lines = [line.rstrip('\n') for line in ijones]
            for line in lines:
                symbol = line.split(' ')
                lst.append(symbol)
    except FileNotFoundError:
        print("File with data does not exist")
    return lst


def ijones_algo(input_letters, width_matrix, height_matrix):
    graph = dict()
    for i in range(0, width_matrix):
        for j in range(0, height_matrix - 1):
            letter_list = [str(i) + str(j + 1)]
            letter_list = find_same_letter(input_letters, letter_list, input_letters[i][j], width_matrix, height_matrix, i, j)
            graph[str(i) + str(j)] = letter_list
    return graph


def find_same_letter(input_letters, letter_list, current_letter, width_matrix, height_matrix, cur_row, cur_column):
    for i in range(0, height_matrix):
        for j in range(cur_column + 1, width_matrix):
            if (input_letters[i][j] == current_letter) and not ((i == cur_row) and (j == cur_column + 1)):
                letter_list.append(str(i) + str(j))
    return letter_list


if __name__ == '__main__':
    input_data = read_data_from_file()
    width = int(input_data[0][0])
    height = int(input_data[0][1])
    input_data.pop(0)
    print(input_data)
    letter_graph = ijones_algo(input_data, width, height)
    print(letter_graph)
    print(search_start())
