## Print a right-aligned triangle (staircase) pattern using '#' symbols

x = 5
R = []
for i in range(1 , x + 1):
    r = [" "] * x
    for z in range(x - i , x):
        r[z] = ["#"]
    R.append(r)

for r in R:
    print(r)
    
            