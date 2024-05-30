import math
def char_list_to_string(char_list):
    result = ""
    for char in char_list:
        result+=char
    return result

def area_of_circle(radius):
    return math.pi * math.pow(radius, 2)

def square_of_elements_of_array(elements):
    result = []
    for element in elements:
        result.append(math.pow(float(element),2))
    return result

def find_largest_number(elements):
    sorted_elements = sorted(elements,reverse=True)
    result = ''.join(sorted_elements).split(' ')
    return int(result[0])

def cumulative_sum(elements):
    result = []
    sum = 0
    for element in elements:
        sum += element
        result.append(sum)
    return result

#task 1
print("task 1 starting...")
print(char_list_to_string(['a','b','c','d']))
print("task 1 done.\n")


#task 2
print("task 2 starting...")
task_2_input =float(input('enter radius of area: '))
print(area_of_circle(task_2_input))
print("task 2 done.\n")


#task 3
print("task 3 starting...")
task_3_inputs = []
for i in range(3):
    task_3_inputs.append(input(f"enter {i+1}. element of array: "))
print(find_largest_number(task_3_inputs))
print("task 3 done.\n")


#task 4
print("task 4 starting...")
task_4_input = input('enter elements of list with spaces: ')
print(square_of_elements_of_array(task_4_input.split(' ')))
print("task 4 done.\n")


#task 5
print("task 5 starting...")
task_5_input = [1,2,3,4,5,6,7,8,9,10]
print(f"input: {task_5_input}")
print(f"output: {cumulative_sum(task_5_input)}")
print("task 5 done.\n")