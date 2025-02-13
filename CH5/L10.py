class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        upgrades = {
            "bronze": "iron",
            "iron": "steel"
        }
        if other.sword_type not in upgrades or other.sword_type != self.sword_type:
            raise Exception("cannot craft")
        else:
            other.sword_type = upgrades[other.sword_type]
            return other.sword_type


def main():
    print(Sword("bronze") + Sword("bronze"))
    print(Sword("iron") + Sword("iron"))
    # print(Sword("bronze") + Sword("iron")) # unhide to throw an exception in the .__add__ overload

main()