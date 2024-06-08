import sys


def create_person(name:str, age:int) -> str:
    return f"{name} is {age} years old."

print(create_person("Ali",10))

def sum_def(num1, *nums):
    return sum(nums)+num1
print(sum_def(1,2,3,4,5,6))
sample= {" "}
print(sample)


list1 = [1, 2, 3, 4, 5, 6, 7]
print(list1[-3:6])

dict1 = {"ali":"1","beli":"2"}
dict2 = dict(dict1)




def even_or_odd(number):
    return "odd" if number % 2 == 1 else "even"

def sum_task(*nums):
    return sum(nums)

def avg_task(nums):
    return sum(nums) / len(nums)

def upper_task(parameter):
    return parameter.upper()


def min_and_max(nums):
    min = sys.maxsize
    max = sys.maxsize * (-1) -1
    for i in nums:
        if(i > max):
            max = i
        if(i < min):
            min = i
    return min , max

print(min_and_max([10,20,30,40,50]))
print(even_or_odd(20))
print(sum_task(20,40,50,60,70))
print(avg_task([10,20,40,50]))
print(upper_task("askdklasdklasld"))