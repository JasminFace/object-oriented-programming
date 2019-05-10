class Cat:
    """ A class representing cats """

    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.food = preferred_food
        self.time = meal_time

    def __str__(self):
        return f"Name: {self.name} Preferred food: {self.food} Usual meal time: {self.time}"

muca = Cat("Muca", "dry food", 8)
chava = Cat("Chava", "whatever you're eating", 14)

print(muca)
print(chava)