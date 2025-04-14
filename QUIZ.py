# START
# - Import random library

# FUNCTION generate_question:
#     - Choose a random operator (addition, subtraction, multiplication and division)
#     - Generate two random numbers
#     - Insert the random operator between the two numbers
#     - Make sure division is clean (no remainder) for convenience
#     - Calculate the correct answer based on the operator
#     - Return the question and the correct answer

# FUNCTION generate_choices(correct_answer):
#     - Make 3 fake answers close to the correct one
#     - Insert the correct answer in a random position
#     - Return all choices and the correct one’s index

# MAIN FUNCTION:
#     - Set up choice labels (a, b, c, d)
#     - Open files to save user and correct answers
#     - For the 10 questions:
#         - Generate a question and its correct answer
#         - Generate multiple choices
#         - Ask user to choose a, b, c, or d
#         - Save both the user’s choice and the correct one, so if  we make the other program to check if the user's answer is correct it would be easier
#     - Print all of the user’s answers

# STOP
import random

def generate_question():
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)

    while True:
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        if operator == '/' and num1 % num2 != 0:
            continue
        break