# Defining Robot class
class Robot:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    # method for introducing robot
    def introduce(self):
        print(f"Hello! I am {self.name}.")
        print(f"I am a {self.model} created in {self.year}.")
        print("I'm here to assist you with any tasks you need help with!")

my_robot = Robot(name="Jekyll", model="X3000", year=2024)

# Cal the introduce method to introduce robot
my_robot.introduce()