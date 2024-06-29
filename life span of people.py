"""
Calculating the life span of people based on hypothetical equation
"""

#enter details of user (name, age, lenght, weight) 
name = input("Enter your name: ")
age = int(input("Enter your age(years only): "))
lenght = int(input("Enter your lenght in cm: "))
weight = int(input("Enter your weight in Kg: "))

#calculate of final age based on equation
final_age = int(((lenght/weight)*age)+10)

#calculate year of birth for user 
yearBirth = 2024-age  #2024+(final_age-age)

#calculate year of final_age
final_year = yearBirth + final_age
"""
can calculate that in other way without yearBirth
(final_year = 2024-(final_age-age))
but this determined in specific year "2024"
"""

#print username and final age with yaer 
print("="*30)
print(f'Welcome, {name.title()}')
print(f'You will live until {final_year},and you will be {final_age} years old')
