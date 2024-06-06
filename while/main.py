number = int(input("enter number: "))
result = 1
temp = number
string = ""
while temp > 0:
    string +=f"{temp}"
    if(temp != 1):
        string +="*"
    result *= (temp) 
    temp-=1

string += f" = {result}" 
print(string)