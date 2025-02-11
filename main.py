class Character:
    total_damage = 0
    character_list = {}
    
    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage
        self._add_class_to_dict()

    def greeting(self):
        return f"Hey, i'm {self.name}, I have {self.health} Health, {self.armor} Armor, {self.damage} Damage."
    
    def take_damage(self, damage):
        self.health -= damage
    
    def _add_class_to_dict(self):
        if self.name in Character.character_list:
            print(f"Character already exists {self.name}, Entry not Updated")
        else:
            Character.character_list[self.name] = {
                "health": self.health,
                "armor": self.armor,
                "damage": self.damage
            }
        return Character.character_list
    

def list_character_attr(character_dict):
    character_dict = Character.character_list
    for name in character_dict:
        health = character_dict[name]["health"]
        armor = character_dict[name]["armor"]
        damage = character_dict[name]["damage"]
        print(f"Name: {name}, Health: {health}, Armor: {armor}, Damage {damage}")

def character_battle(victim, attacker):
    while victim.health > 0:
        victim.take_damage(attacker.damage)
        print(f"{victim.name} took {attacker.damage} Damage from: {attacker.name}. Health: {victim.health}")
        if victim.health <= attacker.damage:
            victim.health = 0
            print(f"{victim.name} took {attacker.damage} Damage from: {attacker.name}. Health: {victim.health}")
            print(f"{victim.name} is Dead.")


def main():
    Character("Logen Nine", 15, 12, 20)
    Character("Cual Shivers", 10, 20, 5)
    Character("Logen Nine", 1, 1, 1)
    Character("Nicoma Cosca", 8, 10, 3)

    brandon = Character("Brandon", 10, 3, 5)
    luna = Character("Luna", 10, 4, 3)

    print(Character.character_list)
    list_character_attr(Character.character_list)

    character_battle(brandon, luna)


main()