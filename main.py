while(True):

    try:
        import random
        # Snake Water Gun or Rock Paper Scissors
        def gameWin(comp,you):
            # If two values are equals, Declare a tie!
            if comp == you:
                return None

            # Check all possibilities when a computer chose s
            elif comp == 's':
                if you == 'w':
                    return False
                elif you == 'g':
                    return True
            
            # Check all possibilites when a computer chose w
            elif comp == 'w':
                if you == 'g':
                    return False
                elif you == 's':
                    return True

            # Check all possibilites when a computer chose g
            
            elif comp == 'g':
                if you == 's':
                    return False
                elif you == 'w':
                    return True

        print("Comp Turn: Snake(s) , Water(w) or Gun(g)?")
        randomNo = random.randint(1,3)
        if randomNo == 1:
            comp = 's'
        elif randomNo == 2:
            comp = 'w'
        elif randomNo == 3:
            comp = 'g'


        you= input("Yours Trun: Snake(s) , Water(w) , or Gun(g)---->>>>\n")
        
        a = gameWin(comp,you)

        print(f"Computer Choose {comp}")
        print(f"You Choose {you}")

        if a == None:
            print("The Game is a Tie!")
        elif a:
            print("You win!")
        else:
            print("You Loose!!")

    except Exception as e:
        print(e)