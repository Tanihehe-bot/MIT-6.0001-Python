#In ps1b.py, copy your solution to Part A (as we are going to reuse much of that machinery).  Modify your program to include the following
# 1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
# 2. After the 6th month, increase your salary by that percentage.  Do the same after the 12th month, the 18th month, and so on. 

# Write a program to calculate how many months it will take you save up enough money for a down payment.  LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%).  Have the user enter the following variables:
# 1. The starting annual salary (annual_salary)
# 2. The percentage of salary to be saved (portion_saved)
# 3. The cost of your dream home (total_cost)
# 4. The semi­annual salary raise (semi_annual_raise)

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi-annual salary raise, as a decimal: "))

months = 0
current_savings = 0
portion_down_payment = 0.25
r = 0.04

down_payment = total_cost * portion_down_payment
monthly_savings = (annual_salary/12)*portion_saved

while current_savings < down_payment:
    investment_return = current_savings * (r/12)
    current_savings += monthly_savings + investment_return
    months += 1
    if months % 6 == 0:
        annual_salary = annual_salary + (annual_salary*semi_annual_raise)
        monthly_savings = (annual_salary/12)*portion_saved

print(f"Number of months: {months}")