'''
Program: function_return_value.py
Author: Joshua M McGinley
Last Date Modified: 09/21/2022

This program involves a function (hourly_employee_input) calling another function (weekly_pay) which returns the
calculation (total) for a weeks pay. It then returns a string of name + (salary) that weeks pay.

Open the editor of your choice. Make a copy of your .py file containing the function called hourly_employee_input
that asks the user for a name (string), hours worked (int) and an hourly pay rate (float) and prints a string
including the information. Write a function weekly_pay that accepts in the parameter list the hours_worked and
hourly_pay_rate and returns the calculated weekly pay.

    Make a function call in hourly_employee_input
    Change the string in hourly_employee_input  to print name and weekly pay
    Change the hourly_employee_input instead of printing, return a statement and print the result in the main

Include a docstring as your first line declaring what the function does.
'''
#Function that returns string
def hourly_employee_input():
    '''a function that takes name as input then calls weekly_pay function stores it as salary. It then returns name
    and salary as the string name_salary.'''
    name = str(input('Enter name: '))
    salary = weekly_pay()
    name_salary = name + " " + str(salary)
    return name_salary

#Function that returns total of hrs_worked times hr_rate
def weekly_pay():
    '''a function that takes hrs_worked (int) times hr_rate (float) and stores them in total. It then returns total.
    '''
    try:
        hrs_worked = int(input('Enter hours worked: '))
    except:
        print('Evil input!')
    try:
        hr_rate = float(input('Enter hourly pay rate: '))
    except:
        print('Evil input!')
    total = hrs_worked * hr_rate
    return total

#driver code
if __name__ =="__main__":
    statement = hourly_employee_input()

print(statement)
