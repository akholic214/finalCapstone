import math   #Insert the math module for calculations..
print("investment - to calculate the amount of interest you'll earn on your investment")      
print("bond - to calculate the amount you'll have to pay on a home loan")
choice=input("Enter either 'investment' or 'bond' from the menu above to proceed:")
if choice.lower() == "investment":
    money = int(input("Please enter the deposit ammount : "))
    interest_rate = int(input("Please enter the interest rate : "))
    years = int(input("Please enter the number of years for the deposit : "))
    interest = input("Would you like simple or compound ? ")
    r = interest_rate / 100
    P = money
    t = years
    if interest.lower() == "simple" :
        A = P * (1 + r * t)
        print("Your simple interest will bring you :" , A ,"£") 
    elif interest.lower() == "compound" :
        A = P * math.pow((1 + r) , t)
        print("Your compound interest will bring you :" , A ,"£")
elif choice.lower() == "bond" :
    house_value = int(input("Please enter the property value : "))
    interest_rate = int(input("Please enter the interest rate : "))
    repayment_months = int(input("Please enter the total repayment time in months : "))
    P = house_value
    i = (interest_rate / 100) / 12
    n = repayment_months
    repayment = (i * P) / (1 - (1 + i) ** (-n))
    print("Your repayments for the property are gonna be" , repayment , "£/month")
else : print("Please enter a valid choice")