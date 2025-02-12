class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows
    
def main():
    brandon = Archer("Brandon", 10)
    random_human = Human("Jal")

    print(brandon.get_name()) # using our parent class method here in our child -- wooooo inheritance!
    print(brandon.get_num_arrows())

    print(random_human.get_name()) # parent Human only has a single method thus we can't get the num_arrows method - super cool
    

main()
