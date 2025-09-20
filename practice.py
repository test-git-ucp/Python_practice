print("hello")
"""a=int(input("enter a value:"))
j=1
while j<=10:
    for i in range(1,11):
        print(f"{j}x{i}={j*i}")
    print("")
    j+=1"""

"""n=int(input("enter a value:"))
i=0
sum=0
while i<=n:
    print(i)
    sum=i+sum
    i+=1
print(sum) """   

"""n=int(input("enter a value:"))
i=1
product=1
while i<=n:
    print(i)
    product=i*product
    i+=1
print(product) """
"""
n = int(input("Enter a number: "))

if n <= 1:
    print("Not a prime number")
else:
    flag = 0
    for i in range(2, n):
        if n % i == 0:
            flag = 1
            break

    if flag == 0:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")
"""

"""n=int(input("enter value:"))
if(n<=1):
    print("enter a valid num:")
else:
      
   for i in range(2,n):
     flag=0
     if(n%i==0):
        flag=1
        break
      
      
if(flag==0):
    print("yes")
else:
    print("no") """  
    
for num in range(2, 101):  
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

   



































