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
import os

def generate_question():
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)

    while True:
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        if operator == '/' and num1 % num2 != 0:
            continue
        break

    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    elif operator == '/':
        correct_answer = num1 // num2

    question_text = (num1, operator, num2)
    return question_text, correct_answer

def generate_choices(correct_answer):
    choices = []
    while len(choices) < 3:
        fake = correct_answer + random.randint(-10, 10)
        if fake != correct_answer and fake not in choices:
            choices.append(fake)

    correct_position = random.randint(0, 3)
    choices.insert(correct_position, correct_answer)
    return choices, correct_position

def main():
    labels = ['a', 'b', 'c', 'd']
    user_answers = []
    correct_answers = []

    with open("answers.txt", "w") as ans_file, open("correct_answers.txt", "w") as corr_file:
        for i in range(1, 11): # 1 - 10 number of questions
            question, correct = generate_question()
            choices, correct_index = generate_choices(correct)

            print(f"\nQuestion {i}: {question[0]} {question[1]} {question[2]}")
            for options, choice in enumerate(choices):
                print(f"  {labels[options]}) {choice}")

            while True:
                user_input = input("Your answer (a/b/c/d): ").lower()
                if user_input in labels:
                    break
                print("Invalid input. Please choose a, b, c, or d.")

            user_answers.append(f"{i}.{user_input}")
            correct_answers.append(f"{i}.{labels[correct_index]}")

            ans_file.write(f"{i}.{user_input}\n")
            corr_file.write(f"{i}.{labels[correct_index]}\n")

        print("\nYour answers:")
        for ans in user_answers:
            print(ans)

    print("\nSaving files to:", os.getcwd())

if __name__ == "__main__":
    main()
