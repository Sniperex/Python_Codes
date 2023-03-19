word=input("Enter Word: ")
pallindrome=word[::-1]
if word==pallindrome:
    print("The word is a Pallindrome", word)
else:
    print("Word is not a Pallindrome", word)
    
