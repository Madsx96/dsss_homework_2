"""
-----------------------------------------------------------------------------
 Name:          math_quiz.py
 Purpose:       This script is a Math Quiz Game which user should answer a number of
                simple arithmetic math questions and eventually it gives out a score.
 Modified by:   Mohammad Ali Karimi (mohammadali.karimi@fau.de)
 Interpreter:   PYTHON version 3.11.5
 Created:       2023/11/12
 Licence:       Apache 2.0
-----------------------------------------------------------------------------
"""

import random


def function_A(min, max):
    """
    Generates two numbers randomly in range of min and max.
    
    Args:
        min_number (int): The minimum number
        max_number (int): The maximum number

    Return:
        int: a random number between min and max.
    """
    return random.randint(min, max)


def function_B():
    """
    Randomly generates an arithmetic operator from '+', '-', '*'.
    
    Arg:
        void
        
    Return:
        str: a random arithmetic operator.
    """
    return random.choice(['+', '-', '*'])


def function_C(n1, n2, o):
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
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 - n2
    elif o == '-': a = n1 + n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    """
    This function runs the Math Quiz Game!
    
    Arg:
        void
    
    Return:
        None
    """
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = function_A(1, 10); n2 = function_A(1, 5.5); o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
