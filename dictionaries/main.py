cars_dic = {
    "99-EE-999":{"model":"Mustang","brand":"Ford","year":1964},
    "99-EE-998":{"model":"Mustang","brand":"Ford","year":1965}
}

print(cars_dic["99-EE-998"])

for i in cars_dic.keys():
    if('99-EE-999'==i):
        print("bu key momvcuddu qaqa")
count = 0
for i in cars_dic.values():
    
    if(i["brand"] == 'Ford'):
        count+=1

print(count)

users_dict = {
    1:{"first_name":"Ali","last_name":"Huseynli","password":"ali1234"},
    2:{"first_name":"Nihat","last_name":"Aliyev","password":"naliyev1234"},
    3:{"first_name":"Elmir","last_name":"Mikayilli","password":"elmirmikayil1234"},
}

id = int(input("enter user id: "))

if(id in users_dict.keys()):
    print(f"{users_dict[id]['first_name']} {users_dict[id]['last_name']}")
else:
    print(f"{id} nomreli istifadeci sistemde tapilmadi")

for i in users_dict:
    print(i)

for i in users_dict:
    print(users_dict[i])

for i in users_dict.values():
    print(i)

for i, j in users_dict.items():
    print(f"{i}. {j['first_name']} {j['last_name']}")

new_users_dict = dict(users_dict)
print(new_users_dict)