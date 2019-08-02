def fibonacci(max_iterations):
    """
    Prints the fibonacci sequence until reach max iteration number
    """
    number1, number2 = 0,1
    print(number1, end=" ")
    for i in range (max_iterations - 1):
        number1, number2 = number2, number1 + number2
        print(number1, end=" ")
   


if __name__ == "__main__":
    max_iterations = int(input("Max iterations>"))
    fibonacci(max_iterations)
    