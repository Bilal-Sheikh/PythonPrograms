eng=int(input("Enter marks of English: "))
hin=int(input("Enter marks of Hindi: "))
mar=int(input("Enter marks of Marathi: "))
his=int(input("Enter marks of History: "))
geo=int(input("Enter marks of Geology: "))

avg=(eng+hin+mar+his+geo)/5

if(avg>=100):
    print("Enter marks less than 100")
elif(avg>=90 and avg<=100):
    print("Grade A")
elif(avg>=80 and avg<=90):
    print("Grade B")
elif(avg>=70 and avg<=80):
    print("Grade C")
elif(avg>=60 and avg<=70):
    print("Grade D")
elif(avg>=50 and avg<=60):
    print("Grade E")
elif(avg<=50):
    print("Grade F")