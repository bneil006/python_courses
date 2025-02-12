def main():
    dragons = [
        Dragon("Green Dragon", 0, 0, 1),
        Dragon("Red Dragon", 2, 2, 2),
        Dragon("Blue Dragon", 4, 3, 3),
        Dragon("Black Dragon", 5, -1, 4),
    ]

    # don't touch above this line

    # This challenge was deceptively hard. I'll break down why and how I solved it.
    # It was hard because we are using a method inside the Dragon Class instance that loops over all the Dragon Class instances in a list
    # and then we come outside of the class into the main function to create some logic to make each dragon shoot at eachother but
    # they can not hit themselves. Sounded super easy until I begain. 

    for dragon in dragons:
        describe(dragon)


    # I have to loop through the dragons list that we have, create a copy of that list and delete the list object at the counter 
    # increment starting at index 0 then increment the counter += 1, i guess I could probably increment at the end of the for loop as well
    # just as long as i create a copy of the dragons list and delete the counter index before using the .breathe_fire method again.

    counter = 0
    for dragon in dragons:
        attack_list = dragons.copy()
        del attack_list[counter]
        dragon.breathe_fire(3, 3, attack_list)
        counter += 1

    # this took me forever to figure out for some reason, but the simpliest problems always feel the hardest i guess.

# don't touch below this line


def describe(dragon):
    print(f"{dragon.name} is at {dragon.pos_x}/{dragon.pos_y}")


class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        print(f"{self.name} breathes fire at {x}/{y} with range {self.__fire_range}")
        print("====================================")
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                print(f"{unit.name} is hit by the fire")


main()
