item =[]
price =[]
tot = 0
discount = 0
net = 0
no = 0
pr = 0
i=0
no = input("enter item =  ")
while(no != i):
    if (no== "" ) :
        break
        
    pr = input("enter price =  ")
   
    
    try:
        
        if (pr==float(pr)):
            
            price.append(pr)
            
    except ValueError :
        
        print ("The price does not contain numbers")
        continue
    


    
    tot = tot + float (pr)
    no = input("enter item =  ")
    
if(tot > 1000):
    discount = tot*5/100
elif(tot>3000):
    discount = tot*10/100
elif(tot>5000):
    discount = tot*20/100

print("total =  ",tot)
print("discount =   ",discount)
print("net =  ",tot - discount)
