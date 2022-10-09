letter = '''\n\nDear <|Name|>,
YOU ARE SELECTED! 

Date: <|Date|>'''
name=input("Enter your name: ")
date=input("Enter a date:")
letter=letter.replace("<|Name|>", name)
letter=letter.replace("<|Date|>", date)
print(letter)