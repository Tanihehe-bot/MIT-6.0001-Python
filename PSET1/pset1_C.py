#In Part B, you had a chance to explore how both the percentage of your salary that you save each month  and your annual raise affect how long it takes you to save for a down payment. This is nice, but suppose you want to set a particular goal, e.g. to be able to afford the down payment in three years.
# How much should you save each month to achieve this?  In this problem, you are going to write a program to answer that question. To simplify things, assume:
# 1. Your semi­annual raise is .07 (7%)
# 2. Your investments have an annual return of 0.04 (4%)  
# 3. The down payment is 0.25 (25%) of the cost of the house 
# 4. The cost of the house that you are saving for is $1M.
# You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of the required down payment.  
# In ps1c.py, write a program to calculate the best savings rate, as a function of your starting salary. You should use bisection search to help you do this efficiently. You should keep track of the number of steps it takes your bisections search to finish. You should be able to reuse some of the code you wrote for part B in this problem. 

starting_salary = int(input("Enter the starting salary: "))

r = 0.04
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
months = 36

down_payment = total_cost * portion_down_payment

low = 0
high = 10000
steps = 0

guess = (low + high) // 2
portion_saved = guess / 10000

current_savings = 0

while abs(current_savings - down_payment) > 100:
    guess = (low + high) // 2
    portion_saved = guess/10000
    current_savings = 0
    annual_salary = starting_salary
    for month in range(1, 37):
        monthly_savings = (annual_salary / 12) * portion_saved
        investment_return = current_savings * (r / 12)
        current_savings += monthly_savings + investment_return

        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise

    if current_savings < down_payment:
        low = guess
    else:
        high = guess
    
    steps += 1

print(f"Best savings rate: {portion_saved}")
print(f"Steps in bisection search: {steps}")