def readFile(file):
    try:
        with open (file, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {file} not found!!!!!!!!!")
        
readFile("C:\\Users\\Bilal Sheikh\\Desktop\\Coding Stuff\\Python\\practice\\YOUTUBE\\FileNotFound\\1.txt")
readFile("C:\\Users\\Bilal Sheikh\\Desktop\\Coding Stuff\\Python\\practice\\YOUTUBE\\FileNotFound\\2.txt")
readFile("C:\\Users\\Bilal Sheikh\\Desktop\\Coding Stuff\\Python\\practice\\YOUTUBE\\FileNotFound\\3.txt")