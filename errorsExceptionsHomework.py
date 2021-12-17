'''    
for i in ['a','b','c']:
    try:
        print(i**2)
    except TypeError:
        print(f"Cannot ** between string {i} and integer 2!")
'''
'''
from typing import final


x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("All Done!")
'''

def ask():
    while True:
        try:
            number = int(input("Please enter a number: "))
        except:
            print("Invalid entry! Please use only numbers!")
            continue
        else:
            print(f"Thank you! You're number squared is", number**2,".")
            break
        
ask()