def sum_two_dictionaries(dict1, dict2):
    for key, value in dict2.items():
        if(key in dict1):
            sum = dict1[key] + value
            dict1.update({key : sum})  
        else:
            dict1.update({key : value})
    return dict1
def create_dicrionary():
    return {}
def print_dict(dictionary):
    for i, j in dictionary.items():
        print(f"{i} - {j}")
def remove_by_key(dictionary, key):
    dictionary.pop(key)
    return dictionary
def sort_dict(dictionary):
    return dict(sorted(dictionary.items()))
def update_by_key(dictionary, new_data):
    dictionary.update(new_data)
    return dictionary
def print_all_values(dictionary):
    return dictionary.values()
def basket_sum(dictinary):
    sum = 0
    for i in dictinary.values():
        sum+=i
    return sum
def discount(dictionary):
    discount_count = 0.9
    for i,j in dictionary.items():
        dictionary.update({i: j*discount_count})
    return dictionary
#task 1
dict1_for_task_1 = {'a':100,'b':1000,'c':300}
dict2_for_task_1 = {'a':100,'d':8000,'e':500}
print(sum_two_dictionaries(dict1_for_task_1,dict2_for_task_1))
#task 2
print(type(create_dicrionary()))

#task 3
print_dict({1:"Ali",2:"Nihat",3:"Elmir"})

#task 4
print(remove_by_key({'name':'ali','age':10},'age'))

#task 5
print(sort_dict({"b":900,"a":1000,"c":200}))

#task 6
print(update_by_key({'Alice': 85, 'Bob': 90},{'Alice':95}))

#task 7
print(print_all_values({'Alice': 85, 'Bob': 90}))

#task 8
item_prices = {'apple': 1.00, 'banana': 0.50}
print(basket_sum(item_prices))
print(discount(item_prices))