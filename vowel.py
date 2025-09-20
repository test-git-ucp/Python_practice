n=input("enter the value:")
vowel=['a' ,'e','i','o','u']
result=""
for char in n:
    if char.lower() not in vowel:
       result +=char
      
print(result)