def validate_email(email):
    if "@" in email and ".com" in email:
        if email[0] != "@" and email[-1] != "@" and email[-4:] == ".com":
            s = email.split("@")
            if len(s) == 2 and s[1].count(".") <= 1 and s[1].split(".")[0] != "":
                return True
    return False

for i in range(5):
    try:
        email = input("Enter ur Email: ").strip()
        if validate_email(email):
            print("Valid Email")
            break
        else:
            raise ValueError("Invalid Email")
    except ValueError:
        print(ValueError)
else:
    raise ("Try again later.")
