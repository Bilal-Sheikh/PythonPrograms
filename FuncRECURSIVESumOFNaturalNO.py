def total_recursive(num):
    if num==1:
        return 1
    elif num==0:
        return 0
    return total_recursive(num-1) + num

sum= total_recursive(10)
print(sum)