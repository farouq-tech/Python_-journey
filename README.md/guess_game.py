#Guess Game project 
#Date : 18th Oct 

import random
words = ["mohammed","Farouq","Arabi", "Abubakr", "Asmaa","Sam","Youssef"]
print ("the list is :",words)
secret_word =random.choice (words)
guess = ""

guess_limit =0
guess_count=0 
out_of_guess = False


diff_Levels = int(input ("1: easy \n2: Midem \n3: Hard\nSelect your Difficalty Level :"))
if diff_Levels == 1 :
    guess_limit = 5
elif diff_Levels == 2 :
    guess_limit = 3 
else :
    guess_limit = 1 



while guess != secret_word and not out_of_guess :

    if guess_count < guess_limit :

        guess = input (" Enter yor guess : ").lower()
        guess_count += 1
        if guess != secret_word.lower() and guess_count < guess_limit:
            print ("Try agian :(")
    else :
        out_of_guess = True


if guess == secret_word.lower() :       
    print("You Win ")

    
else :
    print ("you lose out of guess ")


