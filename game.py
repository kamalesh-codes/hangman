import random

def choose_word():
    with open("word.txt","r") as f:
        no_line= sum([1 for _ in f])
    with open("word.txt","r") as f:
        line_no=random.randint(1,no_line)
        for i in range(1,no_line+1):
            if i==line_no:
                hint,word = f.readline().split(',')
                return [hint,word.strip().lower()]
            f.readline()
                  
def show_logo():
     with open("hangmanlogo.txt","r") as f:
          print(f.read())

def session(show_hangman_logo=True):

    if show_hangman_logo:
        show_logo() #greeting by showing hangman logo

    #choosing a word from word.txt file
    hint,guessing_word = choose_word()
    word_len = len(guessing_word)

    #game interface
    print("\n==========================================================")
    print("              GUESS THE WORD BY TYPNG LETTERS")
    print("==========================================================\n")

    print(f"HINT : {hint.upper()}")#displaying hint

    #showing the hangman 
    with open("hangman_1.txt","r") as f:
        user_word = ["_" for _ in range(word_len)]
        count=0
        next=True
        total_buffer=0
        while True:
            if next:
                buffer=0
                total_buffer=f.tell()
                for i in range(1,23+1):
                    if i == 8:
                        print(f.readline().strip("\n"),*user_word,end="\n")
                        
                    else:
                        print(f.readline().strip("\n"))
                buffer=f.tell()-total_buffer
            else:
                f.seek(f.tell()-buffer)
                for i in range(1,23+1):
                    if i == 8:
                        print(f.readline().strip("\n"),*user_word,end="\n")
                    else:
                        print(f.readline().strip("\n"))

            if user_word.count("_")==0 or count>5:
                break

            guess = input("\nEnter the letter:").strip().lower() #get user input

            #mark wrong input as wrong guess as a punishment
            if len(guess) != 1:
                print("Enter a single character!")
                count+=1
                continue

            #count n of occurences
            ocurences = guessing_word.count(guess)
            if ocurences == 0:
                count+=1
                next=True

            elif ocurences == 1:
                index = guessing_word.index(guess)
                user_word[index]=guess
                next=False

            elif ocurences>1:
                indeces = []
                for i in range(word_len):
                    if guess == guessing_word[i]:
                        indeces.append(i)
                for index in indeces:
                    user_word[index] = guess
                next=False

        if "".join(user_word) == guessing_word:
            print("\n========================================")
            print("               YOU WON!")
            print("========================================")

        else:
            print("\n========================================")
            print("               YOU LOSE")
            print("========================================")
            print(f"The word is {guessing_word}")

if __name__=="__main__":
    session()
    if input("Do you wanna play it again ? (y/n): ") == "y":
        session(show_hangman_logo=False)

