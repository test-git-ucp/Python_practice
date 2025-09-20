username = input("Enter username: ")


username = username.replace(" ", "_")


username = username.lower()


clean_username = ""
allowed = "abcdefghijklmnopqrstuvwxyz0123456789_."

for char in username:
    if char in allowed:
        clean_username += char


clean_username = clean_username[:15]


if clean_username.startswith("_") or clean_username.startswith("."):
    clean_username = clean_username[1:]

if clean_username.endswith("_") or clean_username.endswith("."):
    clean_username = clean_username[:-1]


print("Formatted Username:", clean_username)

     