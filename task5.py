# Parent class
class Appliance:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class TV(Appliance):
    def turn_on(self):
        return "TV yoqildi: Kanal korsatilmoqda "

    def turn_off(self):
        return "TV ochirildi: Ekran qora boldi "

class Fridge(Appliance):
    def turn_on(self):
        return "Muzlatkich yoqildi: Sovitish boshlandi"

    def turn_off(self):
        return "Muzlatkich ochirildi: Sovitish toxtadi"
appliances = [TV(), Fridge()]

for device in appliances:
    print(device.turn_on())
    print(device.turn_off())
    print('\n')
