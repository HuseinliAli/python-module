def even_or_odd(number:int) -> str: 
    return "odd" if number % 2 == 1 else "even"

def check_number_is_prime(number:int) -> bool:
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def multipy_numbers(*numbers) -> int:
    if len(numbers) == 0:
        return 0
    result = 1
    for number in numbers:
        result *= number
    return result

def upper_and_lower_count(string:str) -> str:
    low_count = 0
    up_count = 0
      
    for i in string:
        if i.islower():
            low_count += 1
        if i.isupper():
            up_count += 1
            
    return f"No. of Upper case characters : {up_count}\nNo. of Lower case Characters : {low_count}"

def square_of_numbers(start:int, end:int) -> list:
    result = []
    for i in range(start, end+1):
        result.append(i**2)
    return result

def is_armstrong(number:int) -> bool:
    digit_count = 0
    temp_for_count = number
    temp_for_armstrong = number
    sum = 0
    
    while temp_for_count > 0:
        temp_for_count = int(temp_for_count/10)
        digit_count+=1
    
    while temp_for_armstrong > 0:
        digit = temp_for_armstrong % 10
        sum += digit ** digit_count
        temp_for_armstrong = int(temp_for_armstrong/10)
    
    return number == sum

def digits_sum(number:int)->int:
    digits = [int(digit) for digit in str(number)]
    return sum(digits)
    
def num_divisors(number:int) -> list:
    result = []
    for i in range(1,number+1):
        if number % i == 0:
            result.append(i)
    return result

def fuel_cost(distance: float, km: float = 50, fuel_cost: float = 1) -> float:
    return (distance / km) * fuel_cost

def hcf(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
print("task 1 starting...")
print(even_or_odd(100))
print("task 1 done.\n")

print("task 2 starting...")
print(check_number_is_prime(17))
print("task 2 done.\n")

print("task 3 starting...")
print(multipy_numbers(8,2,3,7,-1))
print("task 3 done.\n")

print("task 4 starting...")
print(upper_and_lower_count("Ali Huseynli"))
print("task 4 done.\n")

print("task 5 starting...")
print(square_of_numbers(3, 5))
print("task 5 done.\n")

print("task 6 starting...")
print(is_armstrong(154))
print("task 6 done.\n")

print("task 7 starting...")
print(digits_sum(164))
print("task 7 done.\n")

print("task 8 starting...")
print(num_divisors(24))
print("task 8 done.\n")

print("task 9 starting...")
print(fuel_cost(50,20,2))
print("task 9 done.\n")

print("task 10 starting...")
print(hcf(50,20))
print("task 10 done.\n")