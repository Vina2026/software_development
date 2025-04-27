"""
Neven Said
"""

import math

print ("\n ------ Example 3: Function that doesn't return values  ------")
def greeting():
    print ("welcome to functions!")



print ("\n ------ Example 4: Function with parameter 'username'  ------")
def printusername (username):
    print (f"welcome to function {username}")



print ("\n ------ Example 5: Function with default parameters   ------")
def user_country(username = "(no name)", country ="USA"):
    print (f"{username} is living in {country}")


print ("\n ------ Example 6: Function that returns a value   ------")
def product(n1=1, n2=1):
    return n1*n2



print ("\n ------ Example 7: Boolean function   ------")
def multiple3(n):
    if n%3 == 0 and n!=0:
        return True
    else:
        return False



print ("\n ------ Example 8: compostion function   ------")
def collectnum():
    n = float(input("Enter a number between 1 and 9 (inclusive)"))
    while not (1 <= n <=9):
        n = float (input("Re-enter a number agin: "))
    return n


def sumnumbers(totalnumbers):
    sum = 0
    for n in range (totalnumbers):
        sum += collectnum()
    return sum


def print_result(totalsum):
    print (f"Sum of all numbers is = {totalsum}")



print ("\n ------ Example 9: built-in Function  ------")
def areacircle(radius):
    a = math.pow(radius,2) * math.pi
    return round(a, 2)

def areaprint(area, radius = 0):
    print (f"the area of the circle with {radius} radius is {area}")


print ("\n ------ Example 10: Function to return the ratio of two numbers ------")
def ratio_hour(hour):
    try:
        dayhour = 24 
        r = hour/dayhour
    except ZeroDivisionError:
        print(f"Zero Exception")
        return 0
    except ZeroDivisionError:
        print(f"Value Exception")
        return 0
    except:
        print("General Exception")
    else:
        return r
    finally:
        print("Process Completed!")



print ("\n ------ Example 11: classes ------")
class Myclass:
    id = 12345

    def msg(self):
        return "welcome to python class"



print ("\n ------ Example 12: instantiation classes ------")
class Complexnumber():
    def __init__(self, realnumber, imgnumber):
        self.r = realnumber
        self.i = imgnumber
    


print ("\n ------ Example 13: classes application ------")
class Car:
    def __init__(self, make, model, year):
        self.carmake = make
        self.carmodel = model
        self.caryear = year

    odometer_reading = 0
    
    def get_car_description(self):
        return f"{self.carmake} with model {self.carmodel} was made on {self.caryear}"
    
    def read_odometer(self):
        return f"this car has {self.odometer_reading} miles on it"
    
    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('odometer cant roll back')
            
            
    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("can't add negative miles")
        