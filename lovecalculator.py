def calculate_love_score(name1, name2):
    name = name1.lower() + name2.lower()
    true = 0
    love = 0

    for letter in "true":
        true += name.count(letter)
    for letter in "love":
        love += name.count(letter)

    print(str(true)+str(love))

calculate_love_score(name1 = "Angela Yu", name2 = "Jack Bauer")