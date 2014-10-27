## 2 Suit Spider Solitaire
## 11/09/2012
## UM

## Two Suit Spider Solitaire - Please scroll down for rules of the game.

import cards
        
## Creates the foundation, tableau, and stock of cards.        
def setup():
    '''Foundation'''
    thefoundation = [[],[],[],[],[],[],[],[]]
    '''Tableau'''
    thetableau = [[],[],[],[],[],[],[],[],[],[]]
    '''Stock'''
    thestock = []
    ''' Create the deck '''
    for i in range(4):
        aDeck = cards.Deck()
        aDeck.shuffle()
        for j in range(52):
            card = aDeck.deal()
            card.set_hidden()
            if card.get_suit() in "SH":
                thestock.append(card)
    for x in range(54):
        cardremove = thestock.pop()
        thetableau[x%10].append(cardremove)
    ''' Create the rows '''
    for y in range(10):
        thetableau[y][-1].set_hidden(False)

    return thefoundation, thetableau, thestock

## Print the cards, foundation, and stock.
def print_game(fdation, tableau, stock):
    '''Display Tableau'''
    print ("Tableau: ")

    count = 1
    for item in tableau:
        print()
        print ("Row", count, ":", end="")
        count += 1
        for line in item:
            print (line, end="")
             
    '''Display Foundation'''
    fdationlen = len(fdation) - 8
    print()
    print ("\nFoundation: ", fdationlen, "/", "8 runs completed")
    
    '''Display Stock'''
    print ("\nStock:", len(stock), "cards remaining")

## Reveals top card
def reveal_card(tableau, tRow):
    ''' Reveal top card '''
    tableau[tRow - 1][-1].show_card()

## Check if a run has been made and then append to foundation.
def check_completion(tableau, fdation, tRow):
    fdation_move = False
    ''' Get ranks of foundation and tableau '''
    tableau_rank = tableau[int(tRow)-1][len(tableau[int(tRow)-1])-1]
    foundation_rank = fdation[int(tRow)-1][len(fdation[int(tRow)-1])-1]
    ''' Check if order and rank is correct and add to foundation '''
    if tableau_rank.get_rank() - foundation_rank.get_rank() == 1 and tableau_rank.get_suit() == foundation_rank.get_suit():
        tableau[int(t_row)-1].pop()
        fdation[int(f_row)-1].append(tableau[int(t_row)-1][len(tableau[int(t_row)-1])-1])
        reveal_card(tableau,tRow)
        print("Moved card to foundation.")
        return fdation_move == True
    else:
        return fdation_move == False
    ''' If foundation is empty check for Ace '''
    if len(fdation[tRow - 1]) == 0 and tableau[tRow - 1][-1].get_rank() == 1:
        tableau[tRow - 1].remove(tableau[tRow - 1][-1])
        fdation[tRow - 1].append(tableau[tRow - 1][-1])
        reveal_card(tableau, tRow)
        print("Moved card to foundation.")
        return fdation_move == True
    else:
        print("Incorrect move.")

## Check if cards are in correct order of alternating suits and decreasing rank.
def can_be_connected(card1, card2):
    connect = True
    if card2.has_same_color(card1) == True:
        connect = False
    if (card2.get_rank()) - (card1.get_rank()) != 1:
        connect = False
    return connect

## Function to move cards from one row to the other.
def move_in_tableau(tableau, num_of_cards, source_row, dest_row):
    movein = False
    count = -(num_of_cards)
    count2 = count

    ''' Check to see if we can move cards '''
    if len(tableau[source_row-1][count:]) == 1:
        movein = True
    if len(tableau[source_row-1][count:]) != 1:
        for item in tableau[source_row - 1][count:]:
            if count2 < -1:
                if can_be_connected(tableau[source_row - 1][count2 + 1], item) == True:
                    movein = True
                    count2 += 1
                else:
                    movein = False
                    continue

    ''' If correct order, move cards to destination row '''
    if movein == True:
        if len(tableau[source_row - 1])!=0 and len(tableau[dest_row - 1]) == 0:
            for item in tableau[source_row - 1][count:]:
                ''' Move one card if one card in row '''
                if len(tableau[source_row - 1]) == 1:
                    tableau[source_row - 1].remove(item)
                    tableau[dest_row - 1].append(item)

                ''' For more than one card in row, move cards and reveal top card '''
                if len(tableau[source_row - 1]) > 1:
                    tableau[source_row - 1].remove(item)
                    tableau[dest_row - 1].append(item)
                    reveal_card(tableau, source_row)

            return movein
        
    if (can_be_connected(tableau[source_row-1][count], tableau[dest_row-1][-1]) == True) and (tableau[source_row-1][count].get_suit() != tableau[dest_row-1][-1].get_suit()):
        if len(tableau[source_row - 1]) != (-(count)):
            for item in tableau[source_row - 1][count:]:
                tableau[dest_row - 1].append(item)
                tableau[source_row - 1].remove(item)
                reveal_card(tableau, source_row)
        if len(tableau[source_row - 1]) == (-(count)):
            for item in tableau[source_row - 1][count:]:
                tableau[dest_row - 1].append(item)
                tableau[source_row - 1].remove(item)
    else:
        print ("Incorrect move.")

    return movein        

## Deal more cards to tableau.
def deal_more_cards(stock, tableau): 
    newdeal = False 
    remaining_cards = len(stock)
    if 0 < remaining_cards < 10: 
        for x in range(remaining_cards): 
            tableau[x].append(stock[-1])
            tableau[x][-1].set_hidden(False)
            stock.pop() 
            newdeal = True 
    if remaining_cards >= 10: 
        for x in range(10): 
            tableau[x].append(stock[-1])
            tableau[x][-1].set_hidden(False)
            stock.pop() 
            newdeal = True  
    if remaining_cards == 0: 
        newdeal = False 
        print ("Error: No more cards left.") 
    return newdeal

## Check for winner.
def is_winner(fdation):
    count = 0
    for line in fdation:
        if line:
            for card in line:
                count +=1
    if count == 52:
        return True
    else:
        return False

## Print rules, pretty self explanatory.
def print_rules():
    print("\nRules of Spider Solitaire:")
    print("The goal is to move all cards to the foundation. Cards can only be moved")
    print("to the foundation if in a completed run of cards (King, Queen, ..., Ace).")
    print("A single card in the tableau can be moved to another row if the destination")
    print("card is one rank higher than the moving card. Multiple cards can be moved at")
    print("once, but all cards within the stack being moved must be in descending order,")
    print("and they must all be the same suit. The destination card must also be one")
    print("rank higher than the top card of the stack being moved.")

## Shows the available user inputs.
def show_help():
    print("\n")
    print("Acceptable commands:")
    print("q = quit")
    print("d = deal")
    print("h = help")
    print("m (# of cards) (source row #) (dest row #) = ")
    print("move the # of cards from source row to destination row")
    print("\n")

## Beginning of the program, error checking and input/output.
def play():
    print_rules()
    show_help()
    foundation, tableau, stock = setup()
    
    while True:
        print_game(foundation, tableau, stock)
        cmd_input = input("Enter command (h for help, q for quit): ")
        lowerinput = cmd_input.lower()
        playerinput = lowerinput.split()
    
        if is_winner(foundation) == True:
            print("Congratulations, you have no life, but you won!")
            break
        if playerinput[0] == 'h':
            print_rules()
            show_help()
            continue
        if playerinput[0] == 'd':
            deal_more_cards(stock, tableau)
            continue
        if playerinput[0] == 'm' and (len(playerinput) == 4):
            move_in_tableau(tableau, int(playerinput[1]),int(playerinput[2]),int(playerinput[3]))
            continue
        if playerinput[0] == 'q':
            print ("Game over...")
            break
        else:
            print ("\nError, incorrect input.\n")


play()
