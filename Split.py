############Printing words which are starting with "s"

# st= "Print only the words that starts with s in this Sentence"

# # print(st.split())
# for letter in st.split():
#     if letter[0].lower() == 's': #using index to find words starting with s
#         print(letter)

############Printing words which are even in length

# st= "Print every word in this sentence that has an even number of letters"

# for letter in st.split():
#     if len(letter) % 2 == 0:
#         print(letter + " is even")

############Creating a list of every word in this sentence

st= "Create a list of the first letter of every first letter in a string"

print([letter[0] for letter in st.split()])