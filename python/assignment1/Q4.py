def simple_interest(p,t,r):
  
    
    si = (p * t * r)/100
    
    print('The Simple Interest is', si)
    
    

P = int(input("Enter the principal amount :"))
T = int(input("Enter the time period :"))
R = int(input("Enter the rate of interest :"))
simple_interest(P,T,R)