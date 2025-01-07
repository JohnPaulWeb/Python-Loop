totaljp = 0
count = 0

while count < 10:

    for i in range(1):  
        number = float(input(f"Enter number {count + 1}: "))
        totaljp += number 
    count += 1  

print(f"The total number is: {totaljp}")