# You are given a list of email addresses, some of which are invalid.
#  Your task is to use the filter() 
# function to return only the valid email addresses.

domines = [
    "ali@gmail.com",
    "sara@yahoo.com",
    "mohamed@outlook.com",
    "omar@",
    "zahran.yahoo@com",
    "ahmed.com@gmail",
    "sayed@outlookcom",
    "khaled hotmail@"
]

valid_emails = filter(
    lambda e: 
        "@" in e and 
        "." in e.split("@")[-1] and 
        e[0] != "@" and 
        e[-1] != "@",
    domines
)

print(list(valid_emails))
