#Write a python script that will calculate how many months it will take to save enough money for a down payment
#Ask for input = Variables annual_salary, portion_saved, total_cost,
#Print output = annual_salary, portion_saved (.15), total_cost

"""
- Retrieve user input. Look at `input()` if you need help with getting user input. For this problem set, you can assume that users will enter valid input (e.g. they won’t enter a string when you expect a number.)
- Initialize some state variables. You should decide what information you need. Be careful about values that represent annual amounts and those that represent monthly amounts.
- Try different inputs and see how long it takes to save for a down payment.
    
"""
annual_salary = input("Enter Your Annual Salary: ")

portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
monthly_salary_saved = (float(annual_salary)/12)*float(portion_saved)
total_cost = input("Enter the cost of your dream home: ")

portion_down_payment = 0.25 * float(total_cost)
current_savings = 0

i = 0
#when i use i=0 test 1 is off by one month and test 2 is correct
#when i use i=1 test 1 is correct and test 2 is off by one month

while current_savings < portion_down_payment:
    current_savings += monthly_salary_saved
    investment_return = current_savings * (.04/12)
    current_savings += investment_return
    i+=1


print("Number of months: ", i)
# print("It will take you", i, "months to save up enough money for a down payment!") 
#=> total_cost = Cost of Home

#=> portion_down_payment = Portion of cost needed for downpayment (=0.25/25%)
#=> current_savings = Amount saved so far 
# Current savings starts with = 0

# Annual 'r' "Annual Rate" = 0.04/4% 
# At the end of each month I receive an addtional => current_savings*r/12 see last line for formula 




#=> annual_salary = annual salary

#portion_saved in decimal form  




#=> At the end of each month my savings will increase by the return on my investment ((current_savings*0.04)/12)




#=> W
