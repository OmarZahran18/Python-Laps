# Write a program that counts up the number of vowels [a, e, i, o, u]contained in the string.

T = "My Name Is Omar Zahran"

v= "aeiou"
counter =0
for i in T:
    if i in v:
        counter+=1
    
print(counter)




