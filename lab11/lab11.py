"""
Neven Said 
"""

import math
from lab11_functions import *


print ('\n ------ Example 1: python dictionary  ------')
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
print (car)

print (f"the year of the car is = {car['year']}")

car["year"] = 1980
print (f"the year of the car was updated to = {car['year']}")

car["color"] = "red"
print (car)

print("\n loop through each key in the dictionary")
for k in car:
    print(k)

print("\n loop through each value in the dictionary")
for k in car:
    print(car[k])

print("\n loop through each pair in the dictionary")
for k in car:
    print(f"{k} has value = {car[k]}")



print ('\n ------ Example 2: python dictionary application  ------')
phase = "to be or not to be"
print (f"original phase = {phase}")

phase_split = phase.split()
print (f"splitted phase = {phase_split}")

word_count_dict = {}
for word in phase_split:
    if word in word_count_dict:
        word_count_dict[word] +=1
    else:
        word_count_dict[word] =1
print ("result of dictionary: ")

for w in word_count_dict:
    print (f"{w} = {word_count_dict[w]} in the list")



print ("\n ------ Example 3: Function that doesn't return values  ------")
greeting()



print ("\n ------ Example 4: Function with parameter 'username'  ------")
printusername(10)
printusername("peter pan")



print ("\n ------ Example 5: Function with default parameters   ------")
user_country("Neven", "Egypt")
user_country("", "France")
user_country()
user_country('Neven')



print ("\n ------ Example 6: Function that returns a value   ------")

num1 = 2
num2 = -6

product1 = product(num1, num2)
print(f"The product of {num1} and {num2} is {product1}")

product1 = product(num1)  
print(f"The product is {product1}")

product1 = product()  
print(f"The product is {product1}")



print ("\n ------ Example 7: Boolean function   ------")
checknum1 = multiple3(10)
checknum2 = multiple3(-6)
print(f" is {num1} multiple of 3? {checknum1}")
print(f" is {num2} multiple of 3? {checknum2}")



print ("\n ------ Example 8: compostion function   ------")
number = collectnum()
print(number)

sumall = sumnumbers(3)
print(sumall)



print ("\n ------ Example 9: built-in Function  ------")
r = 2
a = areacircle(r)
areaprint(a,r)



print ("\n ------ Example 10: Function to return the ratio of two numbers ------")
ratio = ratio_hour(0)
r2 = ratio_hour(3)
r3 = ratio_hour("peter")



print ("\n ------ Example 11: classes ------")
user1 = Myclass()
print (f"an instance of the class = {user1}")

userid = user1.id
print (f"user 1 id = {userid}")

user1msg = user1.msg()
print (f"user 1 message = {user1msg}")



print ("\n ------ Example 12: instantiation classes ------")
paircomplexnumber = Complexnumber(2,3)
real = paircomplexnumber.r
print(f"the real part is {real}")



print ("\n ------ Example 13: classes application ------")
car1 = Car("Tesla", "S", 2023)
car_reading = car1.odometer_reading
print(f"car miles reading = {car_reading}")

print (car1.get_car_description())

print (car1.read_odometer())

car1.update_odometer(10)
print(car1.read_odometer())

car1.update_odometer(5)
print(car1.read_odometer())


car1.increment_odometer(20)
print(car1.read_odometer())

car1.increment_odometer(-5)
print(car1.read_odometer())

car1.increment_odometer(8)
print(car1.read_odometer())
