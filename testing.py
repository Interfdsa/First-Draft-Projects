"""this is my first attempt at making a heads up blackjack game in python"""
import random
Jack = 10
Queen = 10
King = 10
Ace= 11
Hand = []
Card_Value= [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King]
Suits = ["of Spades", "of Clubs", "of Hearts", "of Diamonds"]
def win_condition_Blackjack():
    if (sum(PlayerHand) > sum(Hand) and sum(PlayerHand) <= 21):
        print("Congratulations you win!")
    elif (sum(PlayerHand) <= 21 and sum(Hand) > 21):
        print("Congratulations you win!")
        exit()
    elif sum(PlayerHand) == sum(Hand):
        print ("Push")
        exit()
    else:
        print( "Dealer Wins, Sorry! better luck next time!")
        exit()
def win_conditions():
    if (sum(PlayerHand) > sum(Hand) and sum(PlayerHand) < 21):
        print("Congratulations you win!")
        exit()
    elif (sum(PlayerHand) <= 21 and sum(Hand) > 21):
        print("Congratulations you win!")
        exit()
    elif sum(PlayerHand) == sum(Hand):
        print ("Push")
        exit()
    elif sum(PlayerHand) == 21:
        dealer()
        win_condition_Blackjack()
    else:
        print("Dealer Wins, Sorry! better luck next time!")
        exit()
def FirstCard():
    cardval1 = random.choice(Card_Value)
    suitval1 = random.choice(Suits)
    Hand.append(cardval1)
    print("Dealers 1st Card is", cardval1, suitval1)
def dealer():
    if sum(Hand) < 17:
        cardval2 = random.choice(Card_Value)
        suitval2 = random.choice(Suits)
        Hand.append(cardval2)
        print("Dealers 2nd Card is", cardval2, suitval2)
        if sum(Hand) < 17:
            cardval3 = random.choice(Card_Value)
            suitval3 = random.choice(Suits)
            Hand.append(cardval3)
            print("Dealers 3rd Card is", cardval3, suitval3)
            if sum(Hand) < 17:
                cardval4 = random.choice(Card_Value)
                suitval4 = random.choice(Suits)
                Hand.append(cardval4)
                print("Dealers 4th Card is", cardval4, suitval4)
                if sum(Hand) < 17:
                    cardval5 = random.choice(Card_Value)
                    suitval5 = random.choice(Suits)
                    Hand.append(cardval5)
                    print("Dealers 5th Card is", cardval5, suitval5)
                    if sum(Hand) < 17:
                        cardval6 = random.choice(Card_Value)
                        suitval6 = random.choice(Suits)
                        Hand.append(cardval6)
                        print("Dealers 6th Card is", cardval6, suitval6)
                        if sum(Hand) < 17:
                            cardval7 = random.choice(Card_Value)
                            suitval7 = random.choice(Suits)
                            Hand.append(cardval7)
                            print("Dealers 7th Card is", cardval7, suitval7)
                            if sum(Hand) < 17:
                                cardval8 = random.choice(Card_Value)
                                suitval8 = random.choice(Suits)
                                Hand.append(cardval8)
                                print("Dealers 8th Card is", cardval8, suitval8)
                                if sum(Hand) < 17:
                                    cardval9 = random.choice(Card_Value)
                                    suitval9 = random.choice(Suits)
                                    Hand.append(cardval9)
                                    print("Dealers 9th Card is", cardval9, suitval9)
                                    if sum(Hand) < 17:
                                        cardval10 = random.choice(Card_Value)
                                        suitval10 = random.choice(Suits)
                                        Hand.append(cardval10)
                                        print("Dealers 10th Card is", cardval10, suitval10)
                                        if sum(Hand) < 17:
                                            cardval11 = random.choice(Card_Value)
                                            suitval11 = random.choice(Suits)
                                            Hand.append(cardval11)
                                            print("Dealers 11th Card is", cardval11, suitval11)
                                            if sum(Hand) < 17:
                                                cardval12 = random.choice(Card_Value)
                                                suitval12 = random.choice(Suits)
                                                Hand.append(cardval12)
                                                print("Dealers 12th Card is", cardval12, suitval12)
    ticker= Ace
    count = Hand.count(ticker)
    if sum(Hand) > 21:
        Hand.append(-10*count)
    if sum(Hand) < 17:
        cardvaln = random.choice(Card_Value)
        suitvaln = random.choice(Suits)
        Hand.append(cardvaln)
        print("Dealers Next Card is", cardvaln, suitvaln)
        if sum(Hand) < 17:
            cardvaln1 = random.choice(Card_Value)
            suitvaln1 = random.choice(Suits)
            Hand.append(cardvaln1)
            print("Dealers Next Card is", cardvaln1, suitvaln1)
            if sum(Hand) < 17:
                cardvaln2 = random.choice(Card_Value)
                suitvaln2 = random.choice(Suits)
                Hand.append(cardvaln2)
                print("Dealers Next Card is", cardvaln2, suitvaln2)
                if sum(Hand) < 17:
                    cardvaln3 = random.choice(Card_Value)
                    suitvaln3 = random.choice(Suits)
                    Hand.append(cardvaln3)
                    print("Dealers Next Card is", cardvaln3, suitvaln3)
                    if sum(Hand) < 17:
                        cardvaln4 = random.choice(Card_Value)
                        suitvaln4 = random.choice(Suits)
                        Hand.append(cardvaln4)
                        print("Dealers Next Card is", cardvaln4, suitvaln4)
                        if sum(Hand) < 17:
                            cardvaln5 = random.choice(Card_Value)
                            suitvaln5 = random.choice(Suits)
                            Hand.append(cardvaln5)
                            print("Dealers Next Card is", cardvaln5, suitvaln5)
    count2= Hand.count(ticker) - count
    if sum(Hand) > 21:
        Hand.append(-10*count2)
    if sum(Hand) < 17:
        cardvalm = random.choice(Card_Value)
        suitvalm = random.choice(Suits)
        Hand.append(cardvalm)
        print("Dealers mext Card is", cardvalm, suitvalm)
        print("Dealers hand total is", sum(Hand))
        if sum(Hand) < 17:
            cardvalm1 = random.choice(Card_Value)
            suitvalm1 = random.choice(Suits)
            Hand.append(cardvalm1)
            print("Dealers mext Card is", cardvalm1, suitvalm1)
            print("Dealers hand total is", sum(Hand))
            if sum(Hand) < 17:
                cardvalm2 = random.choice(Card_Value)
                suitvalm2 = random.choice(Suits)
                Hand.append(cardvalm2)
                print("Dealers mext Card is", cardvalm2, suitvalm2)
                print("Dealers hand total is", sum(Hand))
                if sum(Hand) < 17:
                    cardvalm3 = random.choice(Card_Value)
                    suitvalm3 = random.choice(Suits)
                    Hand.append(cardvalm3)
                    print("Dealers mext Card is", cardvalm3, suitvalm3)
                    print("Dealers hand total is", sum(Hand))
                    if sum(Hand) < 17:
                        cardvalm4 = random.choice(Card_Value)
                        suitvalm4 = random.choice(Suits)
                        Hand.append(cardvalm4)
                        print("Dealers mext Card is", cardvalm4, suitvalm4)
                        print("Dealers hand total is", sum(Hand))
                        if sum(Hand) < 17:
                            cardvalm5 = random.choice(Card_Value)
                            suitvalm5 = random.choice(Suits)
                            Hand.append(cardvalm5)
                            print("Dealers mext Card is", cardvalm5, suitvalm5)
    count3 = Hand.count(ticker) - (count +count2)
    if sum(Hand) > 21:
        Hand.append(-10*count3)
    if sum(Hand) < 17:
        cardvalp = random.choice(Card_Value)
        suitvalp = random.choice(Suits)
        Hand.append(cardvalp)
        print("Dealers pext Card is", cardvalp, suitvalp)
        print("Dealers hand total is", sum(Hand))
        if sum(Hand) < 17:
            cardvalp1 = random.choice(Card_Value)
            suitvalp1 = random.choice(Suits)
            Hand.append(cardvalp1)
            print("Dealers pext Card is", cardvalp1, suitvalp1)
            print("Dealers hand total is", sum(Hand))
            if sum(Hand) < 17:
                cardvalp2 = random.choice(Card_Value)
                suitvalp2 = random.choice(Suits)
                Hand.append(cardvalp2)
                print("Dealers pext Card is", cardvalp2, suitvalp2)
                print("Dealers hand total is", sum(Hand))

    if sum(Hand) > 21:
        print("Dealers hand total is", sum(Hand), "and went bust")
    else:
        print ("Dealers hand total is", sum(Hand))
FirstCard()
PlayerHand = []
def player():
    playercard = random.choice(Card_Value)
    playersuit = random.choice(Suits)
    playercard2 = random.choice(Card_Value)
    playersuit2 = random.choice(Suits)
    PlayerHand.append(playercard)
    PlayerHand.append(playercard2)
    print("Players 1st Card is", playercard, playersuit)
    print("Players 2nd Card is", playercard2, playersuit2)
    #print("Player Hand total is", sum(PlayerHand))
    if sum(PlayerHand) == 21:
        print("BlackJack!")
        print("Player hand total is", sum(PlayerHand))
        dealer()
        win_conditions()
    elif sum(PlayerHand) > 21:
        playercount0 = PlayerHand.count(Ace)
        PlayerHand.append(-10*playercount0)
        print("Player hand total is", sum(PlayerHand))
    elif sum(PlayerHand) < 21:
        print("Player hand total is", sum(PlayerHand))
        answer = input("Would you like another card?")
        if answer == "no":
            dealer()
            win_conditions()
        if answer == "yes":
            playercount0 = PlayerHand.count(Ace)
            playercard3 = random.choice(Card_Value)
            playersuit3 = random.choice(Suits)
            PlayerHand.append(playercard3)
            print("Players 3rd Card is", playercard3, playersuit3)
            if sum(PlayerHand) == 21:
                print("21 Well Done!")
                dealer()
                win_conditions()
            elif sum(PlayerHand) > 21:
                PlayerHand.append(-10*playercount0)
                #print("Player Hand total is", sum(PlayerHand))
            if sum(PlayerHand) > 21:
                print("Player Hand total is", sum(PlayerHand))
                print("too many")
                win_conditions()
            else:
                print("Players Hand total is", sum(PlayerHand))
                answer = input("Would you like another card?")
                if answer == "no":
                    dealer()
                    win_conditions()
                if answer == "yes":
                    playercard5 = random.choice(Card_Value)
                    playersuit5 = random.choice(Suits)
                    PlayerHand.append(playercard5)
                    print("Players 4th Card is", playercard5, playersuit5)
                    print("Player Hand total is", sum(PlayerHand))
                    if sum(PlayerHand) == 21:
                        print("21 Well Done!")
                        (dealer())
                        win_conditions()
                    elif sum(PlayerHand) > 21:
                        PlayerHand.append(-10 * playercount0)

                    elif sum(PlayerHand) > 21:
                        print("Player Hand total is", sum(PlayerHand))
                        print("too many")
                        win_conditions()
                    else:
                        print("Players Hand total is", sum(PlayerHand))
                        answer = input("Would you like another card?")
                        if answer == "no":
                            dealer()
                            win_conditions()
                        elif answer == "yes":
                            playercard4 = random.choice(Card_Value)
                            playersuit4 = random.choice(Suits)
                            PlayerHand.append(playercard4)
                            print("Players 5th Card is", playercard4, playersuit4)
                            print("Player Hand total is", sum(PlayerHand))
                            if sum(PlayerHand) == 21:
                                print("21 Well Done!")
                                dealer()
                                win_conditions()
                            elif sum(PlayerHand) > 21:
                                PlayerHand.append(-10 * playercount0)
                            elif sum(PlayerHand) > 21:
                                print("too many")
                                win_conditions()
    if sum(PlayerHand) > 21:
        playercount1 = (PlayerHand.count(Ace) - playercount0)
        PlayerHand.append(-10*playercount1)
        print("Player Hand total is",sum(PlayerHand))
    answer = input("Would you like another card?")
    if answer == "no":
        dealer()
        win_conditions()
    if answer == "yes":
        playercard3a = random.choice(Card_Value)
        playersuit3a = random.choice(Suits)
        PlayerHand.append(playercard3a)
        print("Players 3rd Card is", playercard3a, playersuit3a)
        print("Player Hand total is", sum(PlayerHand))
        if sum(PlayerHand) == 21:
            print("21 Well Done!")
            dealer()
            win_conditions()
        elif sum(PlayerHand) > 21:
            PlayerHand.append(-10 * playercount1)
        elif sum(PlayerHand) > 21:
            print("Player Hand total is", sum(PlayerHand))
            print("too many")
            win_conditions()
        else:
            print("Players Hand total is", sum(PlayerHand))
            answer = input("Would you like another card?")
            if answer == "no":
                dealer()
                win_conditions()
            if answer == "yes":
                playercard5a = random.choice(Card_Value)
                playersuit5a = random.choice(Suits)
                PlayerHand.append(playercard5a)
                print("Players 4th Card is", playercard5a, playersuit5a)
                if sum(PlayerHand) == 21:
                    print("21 Well Done!")
                    (dealer())
                    win_conditions()
                elif sum(PlayerHand) > 21:
                    PlayerHand.append(-10 * playercount1)
                elif sum(PlayerHand) > 21:
                    print("Player Hand total is", sum(PlayerHand))
                    print("too many")
                    win_conditions()
                else:
                    print("Players Hand total is", sum(PlayerHand))
                    answer = input("Would you like another card?")
                    if answer == "no":
                        dealer()
                        win_conditions()
                    elif answer == "yes":
                        playercard4a = random.choice(Card_Value)
                        playersuit4a = random.choice(Suits)
                        PlayerHand.append(playercard4a)
                        print("Players 5th Card is", playercard4a, playersuit4a)
                        print("Player Hand total is", sum(PlayerHand))
                        if sum(PlayerHand) == 21:
                            print("21 Well Done!")
                            dealer()
                            win_conditions()
                        elif sum(PlayerHand) > 21:
                            PlayerHand.append(-10 * playercount1)
                        elif sum(PlayerHand) > 21:
                            print("too many")
                            win_conditions()
    if sum(PlayerHand) > 21:
        playercount2 = (PlayerHand.count(Ace) - (playercount1 + playercount0))
        PlayerHand.append(-10 * playercount2)
        #print(playercount2)
        print("Player Hand total is", sum(PlayerHand))
    answer = input("Would you like another card?")
    if answer == "no":
        dealer()
        win_conditions()
    if answer == "yes":
        playercount2 = (PlayerHand.count(Ace) - playercount1)
        playercard3b = random.choice(Card_Value)
        playersuit3b = random.choice(Suits)
        PlayerHand.append(playercard3b)
        print("Players 3rd Card is", playercard3b, playersuit3b)
        print("Player Hand total is", sum(PlayerHand))
        if sum(PlayerHand) == 21:
            print("21 Well Done!")
            dealer()
            win_conditions()
        elif sum(PlayerHand) > 21:
            PlayerHand.append(-10 * playercount2)
        elif sum(PlayerHand) > 21:
            print("Player Hand total is", sum(PlayerHand))
            print("too many")
            win_conditions()
        else:
            print("Players Hand total is", sum(PlayerHand))
            answer = input("Would you like another card?")
            if answer == "no":
                dealer()
                win_conditions()
            if answer == "yes":
                playercard5b = random.choice(Card_Value)
                playersuit5b = random.choice(Suits)
                PlayerHand.append(playercard5b)
                print("Players 4th Card is", playercard5b, playersuit5b)
                if sum(PlayerHand) == 21:
                    print("21 Well Done!")
                    (dealer())
                    win_conditions()
                elif sum(PlayerHand) > 21:
                    PlayerHand.append(-10 * playercount2)
                    print("Player Hand total is", sum(PlayerHand))
                elif sum(PlayerHand) < 21:
                    print("Player Hand total is", sum(PlayerHand))
                elif sum(PlayerHand) > 21:
                    print("too many")
                    win_conditions()
    if sum(PlayerHand) > 21:
        playercount3 = (PlayerHand.count(Ace) - (playercount1 + playercount2))
        PlayerHand.append(-10 * playercount3)
        print(playercount3)
        #print("Player Hand total is", sum(PlayerHand))
    answer = input("Would you like another card?")
    if answer == "no":
        dealer()
        win_conditions()
    if answer == "yes":
        playercount3 = (PlayerHand.count(Ace) - (playercount1 + playercount2))
        playercard3c = random.choice(Card_Value)
        playersuit3c = random.choice(Suits)
        PlayerHand.append(playercard3b)
        print("Players 3rd Card is", playercard3c, playersuit3c)
        print("Player Hand total is", sum(PlayerHand))
        if sum(PlayerHand) == 21:
            print("21 Well Done!")
            dealer()
            win_conditions()
        elif sum(PlayerHand) > 21:
            PlayerHand.append(-10 * playercount3)
        elif sum(PlayerHand) > 21:
            print("Player Hand total is", sum(PlayerHand))
            print("too many")
            win_conditions()
        else:
            print("Players Hand total is", sum(PlayerHand))
            answer = input("Would you like another card?")
            if answer == "no":
                dealer()
                win_conditions()
            if answer == "yes":
                playercard5c = random.choice(Card_Value)
                playersuit5c = random.choice(Suits)
                PlayerHand.append(playercard5c)
                print("Players 4th Card is", playercard5c, playersuit5c)
                print("Player Hand total is", sum(PlayerHand))
                if sum(PlayerHand) == 21:
                    print("21 Well Done!")
                    (dealer())
                    win_conditions()
                elif sum(PlayerHand) > 21:
                    PlayerHand.append(-10 * playercount3)
                    print("Player Hand total is", sum(PlayerHand))
                elif sum(PlayerHand) < 21:
                    print("Player Hand total is", sum(PlayerHand))
                elif sum(PlayerHand) > 21:
                    print("too many")
                    win_conditions()
player()
win_conditions()



