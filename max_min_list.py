n=[]
n1=int(input("enter the masrks 1: "))
n2=int(input("enter the masrks 2: "))
n3=int(input("enter the masrks 3: "))
n4=int(input("enter the masrks 4: "))
n5=int(input("enter the masrks 5: "))
n.append(n1)
n.append(n2)
n.append(n3)
n.append(n4)
n.append(n5)
maximum=max(n)
minimum=min(n)
print(maximum)
print(minimum)
#another version with loop: 
n = []

for i in range(5):
    marks = int(input(f"Enter the marks {i+1}: "))
    n.append(marks)

print("Maximum marks:", max(n))
print("Minimum marks:", min(n))
