# Ask the user for his name then confirm that he has entered his name(not an empty 
# string/integers). then proceed to ask him for his email and print all this data   

while True:
    name = input("Enter ur name: ").strip()
    if name.isalpha():
        break
    else:
        print("Invalid name. Please enter letters only.")

email = input("Enter your email: ").strip()

print("\n Your data:")
print("Name:", name)
print("Email:", email)

    
    