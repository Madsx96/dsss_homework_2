"""----------------------------------------------------------------------------------------------
 Name:          math_quiz.py
 Purpose:       This script is a Math Quiz Game which user should answer a number of
                simple arithmetic math questions and eventually it gives out a score.
 Modified by:   Mohammad Ali Karimi (mohammadali.karimi@fau.de)
 Interpreter:   PYTHON version 3.11.5
 Created:       2023/11/12
 Licence:       Apache 2.0
----------------------------------------------------------------------------------------------
"""

import random


def number_generator(min_number: int, max_number: int) -> int :
    """
    Generates two numbers randomly in range of min and max.
    
    Args:
        min_number (int): The minimum number
        max_number (int): The maximum number

    Return:
        int: a random number between min and max.
    """
    # creates a random integer which will be used for two numbers in math questions
    return random.randint(min_number, max_number)


def operator_generator() -> str:
    """
    Randomly generates an arithmetic operator from '+', '-', '*'.
    
    Arg:
        void
        
    Return:
        str: a random arithmetic operator.
    """
    # creates a random arithmetic operation which will be used in math problem
    return random.choice(['+', '-', '*'])


def solver(number_1: int, number_2: int, operator: str) -> (str, int):
    """
    Gets two numbers and an operator, calculating the result of the mathematical operation.
     
    Args:
        number_1 (int): given number
        number_2 (int): given number
        operator (str): arithmetic operator
        
    Returns:
        problem (str): problem display
        answer (int): result of arithmetic operation
    """
    problem = f"{number_1} {operator} {number_2}"
    if operator == '+':
        answer = number_1 + number_2
    elif operator == '-':
        answer = number_1 - number_2
    else:
        answer = number_1 * number_2
    return problem, answer


def math_quiz() -> None:
    """
    This function runs the Math Quiz Game!
    
    Arg:
        void
    
    Return:
        None
    """
    score = 0
    total_questions = 3
    
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number_1 = number_generator(1, 10)
        number_2 = number_generator(1, 10)
        operator = operator_generator()

        problem, answer = solver(number_1, number_2, operator)
        print(f"\nQuestion: {problem}")
        
        # this loop prevents user to input any other data type but integer. this is because an integer is only valid for the answer of this mathematical question.
        while True:
            try:
                user_answer = int(input("Your answer: "))
            except ValueError:
                print("Please enter an integer number!")
                continue
            break
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

# checks whether the Python script is being run as the main program
if __name__ == "__main__": 
    math_quiz()
    