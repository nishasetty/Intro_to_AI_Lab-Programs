flag=True
count=1
while flag:
    perc=input("enter the percept")
    loc=input("enter the location")
    if loc=="A":
        if perc=="dirty":
            print("action: suck...turn right")
            
        else:
            print("action: turn right")
            
    else:
        if perc=="dirty":
            print("action: suck.....turn left")
            
        else:
            print("action: turn left")
    
    print("Do you want to continue?")
    Cont=input("Enter Y or N")
    if Cont == 'Y':
         flag= True
    else : 
         flag = False
