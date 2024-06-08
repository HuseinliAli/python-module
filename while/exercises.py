import math
import sys


def sum_of_values(dictionary):
    values_list = list(dictionary.values())
    sum_of_sample_dict = 0
    count = len(dictionary)
    index = 0
    while(count>0):
        sum_of_sample_dict += values_list[index]
        index += 1
        count -= 1
    print(sum_of_sample_dict)
def min_value_of_dict(dictionary):
    items = list(dictionary.items())
    count = len(items)
    min_value = sys.maxsize
    min_value_of_key = ""
    index = 0
    while(count>0):
        key, value = items[index]
        if value < min_value:
            min_value = value
            min_value_of_key = key
        index += 1
        count -= 1
    return min_value_of_key.title()
def delete_keys(dictionary, remove_key_list):
    for key in remove_key_list:
        if key in dictionary:
            del dictionary[key]
    return dictionary

def extract_dictionary_by_keys(dictionary, keys):
    extracted_dict = {}
    for key, value in dictionary.items():
        if(key in keys):
            extracted_dict.update({key : value})
    return extracted_dict
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

keys_list = list(sample_dict.keys())
print(keys_list)
print("task 1 done.\n")
#task 2
sum_of_values(sample_dict)
print("task 2 done.\n")

#task 3
print(min_value_of_dict(sample_dict))
print("task 3 done.\n")

#task 4
#print(delete_keys(sample_dict, ["Physics","Math"]))
print("task 4 done.\n")

#task 5
print(extract_dictionary_by_keys(sample_dict, ["history"]))
print("task 5 done.\n")

#task 6
nums = []
count_in_task_6 = 1
count_of_inputs = 10
temp_in_task_6 = count_of_inputs
while temp_in_task_6 > 0:
    nums.append(int(input(f"enter {count_in_task_6}. input: ")))
    count_in_task_6 += 1
    temp_in_task_6 -= 1

avarage = sum(nums) / count_of_inputs
print(avarage)

#task 8
number = int(input("enter number: "))
result = 1
temp_in_task_8 = number
string = ""
while temp_in_task_8 > 0:
    string +=f"{temp_in_task_8}"
    if(temp_in_task_8 != 1):
        string +="*"
    result *= (temp_in_task_8) 
    temp_in_task_8 -= 1

string += f" = {result}" 
print(string)

#task 9
number_in_task_9 = int(input("enter number: "))
temp_in_task_9 = number_in_task_9
sum_in_task_9 = 0
while(temp_in_task_9 > 0):
    digit = temp_in_task_9%10
    sum_in_task_9 += digit
    temp_in_task_9 = int(temp_in_task_9 / 10)
print(sum_in_task_9)

#task 10
input_str = input("enter string: ")
count_in_task_10 = len(input_str)
print(len(count_in_task_10))