class Aircraft:
    """Class for Aircraft: 
        This class is inherited by the following 2 classes (AirbusA319, Boeing777)
        Callable Functions:
            registration()
            num_seats()
    """

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

class AirbusA319(Aircraft):
    """Class for Airbus A319:
        Callable Functions:
            registration()
            num_seats()
            model()
            seating_plan()
    """

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1,23), "ABCDEF"

class Boeing777(Aircraft):
    """Class for Boeing 777: 
        Callable Functions:
            registration()
            num_seats()
            model()
            seating_plan()
    """

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return range(1, 56), "ABCDEGHJK"


# To Run in REPL
# from aircraft import * OR from aircraft import AirbusA319, Boeing777
# a = AirbusA319("Name")
# a.num_seats()
# a.model()
# a.registration()
# a.seating_plan()

