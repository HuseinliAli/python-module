#from exercises import multipy_numbers as multp
from exercises import multipy_numbers, even_or_odd
from loops.main import area_of_circle
result = multipy_numbers(1,2,3,4,5,6,7,7,8,9,0)
print(result)

def test_function(first_name,last_name,**others):
    return others

print(test_function(1,3,age=10,city="baku"))
print(even_or_odd(1))