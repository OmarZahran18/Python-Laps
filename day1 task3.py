# Write a program that generate a multiplication table from 1 to 5
x = input("enter num")
x = int(x)
for i in range(1,6):
    for k in range(1 , i + 1):
        print(f" {i} * {k} ={i*k}")