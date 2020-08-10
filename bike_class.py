class Bike:
    condition = "new"

    def __init__(self, model, color, average):
        self.model = model
        self.color = color
        self.average = average

    def display_bike(self):
        print("This is a %s %s with %s average" %
              (self.color, self.model, self.average))


my_bike = Bike("CD 100","Red","24.5")
my_bike.display_bike()