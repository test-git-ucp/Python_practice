n="hello kia hal ha mia sb 123567"
digi=['1','2','3','4','5','6','7','8','9','0']
vowe=('a','e','i','o','u')
vowel=''
digit=''
spaces=0
consonent=''
for char in n:
    if char.lower()  in vowe:
       vowel+=char
    elif char in digi:
        digit+=char
    elif char ==' ':
        spaces+=1
    elif char .isalpha():
        consonent+=char
print("Vowels:", vowel)
print("Consonants:", consonent)
print("Digits:", digit)
print("Spaces:", spaces)
