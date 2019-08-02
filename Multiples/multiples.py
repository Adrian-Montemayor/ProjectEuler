def sum_multiples():
    """
    Determine the sum of all multiples of 3 or 5 below 1000
    """
    return sum([i for i in range(1,1000) if i%3 ==0 or i%5==0])
    

if __name__ == "__main__":
    print(f'Total: {sum_multiples()}')