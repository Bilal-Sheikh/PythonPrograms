n = int(input("Enter a num: "))
sum = 0
order = len(str(n))
original_n = n

while (n>0):
    digit = n%10 # to take the last digit
    sum += digit ** order # mul by the number of digits
    n = n // 10 # removing the last digit until number becomes 0

if (sum == original_n):
    print(f"{original_n} is Armstrong num")
else:    
    print(f"{original_n} is not an Armstrong num")

