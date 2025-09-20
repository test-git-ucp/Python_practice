a=[1,2,3,4,5,9,8,6,7]

print(a)
"""
#sort method in list by different way:
a.sort()
print(a)
b=sorted(a)
print(b)"""


"""
#slicing
print(a[1:6]) #simple slicing by index
print(a[0:])#start to end slicing from 0
print(a[:9])#start to slicing until index 9 reach
print(a[::2])#by step slicing
print(a[::-1])#reverse list"""

"""
#copy of list
b=a #if we do  copy by this type all changes also occur in main list 
b.pop(8)
print(a)
print(b)
c=a.copy()
c.append(888)# in this way only change occur in new list
print(c)
d=list(a)#different but same to copy list
print(d)"""
#pop append clear remove insert count 
#a.pop(8)#remove item by index
#a.append("ali") #append item at end
#a.remove(2)#remove the item 
#a.clear() #clear kar deta ha list ko
#g=a.count(1)#count value 
#print(g)
#a.insert(0,99)#take 2 arguments 1 index and other value
#print(len(a))

# comprehension of list advanced python
#b=list([x*x for x in a])
#b.sort()
#b.append(100)
#print(b)
# max min sum all any extend index
"""
print(max(a))
print(min(a))
print(sum(a))
print(a.index(4))
b=[10,20,30]
a.extend(b)
print(a)
"""
#enumerate ko use karna sa index bhi sath show kar skta hn:
"""for i,val in enumerate(a):
    print(f"val{val}->{i}")"""
names = ["Ali", "Sara", "Ahmed"]
marks = [90, 85, 92]

for n, m in zip(names, marks):
    print(n, "->", m)
    
    
#lamda reduce filter map
nums=[1,2,3]
#add=list(map(lambda x:x*x,nums))
add=list(filter(lambda x: x%2==0 ,nums))


print(add)
nums = [1, 2, 3, 4, 5, 6]

result = list(map(lambda x: f"{x} is Even" if x % 2 == 0 else f"{x} is Odd", nums))
print(result)

# Output:
# ['1 is Odd', '2 is Even', '3 is Odd', '4 is Even', '5 is Odd', '6 is Even']



