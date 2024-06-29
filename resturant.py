"""
A scale model for building a restaurant program that can be enlarged and based on which applicationa can be built.
"""

#Write name of Restaurant
print("="*30)
print("SEHHA & HANAA \nRestaurant")
print("="*30)

# set of prices for some orders
Pizza = 20
Cola = 5
Water = 1.5

#Enter by user number of each order
numPizza = int(input("What's number of Pizza: "))
numCola = int(input("What's number of Cola: ")) 
numWater = int(input("What's number of Water: "))

#cost for each order
cost_Pizza = Pizza * numPizza
cost_Cola =  Cola * numCola
cost_Water = Water * numWater

#Write list of detalis of order to user
print("-"*30)
print(f'1: Pizza = {numPizza} X {Pizza} = {cost_Pizza} \n2: Cola = {numCola} X {Cola} = {cost_Cola} \n3: Water = {numWater} X {Water} = {cost_Water}')
print("-"*30)

#final cost for all orders
Final_cost = cost_Pizza + cost_Cola + cost_Water

#add tax to final cost by 15% 
Tax = Final_cost * 0.15

#sum of tax and final cost 
Total_cost = Final_cost+Tax

#print detail of cost
print(f'Final_cost = {Final_cost} \nTax = {Tax}')
print("-"*30)
print(f'Total Cost = {Total_cost} \nThank you')
