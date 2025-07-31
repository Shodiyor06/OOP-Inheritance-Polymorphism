class Courier:
    def delivery_range(self):
        pass

    def calculate_fee(self, distance):
        pass

class BikeCourier(Courier):
    def delivery_range(self):
        print("Masofa: 5 km gacha")

    def calculate_fee(self, distance):
        print("Yetkazib berish haqi: ", distance * 0.5)

class CarCourier(Courier):
    def delivery_range(self):
        print("Masofa: 20 km gacha")

    def calculate_fee(self, distance):
        print("Yetkazib berish haqi: ", distance * 1.0)

class DroneCourier(Courier):
    def delivery_range(self):
        print("Masofa: 10 km gacha")

    def calculate_fee(self, distance):
        print("Yetkazib berish haqi: ", distance * 2.0)

bike_courier = BikeCourier()
bike_courier.delivery_range()
bike_courier.calculate_fee(3)
car_courier = CarCourier()
car_courier.delivery_range()
car_courier.calculate_fee(15)
drone_courier = DroneCourier()
drone_courier.delivery_range()
drone_courier.calculate_fee(8)