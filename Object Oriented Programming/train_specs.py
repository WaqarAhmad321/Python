class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def status(self):
        print(f"The number of seats in the train are {self.seats}")

    def fare_info(self):
        print(f"The fare of the train is Rs.{self.fare}")

    def bookTicket(self):
        if self.seats > 0:
            print(
                f"Your seat have been booked and your seat number is {self.seatno}")
            self.seats = self.seats - 1
        else:
            print("You can't book because the train is full.")


intercity = Train("Karachi Express", 10, 100)
intercity.seatno = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
