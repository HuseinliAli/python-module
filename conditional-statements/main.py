def mutate_string(string, position, character):
    listed_string = list(string)
    for i in range(len(string)):
        if(i == position):
            listed_string.pop(i)
            listed_string.insert(position,character)
    return ''.join(listed_string)

print(mutate_string('abracadabra',5,'k'))

def swap_case(s):
    listed_string = list(s)
    swapped_list = []
    for char in listed_string:
        if(char.islower()):
            char = char.upper()
        else:
            char = char.lower() 
        swapped_list.append(char)
        
    return ''.join(swapped_list)

print(swap_case('Swap Case 2'))

def solve(s):
    splitted_string = s.split()
    result_list = []
    for string in splitted_string:
        result_list.append(string.title())
    return ' '.join(result_list)

def login(username, password):
    if(len(username)<5):
        print("username is too short")

    for char in password:
        if(char.isdigit() != True):
           print("password doesnt contains number")
           break
    
    if(len(username)>=5 and len(password)>8):
        print("login successfuly")

#login("ali1234","password1")









def dicount_app(price):
    if(price >=500 and price<1000):
        price *=0.9
    elif(price >=1000):
        price *=0.85
    elif(price <100):
        price +=10
    return price

print(dicount_app(60))

