with open('C:\\Users\Bilal Sheikh\\Desktop\\Coding Stuff\\Python\\practise\\IO operaions\\Hi-Score.txt') as f:
    hi_score=f.read()
if hi_score=="":
    with open("C:\\Users\Bilal Sheikh\\Desktop\\Coding Stuff\\Python\\practise\\IO operaions\\Hi-Score.txt", "w") as f:
        f.write(str(score))