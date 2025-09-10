"""
TASK: Create a Bus class.

Requirements:
1. Store bus capacity and passenger list.
2. Provide a method to add a passenger (if space available).
3. Provide a method to remove a passenger.
4. Provide a method to show all passengers.

Example Usage:
    metro_bus = Bus(capacity=3)
    metro_bus.add_passenger("John")
    metro_bus.add_passenger("Mary")
    metro_bus.add_passenger("Paul")
    metro_bus.add_passenger("Lisa")  # "Bus is full!"
    print(bus.show_passengers())  # ["John", "Mary", "Paul"]
"""
class Bus:
    def __init__(self,add_passenger):
        self.add_perssenger = []
    def add_p(self,add):
        if len(self.add_perssenger) ==3:
            print('bus is full')
        else:
            self.add_perssenger.append(add)
            print(self.add_perssenger)
    def remove_p(self,remove_l):
        self.add_perssenger.remove(remove_l)
        print(self.add_perssenger)

bus = Bus('add_passenger')
bus.add_p('addd')
bus.add_p('wet')
bus.add_p('domnam')
bus.add_p('www')
bus.remove_p('addd')
        