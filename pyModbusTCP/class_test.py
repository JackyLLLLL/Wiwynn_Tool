class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def __repr__(self):
        return f"{self.name} 是一隻 {self.species}"
    def make_noice(self, noice):
        print(f"動物會發出 {noice} 的聲音")


class Cat(Animal):
    def __init__(self, name, species,breed, toy):
        self.name = name
        self.species = species
        self.breed = breed
        self.toy =toy

ball = Cat("小球","貓","波斯", "老鼠")
print(ball)