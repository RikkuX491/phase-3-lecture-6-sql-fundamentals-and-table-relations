import ipdb

class Car:

    def __init__(self, make, year, plate_number, color):
        self.make = make
        self.year = year
        self.plate_number = plate_number
        self.color = color
    
    def honk_horn(self):
        print("Beep beep!")

    def go(self):
        print("VROOOOM!")

    def get_year(self):
        print("Getting the year...")
        return self._year
    
    def set_year(self, year):
        if(2000 <= year <= 2023):
            print("Setting the year...")
            self._year = year
        else:
            raise Exception("Invalid year!")
        
    def get_plate_number(self):
        print("Getting the plate number...")
        return self._plate_number
    
    def set_plate_number(self, plate_number):
        if(type(plate_number) == str) and (len(plate_number) == 7):
            print("Setting the plate number...")
            self._plate_number = plate_number
        else:
            raise Exception("Invalid plate number!")

    year = property(get_year, set_year)
    plate_number = property(get_plate_number, set_plate_number)

car1 = Car("Honda", 2023, "ABC1234", "Red")
car2 = Car("Ford", 2021, "BCD2345", "Blue")