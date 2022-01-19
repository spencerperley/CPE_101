senList = []

while True:

    sentence = input("Enter a sentence with at least three words: ")

    senList = sentence.split(" ")
    
    if len(senList) < 3:
        print("Your sentence is too short")
    
    else:
        break
    
final = []
longest = ""
for word in senList:
    
    if len(word) > len(longest):
        longest = word
    
    if ("e" in word) or ("E" in word):
        final.append(word.upper())
    else:
        final.append(word)
        
        
print(" ".join(final))
print(f"the longest word is {longest}")