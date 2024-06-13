from person import Person
from creature import Creature
person_1 = Person("Ali","Huseynli",20)
person_1.print_human()
person_1.move(person_1.first_name)
person_1.Nested()
print(issubclass(Person, Creature))