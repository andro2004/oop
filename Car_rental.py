class Car_rental:
    def __init__(self, avalible_cars,rented_cars):
        self.avalible_cars = avalible_cars
        self.rented_cars = rented_cars
    def display_available_cars(self):
        print("Available cars for rent:")
        for car in self.avalible_cars:
            print(f"- {car}")
    def rent_car(self, car):
        if car in self.avalible_cars:
            self.avalible_cars.remove(car)
            print(f'{car} is renterd')
            self.rented_cars.append(car)
        elif car in self.rented_cars:
            print(f'{car} is already rented.')
        else:
            print(f'{car} is not available.')
    def return_car(self, car):
        if car in self.rented_cars:
            self.rented_cars.remove(car)
            self.avalible_cars.append(car)
            print(f'{car} is returned.')
        elif car in self.avalible_cars:
            print(f'{car} was not rented')
        else:
            print(f'{car} does not belong to us')
    