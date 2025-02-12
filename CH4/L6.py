class RealEstate:
    def __init__(self, location):
        self.__location = location

    def get_location(self):
        return self.__location


class Residential(RealEstate):
    def __init__(self, location, bedrooms):
        super().__init__(location)
        self.__bedrooms = bedrooms
    
    def get_bedrooms(self):
        return self.__bedrooms


class House(Residential):
    def __init__(self, location, bedrooms, yard_size):
        super().__init__(location, bedrooms)
        self.__yard_size = yard_size
    
    def get_yard_size(self):
        return self.__yard_size


def main():
    # using inheritance we have to still use getter methods in each parent to gather private variable information.
    random_house = House("Town", 5, 540)
    print(f"House located in: {random_house.get_location()}. It has {random_house.get_bedrooms()} bedrooms and {random_house.get_yard_size()} feet of yard.")



main()