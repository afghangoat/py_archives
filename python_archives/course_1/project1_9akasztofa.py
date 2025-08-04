#Akasztófa
word=["******** *******"]
word_real=["computer science"]
life=10
correct_letter=[]
incorrect_letter=[]
while word_real != word and life > 0:
    print(word)
    guess = input("Guess the letter:\n")
#    if len(guess) == len(word_real):
#        temp = word
#        word = guess
#        print("You tried to guess the whole solution.")
#        if word == word_real:
#            print("You won!")
#        else:
#            print("Wrong one. You failed!")
#            print(f"You have {life} lives left.")
#            word = temp
    letter_found = False
    for i in range(len(word_real)):
        if word_real[i] == guess:
            my_solution_list=list(word)
            my_solution_list[i] = guess
            word="".join(my_solution_list)
            letter_found = True
    if not letter_found:
        incorrect_letter.append(guess)
        life -= 1
        print("this was a bad guess")
        print(f"You have {life} lives left.")
    else:
        correct_letter.append(guess)
    print(f"List of correct letters:{correct_letter}, list of incorrect letters:{incorrect_letter}.")
if life > 0:
    print("You are winner")
else:
    print("Bruh, you lost hangman.")
