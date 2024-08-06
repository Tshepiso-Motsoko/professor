import random

def main():
    # Get the level from the user
    level = get_level()
    # Initialize the score
    score = 0

    # Generate 10 math problems and prompt the user to solve them
    for _ in range(10):
        # Generate two random integers based on the level
        x = generate_integer(level)
        y = generate_integer(level)
        # Create the problem string and calculate the correct answer
        problem = f"{x} + {y} = "
        correct_answer = x + y

        # Allow the user up to three attempts to answer the problem correctly
        for _ in range(3):
            answer = input(problem)
            try:
                # Convert the user's answer to an integer
                answer = int(answer)
                if answer == correct_answer:
                    # If the answer is correct, increment the score and break the loop
                    score += 1
                    break
                else:
                    # If the answer is incorrect, output "EEE" and prompt again
                    print("EEE")
            except ValueError:
                # If the user's input is not a valid integer, output "EEE" and prompt again
                print("EEE")
        else:
            # If the user did not answer correctly after three attempts, output the correct answer
            print(f"The correct answer is: {correct_answer}")

    # Print the final score
    print(f"Score: {score}")

def get_level():
    while True:
        # Prompt the user for the level and validate the input
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return int(level)
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

def generate_integer(level):
    if level == 1:
        # Generate a random integer between 0 and 9 for level 1
        return random.randint(0, 9)
    elif level == 2:
        # Generate a random integer between 10 and 99 for level 2
        return random.randint(10, 99)
    elif level == 3:
        # Generate a random integer between 100 and 999 for level 3
        return random.randint(100, 999)
    else:
        # Raise a ValueError for an invalid level
        raise ValueError("Invalid level.")

if __name__ == "__main__":
    main()
