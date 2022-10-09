num=int(input("Enter the number: "))

for i in range(1, 11):
#     print(str(num ) + " x " + str(i) + " = " + str(i*num))
# with F strings
    # print(f"{num} x {i} = {i*num}")
    l=[f"{num} x {i} = {i*num}"]
    print(l)

# Printing this table in reverse 
num=int(input("Enter the number: "))

for i in reversed(range(1, 11)):
    l=[f"{num} x {i} = {i*num}"]
    print(l)
