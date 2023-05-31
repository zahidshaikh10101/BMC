import datetime

rounds = int(input("Enter no. of rounds: "))

amount = 0

while(rounds > 0):
    print("Please enter 1.C 2.M 3.B as follow")
    no_C = int(input("C: "))
    no_M = int(input("M: "))
    no_B = int(input("B: "))
    C_amount = 0
    M_amount = 0
    B_amount = 0
    price_C = 10
    price_M = 12
    price_B = 18
    
    current_time = datetime.datetime.now()
    
    if(no_C > 0):
        C_amount = no_C * price_C
        
    if(no_M > 0):
        M_amount = no_M * price_M
        
    if(no_B > 0):
        B_amount = no_B * price_B
        
    amount1 = C_amount + M_amount + B_amount
    
    print("This round amount: ", amount1)
    print(current_time)
    
    rounds = rounds - 1
    
    amount = amount + amount1
    
print(amount)
