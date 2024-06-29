"""
The idea of the project is to make tenders within a company and
the offer with an acceptable rate and the lowest price is the one that is chosen.
"""

#enter names and cost for each one 
names = input("Write the names of provides (Seprate each name with a comma): ")
cost = input("Write the cost of offers (Seprate each cost with a comma): ")

#seprate names and costs in lists 
names_list = names.split(", ")
cost_list = cost.split(", ")

#define initial list to the rate 
rate = [0, 0, 0, 0, 0 ]

#create list for accepted rate offers, names and cost for them
accept = []
names_new = []
cost_new = []

#view an alert message if offers less than five
if len(names_list) <5:
    print("You must enter at least 5 offers")

#entring rate for each offer and insert this values in rate list
else:
    rate[0] = float(input(f"Write the rate of {names_list[0]}'s bid, with cost {cost_list[0]}: "))
    rate[1] = float(input(f"Write the rate of {names_list[1]}'s bid, with cost {cost_list[1]}: "))
    rate[2] = float(input(f"Write the rate of {names_list[2]}'s bid, with cost {cost_list[2]}: "))
    rate[3] = float(input(f"Write the rate of {names_list[3]}'s bid, with cost {cost_list[3]}: "))
    rate[4] = float(input(f"Write the rate of {names_list[4]}'s bid, with cost {cost_list[4]}: "))
    print("=================================")

#create loop in list of rate to check accepted rate (more or equal five)
for i in range(0,5):
    if rate[i] >= 5:
      accept.append(rate[i]) #added accepted offers to accept list
      cost_new.append(int(cost_list[i])) #added cost offers that accepted in new list
      names_new.append(names_list[i]) #added names offers that accepted in new list

#print numbers of all and accepted offers 
print(f"Number of offered bids: {len(names_list)} ")
print(f"Number of accepted offers: {len(accept)} ")

#choose less cost from accepted offers
minm = min(cost_new)

#knowledge number of index for minmum cost
index = cost_new.index(minm)

#import name for minmum cost by number of index
name = names_new[index]

#print selected offer 
print(f"The winner offer is: {name}, with cost {minm}, and rate is {accept[index]}")
