eng=int(input("Enter marks of English: "))
hin=int(input("Enter marks of Hindi: "))
mar=int(input("Enter marks of Marathi: "))

avg=(eng+hin+mar)/3

if(eng<10 or hin<10 or mar<10):
    print("Fail due to less marks in subjects")
elif(avg<50):
    print("Fail due to less average")
else:
    print("PASS!!!!!!")
