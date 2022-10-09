for num in range(1,101):
#first check for both multiples since 3 and 5 are multiples of itself
    if num%3==0 and num%5==0: 
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)
    



