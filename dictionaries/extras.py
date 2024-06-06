def print_people_dict(people):
    for key,value in people.items():
        result = f"{key}. {value['first_name']} {value['last_name']} {value['age']} {value['city']}"
        print(result)
def print_numbers_dict(numbers):
    for key,value in numbers.items():
        result = f"{key}. {value['person']['first_name']} {value['person']['last_name']} {value['number']}"
        print(result)

def print_recap(dict):
    index = 1
    for i, j in dict.items():
        print(f"{index}.{i}\n {j}\n\n")
        index+=1
#exercise 1
#task 1.1
cities_dict = {1:"Baku",2:"Ganja",3:"Sumgayit",4:"Lankaran"}
people_dict = {
    1:{"first_name":"Ali","last_name":"Huseynli","age":19,"city":cities_dict[1]},
    2:{"first_name":"Elmir","last_name":"Mikayilli","age":19,"city":cities_dict[2]},
    3:{"first_name":"Nihat","last_name":"Alizade","age":19,"city":cities_dict[3]},
    }
print("task 1.1 starting")
print_people_dict(people_dict)
print("task 1.1 done.\n")

#task 1.2
phone_numbers = {
    1:{"person":people_dict[1],"number":"+994-55-555-55-51"},
    2:{"person":people_dict[2],"number":"+994-55-555-55-52"},
    3:{"person":people_dict[3],"number":"+994-55-555-55-55"},
}
print("task 1.2 starting")
print_numbers_dict(phone_numbers)
print("task 1.2 done.\n")

#task 1.3
recap_dict = {
    "for":"iterate something",
    "if":"conditional statement",
    "dictionary":"contains key value pair",
    "del":"deletes variable",
    "function":"execute little business rules"}

print_recap(recap_dict)

#exercise 2
#task 2.1
programming_languages_dict = {
    1:"Python",
    2:"C#",
    3:"C++",
    4:"Java",
    5:"JavaScript",
    6:"Dart"
}

programming_languages_people_dict = {
    1:{"person":people_dict[1],"favorites":[programming_languages_dict[1],programming_languages_dict[2],programming_languages_dict[4]]},
    2:{"person":people_dict[2],"favorites":[programming_languages_dict[4],programming_languages_dict[3],programming_languages_dict[5]]},
    3:{"person":people_dict[3],"favorites":[programming_languages_dict[2],programming_languages_dict[1],programming_languages_dict[6]]}
}

print("task 2.1 starting...")
for key, value in programming_languages_people_dict.items():
    print(f"{value['person']['first_name']} {value['person']['last_name']} - {value['favorites']}")
print("task 2.1 done\n")
pets_dict = {
    1:"dog",
    2:"pig",
    3:"mouse",
    4:"cat"
}

pet_and_owners_dict = {
    1:{"pets":[pets_dict[1],pets_dict[2]],"owner":people_dict[1]},
    2:{"pets":[pets_dict[2],pets_dict[1]],"owner":people_dict[2]},
    3:{"pets":[pets_dict[3],pets_dict[4]],"owner":people_dict[3]}
}

print("task 2.2 starting...")
for key, value in pet_and_owners_dict.items():
    print(f"{value['owner']['first_name']} {value['owner']['last_name']} - {value['pets']}")
print("task 2.2 done\n")

favorite_cities_dict = {
    'paris': {
        'country': 'France',
        'population': 2148000,
        'fact': 'Known as the City of Light.'
    },
    'istanbul': {
        'country': 'Turkiye',
        'population': 17398000,
        'fact': 'In past this city called as Constantinopol.'
    },
    'tokyo': {
        'country': 'Japan',
        'population': 9273000,
        'fact': 'Largest metropolitan area in the world.'
    }
}
print("task 2.3 starting...")
for key, value in favorite_cities_dict.items():
    print(f"{key.title()}, {value['country'].title()} {value['population']} {value['fact'].title()}")

print("task 2.3 done")