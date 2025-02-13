class Siege:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, food_price):
        return (distance / self.efficiency) * food_price

    def get_cargo_volume(self):
        pass # empty for Siege but the child classes will override and use this method


class BatteringRam(Siege):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        super().__init__(max_speed, efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area

    def get_trip_cost(self, distance, food_price):
        return (distance / self.efficiency) * food_price + (self.load_weight * 0.01)

    def get_cargo_volume(self):
        return self.bed_area * 2


class Catapult(Siege):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().__init__(max_speed, efficiency)
        self.cargo_volume = cargo_volume

    def get_cargo_volume(self):
        return self.cargo_volume


def main():
    list_of_distances = [125, 50, 10, 100]
    list_of_food_price = [2, 8, 3, 20]
    list_of_equipment = [Siege(100, 10), BatteringRam(100, 10, 200, 5)]

    counter = 0
    for distance in list_of_distances:
        for equipment in list_of_equipment:
            print(f"TRIP COST: {equipment.get_trip_cost(distance, list_of_food_price[counter])}")

    

main()