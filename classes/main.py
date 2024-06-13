from person import Person
from creature import Creature
from practise import Practise
person_1 = Person("Ali","Huseynli",20)
person_1.print_human()
person_1.move(person_1.first_name)
person_1.Nested()
print(issubclass(Person, Creature))

solution = Practise(1,2,"SELAM DUNYA")

print(solution.sum_two_nums())
solution.print_message()

print(solution.sum_of_list([10,20,30,40]))

print(solution.avg_of_list([10,20,30,40]))

print(solution.numbers)