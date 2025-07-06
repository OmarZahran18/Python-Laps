users = [
    {"name": "omar", "pass": "123"},
    {"name": "ahmed", "pass": "456"}
]

name = input("Enter ur name: ").lower()
password = input("Enter ur password: ")

for i in users:
    if i["name"] == name and i["pass"] == password:
        print("Valid")
        break
else:
    print("Invalid")