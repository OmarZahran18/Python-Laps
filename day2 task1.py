# Fill an array of 5 elements from the user, Sort it in descending and ascending orders
numbers = []
for i in range(5):
    num = int(input("Enter Value"))
    numbers.append(num)
    
print(numbers)
print("Ascending" , sorted(numbers))
print("Descending" , sorted(numbers,reverse=True))