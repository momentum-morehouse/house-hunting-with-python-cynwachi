annual_salary = float("What is your annual Salary ")

total_cost = float(input("what is the cost of the dream home "))

print(total_cost)

downpayment = 0.25* total_cost 
portion_saved =float(input("how much do you want to save each month"))


def how_long_money_needed(downpayment, total_cost, salary, po):
    current_savings= 0 
    # each month takes current savings and add earned interest and salary saved
    while current_savings < downpayment:
        current_savings = current_savings + salary * portion_saved / 12 + current_savings* 0.04 / 12
    #stop when the amont of savings is equal to the downpayment 
    # count the number of months that pass 
    return months
    
