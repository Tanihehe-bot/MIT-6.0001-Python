#Write a program that does the following in order: 
# 1. Asks the user to enter a number “x” 
# 2. Asks the user to enter a number “y”  
# 3. Prints out number “x”, raised to the power “y”. 
# 4. Prints out the log (base 2) of “x”. 

import math 

x = int(input("Please enter a number 'x': "))
y = int(input("Please enter a number 'y': "))

raised = x**y
print(f"x**y = {raised}")

log_x = math.log2(x)
print(f"log(x) = {log_x}")