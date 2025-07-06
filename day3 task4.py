def validate_email(email):
    if "@" in email and ".com" in email:
        if email[0] != "@" and email[-1] != "@":
            i = email.split("@")
            if len (i) == 2 and i[1].count(".") >=1 and i[1].split(".")[0] != "":
                if email[-4:] == ".com":
                 return True
    return False

while True:
    name = input("Enter ur name: ").strip()
    if name.isalpha():
        break
    else:
        print("Invalid name")

email = input("Enter ur email: ").strip()
while not validate_email(email):
    print("Invalid email")
    email = input("Enter ur email: ").strip()

print("\nYour Data:")
print("Name:", name)
print("Email:", email)
