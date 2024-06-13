from creature import Creature
class Person(Creature):
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def print_human(self):
        print(f"{self.last_name} {self.first_name} {self.age}")
        
    def move(self, name):
        super().move(name)
        
    class Nested:
        def __init__(self) -> None:
            print("hello")
