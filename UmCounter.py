um_counter = 0
like_counter = 0

text_file = input("File Name: ")

with open("%s" % text_file) as monologue:
    monologue = monologue.readlines()


for words in monologue:
    list_words = words.split()

for word in list_words:
    if word == "um":
        print(word)
        um_counter += 1
    elif word == "like":
        print(word)
        like_counter += 1

print("UM counter =", um_counter)
print("LIKE counter =", like_counter)
