def fibonacci(max_iterations):
    """
    Prints the fibonacci sequence until reach max iteration number
    Prints the even sum, as well
    """
    number1, number2 = 1,2
    even_sum = 0
    print(number1, end=" ")
    for i in range (max_iterations - 1):
        if(number1 > 4000000 or number2 > 4000000):
            break
        number1, number2 = number2, number1 + number2
        if number1 % 2 == 0:
            even_sum += number1
        print(number1, end=" ")
    
    print("\nEven Sum: " + str(even_sum))


if __name__ == "__main__":
    max_iterations = int(input("Max iterations>"))
    fibonacci(max_iterations)
    