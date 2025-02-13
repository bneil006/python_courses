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
        ) # simply returns True or False based on the Unit instance variables for pos_x and pos_y if they fall within the 4 parameters essentially on all cases than True else False


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        units_hit = []
        for unit in units:
            # here we are looping over our Unit Class instances and running the method in_area(self, x_1, y_1, x_2, y_2) over them, we also assigned this to a variable
            # for our if statement on the next lines and then we simply leave the forloop and return the full list once we are finished with the loop and logic.
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range
            )
            if in_area:
                units_hit.append(unit.name)
        return units_hit
            

def main():
    dragons = [Dragon("Draco", 2, 2, 3), Dragon("Fafnir", 1, 1, 1), Dragon("Hydra", 0, 0, 2), Dragon("Smaug", 6, 6, 2)]
    fire_breath_at = [(2, 3), (1, 1), (0, 1), (1, 1)]


    enemies = [
        [Unit("Cian", 3, 3), Unit("Andrew", -1, 4), Unit("Baran", -6, 5)],
        [Unit("Carbry", 2, 1), Unit("Yvor", 1, 0), Unit("Eoin", 2, 0), Unit("Edwin", 10, 10)],
        [Unit("Nicholas", 0, 1), Unit("Andrew", -1, 4), Unit("Baran", -6, 5)],
        [Unit("Yvor", 1, 0), Unit("Nicholas", 0, 1), Unit("Eoin", 2, 0), Unit("Cian", 3, 3), Unit("Andrew", -1, 4), Unit("Baran", -6, 5), Unit("Carbry", 2, 1)]
        ]
    
    count = 0
    for dragon in dragons:
        print(dragon.breathe_fire(fire_breath_at[count][0], fire_breath_at[count][0], enemies[count]))
        count += 1

    # Wow this one was tricky, I got myself confused because i kept thinking that the dragon position x, y was where we were shooting our breath from but realized
    # after some time that boot.dev was testing on shooting from a different position than the x, y of the drake, that the breathe_fire method was passed
    # the x, y of where they wanted fire shot / centered at
    # after realizing this i was able to make the changes needed to figure this out.

main()