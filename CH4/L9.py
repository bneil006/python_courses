class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target):
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10)


class Wizard(Hero):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.__mana = mana

    def get_mana(self):
        return self.__mana

    def cast(self, target):
       damage = 25
       mana_cost = 25
       if self.__mana < mana_cost:
           raise Exception("not enough mana")
       else:
           self.__mana -= mana_cost
           target.take_damage(damage)


def main():
    brandon = Wizard("Brandon", 50, 100)
    random = Hero("Jal", 50)
    print(f"NAME: {brandon.get_name()}, HEALTH: {brandon.get_health()}, MANA: {brandon.get_mana()}")
    print(f"NAME: {random.get_name()}, HEALTH: {random.get_health()}")

    brandon.cast(random)
    print(f"NAME: {brandon.get_name()}, HEALTH: {brandon.get_health()}, MANA: {brandon.get_mana()}")
    print(f"NAME: {random.get_name()}, HEALTH: {random.get_health()}")


main()