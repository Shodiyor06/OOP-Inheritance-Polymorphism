class Character:
    def attack(self):
        pass

    def defend(self):
        pass

class Warrior(Character):
    def attack(self):
        print("Warrior qilich bilan hujum qilmoqda")

    def defend(self):
        print("Warrior qalqon bilan himoyalanmoqda")

class Mage(Character):
    def attack(self):
        print("Mage sehr bilan hujum qilmoqda")

    def defend(self):
        print("Mage sehrli qalqon qoymoqda")

class Archer(Character):
    def attack(self):
        print("Archer oq uzmoqda")

    def defend(self):
        print("Archer qochib pozitsiya ozgartirmoqda")

warrior = Warrior()
warrior.attack()
warrior.defend()

mage = Mage()
mage.attack()
mage.defend()

archer = Archer()
archer.attack()
archer.defend()
