# Input data
salary = [10000, 12000, 15000, 17500, 20000]
service = [12, 6, 10, 3, 5]

# Function to calculate bonus and new salary for each employee
def calculate_bonus_and_salary(emp_number, present_salary, years_of_service):
    if years_of_service > 10:
        bonus_percentage = 12
    elif 6 <= years_of_service <= 10:
        bonus_percentage = 9
    elif years_of_service >= 4:
        bonus_percentage = 5
    else:
        bonus_percentage = 0

    bonus_amount = (bonus_percentage / 100) * present_salary
    new_salary = present_salary + bonus_amount
    percentage_hike = (bonus_amount / present_salary) * 100

    # Output formatted statement
    print(f"Salary Statement For Employee {emp_number + 1}:\n"
          f" Present Salary: Rs. {present_salary}\n"
          f" Service Period: {years_of_service} Years\n"
          f" Eligible Percentage of Bonus: {bonus_percentage} %\n"
          f" Eligible Amount of Bonus: Rs. {bonus_amount}\n"
          f" New Salary: Rs. {new_salary}\n"
          f" Percentage Hike in Salary: {percentage_hike} %\n")

# Generate salary statements for each employee
for i in range(len(salary)):
    calculate_bonus_and_salary(i, salary[i], service[i])
