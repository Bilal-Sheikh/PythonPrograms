words=["morning","hi","hello"]

with open('C:\\Users\Bilal Sheikh\\Desktop\\Coding Stuff\\Python\\practice\\IO operaions\\ReplacingTextInFile.txt') as f:
    content=f.read()

for word in words:
    content= content.replace(word, "***********")
    with open('C:\\Users\Bilal Sheikh\\Desktop\\Coding Stuff\\Python\\practice\\IO operaions\\ReplacingTextInFile.txt', "w") as f:
        f.write(content)