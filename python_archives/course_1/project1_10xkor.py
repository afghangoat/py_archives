#word="vacation"
#tmp = ""
#for i in range(0,len(word)):
#    tmp += word[i]
#    print(str(tmp))
#    i+=1
#space = " "
#tmp2 = ""
#text = "vacation"
#for i in range(text):
#    print(i*" " + text[i])
#amőba:
board = ["  "," 1"," 2"," 3"," 1"," -"," -"," -"," 2"," -"," -"," -"," 3"," -"," -"," -"]
player1t = True
player2t = False
hwinner = False
while not hwinner:
    for i in range(0,16,4):
        print(board[i] + "|"+board[i+1] + "|"+board[i+2] + "|"+board[i+3])
    if player1t:
        print("1-es játékos jön!")
    else:
        print("2-es játékos jön!")
    newplace = False
    while not newplace:
        row = column = 10
        while row > 3 or row < 1:
            row = int(input("Melyik sorba szeretnél rakni?\n"))
        while column>3 or column <1:
            column=int(input("Melyik oszlopba szeretnél rakni?\n"))
        if board[row*4+column] == " -":
            newplace = True

        if player1t:
            board[row * 4 + column] = "x"
        else:
            board[row * 4 + column] = "o"
        if board[5] == board[6] and board[7] == board[6] and board[5] != " -":
            if player1t:
                print("AZ 1. játékos nyert")
            else:
                print("A(Z) 2. játékos nyert")
            hwinner = True
        if board[9] == board[10] and board[10] == board[11] and board[11] != " -":
            if player1t:
                print("AZ 1. játékos nyert")
            else:
                print("A(Z) 2. játékos nyert")
            hwinner = True
        if board[13] == board[14] and board[14] == board[15] and board[15] != " -":
            if player1t:
                print("AZ 1. játékos nyert")
            else:
                print("A(Z) 2. játékos nyert")
            hwinner = True
        if board[5] == board[10] and board[10] == board[15] and board[15] != " -":
            if player1t:
                print("AZ 1. játékos nyert")
            else:
                print("A(Z) 2. játékos nyert")
            hwinner = True
        if board[7] == board[10] and board[13] == board[10] and board[10] != " -":
            if player1t:
                print("AZ 1. játékos nyert")
            else:
                print("A(Z) 2. játékos nyert")
            hwinner = True
        if board[5] == board[13] and board[9] == board[13] and board[5] != " -":
            if player1t:
                print("AZ 1. játékos nyert")
            else:
                print("A(Z) 2. játékos nyert")
            hwinner = True
        if board[6] == board[14] and board[14] == board[10] and board[10] != " -":
            if player1t:
                print("AZ 1. játékos nyert")
            else:
                print("A(Z) 2. játékos nyert")
            hwinner = True
        if board[7] == board[15] and board[11] == board[7] and board[11] != " -":
            if player1t:
                print("AZ 1. játékos nyert")
            else:
                print("A(Z) 2. játékos nyert")
            hwinner = True
        if " -" not in board and not hwinner:
            hwinner = True
            print("Döntetlen!")
        if not hwinner:
            player1t= not player1t
for i in range(0,16,4):
    print(board[i] + "|"+board[i+1] + "|"+board[i+2] + "|"+board[i+3])
#pythonturtle.org