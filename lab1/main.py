import csv
from stadium import Stadium
from sorting import selection_sort_by_spotlights
from sorting import merge_sort_by_max_seats
from datetime import datetime


def read_data_from_file():
    data_list = []
    try:
        with open('stadium_data.csv') as csvin:
            reader = csv.reader(csvin)
            for row in reader:
                new_stadium = Stadium(row[0], int(row[1]), int(row[2]))
                data_list.append(new_stadium)
    except FileNotFoundError:
        print("File with data does not exist")
    return data_list


def work_time(start_time, finish_time):
    return finish_time - start_time


if __name__ == "__main__":
    stadium_list = read_data_from_file()
    print("Stadium list:\n" + stadium_list.__str__())
    start = datetime.now().microsecond
    print("\nSorted by spotlights:\n" + selection_sort_by_spotlights(stadium_list).__str__())
    finish = datetime.now().microsecond
    print("Work time: " + work_time(start, finish).__str__())
    print("Change: " + str(Stadium.change_number) + "\nCompare: " + str(Stadium.comparing_number))
    Stadium.reset_count()
    start = datetime.now().microsecond
    print("\nSorted by max seats:\n" +
          merge_sort_by_max_seats(stadium_list).__str__())
    finish = datetime.now().microsecond
    print("Work time: " + work_time(start, finish).__str__())
    print("Change: " + str(Stadium.change_number) + "\nCompare: " + str(Stadium.comparing_number))
