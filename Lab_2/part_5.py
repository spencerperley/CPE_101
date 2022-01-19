word = input("Enter a five letter word: ")

if len(word)!=5:
    print("{word} is not five letters long")
else:
    drow = word[4] + word[3]+word[2]+word[1]+word[0]
    if word == drow:
        print (f'{drow} is {word} backwards.\nIt is a palendrome')
    else:
        print (f'{drow} is {word} backwards.\nIt is not a palendrome')
