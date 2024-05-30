name = "ali"
age = 3
global x

x = 10

#python-da dəyişən adları digər dillərdə olduğu kimidir.
#global dəyişən təyin etdiyimiz anda default dəyər set etmək mümkün deyildir.
#numberic => int float complex
#boolean type => bool
#binary types => bytes bytearrray memoryview
#none type => NonteType
a = "name"


#dəyişən adları necə istifadə etmək olar.

a = 1

b = [10,20,30]
x = -5
print(~x)
#ən yuxarıda import etmək lazımdır.





number = int(input())
length = len(str(number))
sum = 0
temp = number

while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10

print(number == sum)





