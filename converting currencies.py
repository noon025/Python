"""
A virtual project for converting between currencies (USD, EUR, SAR)
"""

#virtual numbers for converting between them as formula such that (to_from = x) (to = x * from)
USD_SAR = 3.75
USD_EUR = 0.99
SAR_EUR = 0.99/3.75

#print store welcome
print("="*50)
print("Welcome to $$ EXCHANGE STORE $$")
print("="*50)

#enter original currency and the currency to be converted to with the amount mentioned.
original = input("Exchange FROM (USD, EUR, SAR): ").upper()
amount = int(input("How much? "))
target = input("Exchange to (USD, EUR, SAR): ").upper()

#define variable as int bafore conditions 
money = 0 

#print false if one of currencies not true 
if (original!= "USD") and (original!= "EUR") and (original!="SAR"):
    print("the exchange from not true")
elif target!= "USD" and target!= "EUR" and target!="SAR":
    print("the exchange to not true")

#print no change if currencies are equal
elif original == target:
    print("the cost will still same value")

#create conditions for converting
elif (original == "USD") and (target == "EUR"):
    money = amount / USD_EUR
    print(f'You will give {amount} {original} , and you will take {money} {target}')
elif (original == "USD") and (target == "SAR"):
    money = amount / USD_SAR
    print(f'You will give {amount} {original} , and you will take {money} {target}')
elif (original == "EUR") and (target == "USD"):
    money = amount * USD_EUR
    print(f'You will give {amount} {original} , and you will take {money} {target}')
elif (original == "SAR") and (target == "USD"):
    money = amount * USD_SAR
    print(f'You will give {amount} {original} , and you will take {money} {target}')
elif (original == "SAR") and (target == "EUR"):
    money = amount / SAR_EUR
    print(f'You will give {amount} {original} , and you will take to {money} {target}')
elif (original == "EUR") and (target == "SAR"):
    money = amount * SAR_EUR
    print(f'You will give {amount} {original} , and you will take to {money} {target}')
