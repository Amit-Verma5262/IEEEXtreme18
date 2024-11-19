def probability_of_alice_winning(R1, B1, R2, B2):
    memo = {}

    
    def dp(R1, B1, R2, B2, alice_turn):
        # Base cases
        if R1 == 0 and B1 == 0:  # Alice loses
            return 0.0
        if R2 == 0 and B2 == 0:  # Bob loses
            return 1.0
        if (R1, B1, R2, B2, alice_turn) in memo:
            return memo[(R1, B1, R2, B2, alice_turn)]

        if alice_turn:
            # Alice's turn, maximize her probability of winning
            result = 0.0
            total_choices = 0
            
            if R1 > 0:  # If Alice can choose Red
                total_choices += 1
    
                result += 0.5 * dp(R1 - 1, B1, R2, B2, False)
                result += 0.5 * dp(R1, B1, R2, B2 - 1, False)

            if B1 > 0:  # If Alice can choose Blue
                total_choices += 1

                result += 0.5 * dp(R1, B1 - 1, R2 - 1, B2, False)
                result += 0.5 * dp(R1, B1 - 1, R2, B2 - 1, False)

            if total_choices > 0:
                result /= total_choices  
        else:
            
            result = 1.0 
            total_choices = 0
            
            if R2 > 0:  # If Bob can choose Red
                total_choices += 1
              
                result = min(result, 0.5 * dp(R1 - 1, B1, R2 - 1, B2, True))
                result = min(result, 0.5 * dp(R1, B1 - 1, R2 - 1, B2, True))

            if B2 > 0:  # If Bob can choose Blue
                total_choices += 1
                
                result = min(result, 0.5 * dp(R1 - 1, B1, R2, B2 - 1, True))
                result = min(result, 0.5 * dp(R1, B1 - 1, R2, B2 - 1, True))

            if total_choices > 0:
                result /= total_choices  

        memo[(R1, B1, R2, B2, alice_turn)] = result
        return result

    # Start with Alice's turn
    return dp(R1, B1, R2, B2, True)


R1, B1, R2, B2 = map(int, input().strip().split())
print(f"{probability_of_alice_winning(R1, B1, R2, B2):.6f}")