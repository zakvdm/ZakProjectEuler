def sumOfSquares(numbers):
    total = 0
    squares = [num*num for num in numbers]
    for square in squares:
        total = total + square
        
    print(total)

def squareOfSums(numbers):
    total = 0
    for num in numbers:
        total = total + num

    print(total * total)

sumOfSquares(range(1, 101))
squareOfSums(range(1, 101))
        
