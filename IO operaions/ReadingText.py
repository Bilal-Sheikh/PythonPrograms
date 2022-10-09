f = open('C:\\Users\Bilal Sheikh\\Desktop\\Coding Stuff\\Python\\practice\\YOUTUBE\\IO operaions\\Poem.txt')
t = f.read()
if 'Twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close