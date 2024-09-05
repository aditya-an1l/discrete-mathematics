import itertools

def truth_table(num_of_proposition):
    truth_values = [True, False]
    
    combinations = itertools.product(truth_values, repeat=num_of_proposition)
    
    for combo in combinations:
        print(*combo, "\n")

if __name__ == "__main__":
    try:
        num_of_proposition = int(input("Enter the number of propositions: "))
        if num_of_proposition < 0:
            raise ValueError("The number of propositions must be a non-negative integer.")
        
        print(f"All possible combinations of truth values for {num_of_proposition} propositions:")
        truth_table(num_of_proposition)
    except ValueError as e:
        print(f"Invalid input: {e}")
