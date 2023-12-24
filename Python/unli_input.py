numbers = [3,6,2,4,3,6,8,9]
for i in range(len(numbers)): 
    for j in range(i+1, len(numbers)): 
        if numbers[i] == numbers[j]: 
            duplicate = numbers[i] 
            break
for i in range(len(numbers)): 
    if numbers[i] == duplicate: 
        print(i)