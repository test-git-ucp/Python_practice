password = input("Enter password: ")

length_ok = False
has_lower = False
has_upper = False

if len(password) >= 8:
    length_ok = True

i = 0
while i < len(password):
    ch = password[i]
    if ch >= 'a' and ch <= 'z':
        has_lower = True
    if ch >= 'A' and ch <= 'Z':
        has_upper = True
    i += 1

if length_ok and has_lower and has_upper:
    print("Strong Password")
else:
    print("Weak Password")
