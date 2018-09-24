from stadium import Stadium


def selection_sort_by_spotlights(spotlight_list):
    for i in range(len(spotlight_list)):
        for j in range(i + 1, len(spotlight_list)):
            if spotlight_list[i].spotlights < spotlight_list[j].spotlights:
                spotlight_list[i], spotlight_list[j] = spotlight_list[j], spotlight_list[i]
                Stadium.compare_count()
                Stadium.change_count()
    return spotlight_list


def merge_sort_by_max_seats(max_seats_list):
    if len(max_seats_list) <= 1:
        return max_seats_list
    list_mid = int(len(max_seats_list) / 2)
    left_list = merge_sort_by_max_seats(max_seats_list[:list_mid])
    right_list = merge_sort_by_max_seats(max_seats_list[list_mid:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    result_list = []
    i = 0
    j = 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i].max_seats <= right_list[j].max_seats:
            result_list.append(left_list[i])
            i += 1
        else:
            result_list.append(right_list[j])
            j += 1
            Stadium.change_count()
            Stadium.compare_count()
    result_list += left_list[i:]
    result_list += right_list[j:]
    return result_list
