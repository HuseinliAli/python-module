class Creature:
    def __init__(self, paw_count, height, age):
        self.paw_count = paw_count
        self.height = height
        self.age = age
        
    def move(self, name):
        print(f"{name} is moving now")