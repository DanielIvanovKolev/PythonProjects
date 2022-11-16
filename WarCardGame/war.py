import card
import deck
import player

def main():
    player_one = player.Player("One")
    player_two = player.Player("Two")

    # Creating and shuffling a deck of cards
    new_deck = deck.Deck()
    new_deck.shuffle()

    # Splitting the deck between the players
    for x in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    # Bool for the game
    game_on = True

    # Counter for the rounds
    round_num = 0

    while game_on:
        round_num += 1

        # The cards that are going to be on the table
        player_one_cards = []
        player_two_cards = []

        print(f"Round {round_num}")

        # Printing the cards of each player after each round
        print(f"Player One has: {len(player_one.all_cards) + len(player_one_cards)} cards"
              f"\nPlayer Two has: {len(player_two.all_cards) + len(player_two_cards)} cards")

        # Checking if one of the two players have won
        if len(player_one.all_cards) == 0:
            print("Player One, out of cards! Player Two Wins!")
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            print("Player Two, out of cards! Player One Wins!")
            game_on = False
            break

        # Start a new round

        # The cards that player will leave on the table

        player_one_cards.append(player_one.remove_one())
        player_two_cards.append(player_two.remove_one())

        # While at war

        war = True

        while war:
            # We are using -1 for this purpose:
            # so if we have a war [Q] the player have to draw
            # 3 more cards and the list of player_one_cards will look like
            # that [Q, K, J, 2] and basically if we don't use -1
            # we are going to check [Q] vs [Q] every time
            # so that's why we use -1 to check the last element
            # in the list!!!

            if player_one_cards[-1].value > player_two_cards[-1].value:

                player_one.add_cards(player_one_cards)  # Adding the player one cards
                player_one.add_cards(player_two_cards)  # and adding the opponent cards to player 1 deck

                war = False

            elif player_two_cards[-1].value > player_one_cards[-1].value:

                player_two.add_cards(player_two_cards)
                player_two.add_cards(player_one_cards)

                war = False

            else:
                print("\nWAR!\n")

                if len(player_one.all_cards) < 3:
                    print("Player One unable to declare war!\n")
                    print("Player Two Wins!")
                    game_on = False
                    break
                elif len(player_two.all_cards) < 3:
                    print("Player Two unable to declare war!\n")
                    print("Player One Wins!")
                    game_on = False
                    break
                else:
                    for num in range(3):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

                ##############################################
                # Showing the war at action!!!
                ##############################################

                print(f"The cards that start the war are:"
                      f"\nFor player one: {player_one_cards[0]}"
                      f"\nAnd for player two: {player_two_cards[0]}\n")

                print(f"Player One cards:")
                for card in player_one_cards:
                    if card == player_one_cards[-1]:
                        print("And the last card is: {}".format(card))
                    else:
                        print(card)

                print("\n VS \n")

                print(f"Player Two cards:")
                for card in player_two_cards:
                    if card == player_two_cards[-1]:
                        print("And the last card is: {}".format(card))
                    else:
                        print(card)

                if player_one_cards[-1].value > player_two_cards[-1].value:
                    print("\nPLAYER ONE WON THE WAR! CONTINUING...\n")

                elif player_two_cards[-1].value > player_one_cards[-1].value:
                    print("\nPLAYER TWO WON THE WAR! CONTINUING...\n")

                else:
                    continue


if __name__ == "__main__":
    main()
