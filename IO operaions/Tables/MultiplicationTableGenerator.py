for i in range(2, 11):
    with open(f"C:/Users/Bilal Sheikh/Desktop/Coding Stuff/Python/practise/IO operaions/Tables/Multiplication Table of {i}", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}")
            if j!=10:
                f.write("\n")