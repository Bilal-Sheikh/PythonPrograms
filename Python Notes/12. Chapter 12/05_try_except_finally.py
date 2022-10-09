for i in range(3):
    try:
        i = int(input("Enter a number: "))
        c = 1/i
    except Exception as e:
        print(e)
    finally:
        print("We are done")

    print("Thanks for using the program")