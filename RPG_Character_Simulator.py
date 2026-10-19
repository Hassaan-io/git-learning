class Character:
    def __init__(self, name, health):
        self.name = name
        self._health = int(health)
    def introduce(self):
        print(f"Hi I am {self.name}, and my health is {self._health}")
    def takedamage(self, amount):
        if self._health - int(amount) >= 0:
            self._health -= int(amount)
        else:
            print("Negative health error")
class Warrior(Character):
    def special_attack(self):
        print("Sword Slash!")
class Mage(Character):
    def special_attack(self):
        print("Fireball!")
Warr1 = Warrior("Arthur","100")
Mage1 = Mage("Merlin","80")
Characters = [Warr1, Mage1]
for char in Characters:
    char.introduce()
    char.special_attack()
Warr1.takedamage("30")
Warr1.introduce()