class Level:

    def __init__(self, number):

        self.number = number
        self.time_limit = 60

        if self.number == 1:
            self.goal = 150

        elif self.number == 2:
            self.goal = 250

        else:
            self.goal = 350