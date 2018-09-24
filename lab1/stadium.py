class Stadium:
    comparing_number = 0
    change_number = 0

    @staticmethod
    def compare_count():
        Stadium.comparing_number += 1
        return Stadium.comparing_number

    @staticmethod
    def change_count():
        Stadium.change_number += 1
        return Stadium.change_number

    @staticmethod
    def reset_count():
        Stadium.comparing_number = 0
        Stadium.change_number = 0

    def __init__(self, name, max_seats, spotlights):
        self.name = name
        self.max_seats = max_seats
        self.spotlights = spotlights

    def __repr__(self):
        return str(self.name) + " " + str(self.max_seats) + " " + str(self.spotlights)