n=input("enter the value:")
a=''.join(reversed(n))
if(n==a):
    print("word is palindrome")
else:
    print("not palindrome")