def solve_test_case():
  
    n = int(input())

    arr = list(map(int, input().split()))
    

    modified_array = arr[:]
    

    for i in range(0, n, 2):
    
        curr_sum = modified_array[i] + modified_array[i + 1]
        
        flipped_sum = -modified_array[i] - modified_array[i + 1]
        
  
        if flipped_sum > curr_sum:
            modified_array[i] = -modified_array[i]
            modified_array[i + 1] = -modified_array[i + 1]


    max_so_far = modified_array[0]
    max_ending_here = modified_array[0]
    
    for i in range(1, n):
        max_ending_here = max(modified_array[i], max_ending_here + modified_array[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

def main():
    # Read number of test cases
    t = int(input())
    
    # Process each test case
    for _ in range(t):
        result = solve_test_case()
        print(result)

if __name__ == "__main__":
    main()