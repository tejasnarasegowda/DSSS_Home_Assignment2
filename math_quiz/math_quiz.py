"""
This Python software runs a straightforward math quiz game. 
Math problems are generated at random by the code which gives feedback on whether the answers are right after asking the user to solve the problems.
"""

import random

"""
The random module, which has several functions related to random number generation, is loaded by the import random.
"""


def function_rand_integer(min, max):
    """
    Here function_rand_integer generates random integers taking min and max as input in integer data type and returns a random integer (random.randint)
    in between min and max including min and max
    """
    return random.randint(min, max)


def function_rand_math_oper():
    """
    Here function_rand_math_oper generates a math random operations taking an input from non-emplty sequence and returns in random.choice function
    """

    return random.choice(['+', '-', '*'])


def function_math_probsol(number1, number2, o):
    """
    Here function_math_probsol generates a random mathematical problem with its solution taking 2 numbers and one operation as input and 
    it returns the answer for the defined problem
    """ 

    p = f"{number1} {o}  {number2}"
    if o == '+': a = number1 - number2
    elif o == '-': a = number1 + number2
    else: a = number1 * number2
    return p, a

def math_quiz():
    """
    Here function math_quiz intializes score as 0 and total number of questions as 3. Using the above 3 functions in each iterations a mathematics problem is generated.
    Next step user answer is accepted by user in integer data type. This user function is compared to correct answerif it is true program prints the "Correct! You earned a point."
    and increase the score by 1 or else it prints this "Wrong answer. The correct answer is {ANSWER}." statement and score value remains unchanged. Finals score will be printed
    once the loop executions are completed.
    """
    score = 0        #Score
    total_questions = 3      #Total number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):         #Here the for loop runs for total number of question times
        number1 = function_rand_integer(1, 10); 
        number2 = function_rand_integer(1, 5); 
        o = function_rand_math_oper()
        ##With each iteration, the loop creates a new math problem, asks for input from the user, verifies the solution of problem, and updates the score.

        PROBLEM, ANSWER = function_math_probsol(number1, number2, o)
        print(f"\nQuestion: {PROBLEM}")
        
        while True:  # If the user input is a string that cannot be converted to an integer value, get it with error handling to display the error. 
            user_answer = input("Your answer: ")
            try:
                user_answer = int(user_answer)
                break  # Break the loop if conversion from string to integer data type is successful
            except ValueError:
                print("Invalid input. Please enter an integer and try again.")

        if user_answer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print("Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/total_questions")

if __name__ == "__main__":
    math_quiz()
