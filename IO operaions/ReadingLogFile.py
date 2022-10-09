content =True
i=1
with open("C:\\Users\Bilal Sheikh\\Desktop\\Coding Stuff\\Python\\practice\\YOUTUBE\\IO operaions\\RandomLogFile.txt") as f:
    while content:
        content=f.readline()
        if "python" in content.lower():
            print(content)
            print(f"Python is present on line {i}")
            print(i)
        i+=1
        