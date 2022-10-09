sum = 0
while (True):
	userItem = input("Enter the item name or press q to quit: \n")
	userInput = input("Enter the item price or press q to quit: \n") 
	if (userItem!='q'):
		with open("C:\\Users\Bilal Sheikh\\Desktop\\Coding Stuff\\Python\\practice\\YOUTUBE\\xShop Receipt System\\Receipt.txt", "a") as f:
			f.write(f"\t {userItem} --- {userInput} \n")
			sum = sum + int(userInput)
			print(f"Order total so far: {sum}")
			f.close()
	else:
		print(f"Your Bill total is {sum}. Thanks for shopping with us")
		break
with open("C:\\Users\Bilal Sheikh\\Desktop\\Coding Stuff\\Python\\practice\\YOUTUBE\\xShop Receipt System\\Receipt.txt", "a") as f1:
	f1.write("-------------------------\nT O T A L: " + str(sum) + "\n\n")
	f1.close()

			