def read_data_from_file():
    card_list = []
    try:
        with open('lngpok.in') as lngpok:
            reader = lngpok.read().split(' ')
            for number in reader:
                new_number = int(number)
                card_list.append(new_number)
    except FileNotFoundError:
        print("File with data does not exist")
    return card_list


def write_to_file(res):
    try:
        with open('lngpok.out', 'w+') as lngpok_out:
            lngpok_out.write(res.__str__())
    except FileNotFoundError:
        print("File with data does not exist")


def find_joker(card_list):
    joker_idx = 0
    while card_list[joker_idx] == 0:
        joker_idx += 1
    return joker_idx


def get_unique_cards(card_list):
    unique_cards = []
    unique_card_idx = 0
    for k in range(1, len(card_list)):
        if card_list[k] == 0:
            continue
        if card_list[k] != card_list[k-1]:
            unique_card_idx += 1
            unique_cards.append(card_list[k])
    return unique_cards


if __name__ == "__main__":
    cards = read_data_from_file()
    max_seq = 0
    cards.sort()
    print(cards)
    card_seq = get_unique_cards(cards)
    print(card_seq)
    jokers = find_joker(cards)
    count = 0
    current_seq = 0
    for i in range(1, len(card_seq)):
        for j in range(1, len(card_seq)):
            if card_seq[j] - card_seq[i] == 1:
                count += 1
                current_seq = (count + 1) + jokers
                if current_seq > max_seq:
                    max_seq = current_seq
    result = 0
    if len(card_seq) == 1:
        result = len(card_seq) + jokers
    else:
        result = current_seq + jokers
    write_to_file(result)
