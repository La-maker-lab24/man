import random
lists = ["кот", "вот", "ток", "автомобиль", "дирижабль", "спорт", "йод", "рот"]
word = lists[random.randint(0,7)]
def hangman(word):
    wrong = 0
    stages =["",
             "__________       ",
             "|         |      ",
             "|         0      ",
             "|        /|\     ",
             "|        / \     ",
             "|                ",
             ]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("Это казнь.")
    while wrong<len(stages)-1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] ='$'
        else:
            wrong+=1
        print((" ".join(board)))
        e = wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("Вы выиграли! Было загадно слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Нет! Было загадано слово:\
                {}.".format(word))
hangman(word)
