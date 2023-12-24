# TEST SYSTEM OF EQUATION
# 4x + 8y + z = 2
# x + 7y – 3z = –14
# 2x – 3y + 2z = 3 

# Initialize the array for the system
arr = [[4,8,1,2],
       [1,7,-3,-14],
       [2,-3,2,3]]

# Initialize a function to find lcm using eucladian algorithm

def find_lcm(num1,num2):
    lcm_num1 = num1
    lcm_num2 = num2
    rem = 0
    while(num2 != 0):
        rem = num1 % num2
        num1 = num2
        num2 = rem
    gcf = num1
    lcm = int((lcm_num1*lcm_num2)/gcf)
    return lcm

# Initialize the function that starts the gaussian method
def update_matrix(count,var,current_col):
    current_row = var # Takes the amount of zeroes as row
    if count == num_of_var_per_row[var]: # Ends when the amount of zeroes is reached
        return
    else:
        lcm = find_lcm(arr[current_row][current_col],arr[count][count]) # Finds the lcm in order to always equate the 2 variable to zero
        multiplier__first_term = lcm//arr[count][count]                 # Takes the first multipler to be used on the entire row
        multipler_second_term = lcm//arr[current_row][current_col]      # Takes the second multiplier to be used on the entire row
        for i in range(0,len(arr[current_row])):
            arr[current_row][i] = (multiplier__first_term * arr[count][i]) - (multipler_second_term * arr[current_row][i]) # Calculates the new matrix row and updates it
        count+=1 # Increases count if one zero is taken
        current_col+=1 # Moves through the horizontal of the matrix
        update_matrix(count,var,current_col)

def find_solutions():
    max_row = len(arr)
    max_col = len(arr[0])
    solution_counter = 2
    solutions = []
    solution = 0
    for i in range(0, max_row): # Creates a list the same size with variable count with dummy values
        solutions.append(1)
    for i in range(max_row-1, -1,-1):
        for j in range(0, max_col):
            if j == max_col - 1: # Subtracts the known variable from the right to the left then performs division when the loop reaches its last term
                solution = (arr[i][j]-solution)//arr[i][solution_counter]
            elif j < max_col-1 and j != solution_counter: # Else calculate the known variable to be substracted with the left side
                solution += arr[i][j] * solutions[j]
        solutions[i] = solution
        solution = 0
        solution_counter-=1
    return solutions
num_of_var_per_row = [i for i in range(0,len(arr))]
z_value = 0

if __name__ == "__main__":
    for i in num_of_var_per_row:
        update_matrix(0,i,0)
    print(find_solutions())

