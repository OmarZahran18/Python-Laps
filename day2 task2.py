# Write a program that generate a multiplication table from 1 to the number passed.

x = int(input("Enter Num"))
l = []
for i in range (1, x + 1):
    temp = []
    for y in range (1, i + 1):
            temp.append(i * y)
            l.append(temp)
print(l)