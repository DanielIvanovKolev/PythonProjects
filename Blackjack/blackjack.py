import deck
import player
import random
import computer

game_on = True

max_players = range(1, 6)

# List of players
# Every player object will be stored in this list!
players = []

# Random number of players for the game
num_of_players = random.randint(2, 4)
print(f"The game will be of {num_of_players} players!")

for x in range(0, num_of_players):
    print(f"Player number {x}")
    players.append(player.Player())

new_deck = deck.Deck()
new_deck.shuffle()

computer = computer.Computer(new_deck)

# Creating a list for the computer hand
computer_hand = []

while game_on:
    # Creating a list for the player bets
    player_bets = []

    folded_players = []

    # Players placing bets in a list
    print("\n\nPlayers please bet!")
    i = 0
    for player in players:
        print(f"\nPlayer {player.name} choose how much you want to bet: ")
        print("If you don't want to bet , type 0!")
        print("0, 1 ,5 ,10, 50, 100, 500, 1000")
        player_bets.append(player.bet())
        if player_bets[i] == 0:
            print(f"{player.name} has fold!")
            folded_players.append(i)
        i += 1

    temp_computer_list = []
    sum_of_comp = 0
    count = 0

    while True:
        choice = computer.hit()

        if choice.value + sum_of_comp > 21:
            break

        temp_computer_list.append(choice)
        sum_of_comp += temp_computer_list[count].value
        count += 1

    blackjack = True

    while blackjack:
        # Creating a list for the player values!
        value_list = []

        count = 0
        for player in players:
            temp_player_list = []
            sum_of_value = 0
            print(f"{player.name} it is your turn!")
            print("Your cards are: \n")
            for x in range(0, 2):
                temp_player_list.append(computer.hit())
                sum_of_value += temp_player_list[x].value
                print(f"{temp_player_list[x]} -> {temp_player_list[x].value}")

            print(f"The value of your cards is: {sum_of_value}")

            while True:

                choice = input("\nDo you want to hit or stand? : ")
                if choice.capitalize() == 'Hit':
                    new_card = computer.hit()
                    temp_player_list.append(new_card)
                    sum_of_value += new_card.value

                    print(f"And the new Card is: {temp_player_list[-1]}."
                          f"The new value is: {sum_of_value}")

                    if sum_of_value > 21:
                        print("BUST")
                        count += 1
                        value_list.append(sum_of_value)
                        break

                elif choice.capitalize() == 'Stand':
                    value_list.append(sum_of_value)
                    break

        print(f"The computer score is: {sum_of_comp}")
        count = 0
        for player in players:
            if value_list[count] > 21:
                print(f"\nSorry {player.name} you lose! "
                      f"Your balance is: {player.player_balance()}\n\n")
                count += 1

            elif value_list[count] > sum_of_comp:
                print(f"\n{player.name} good job, you won!")
                print(f"Your balance before win: {player.player_balance()} "
                      f"and after: {player.player_balance() + (player_bets[count] * 2)}")
                player.pot(player_bets[count] * 2)
                count += 1

            elif value_list[count] == sum_of_comp:
                print(f"\n{player.name} good job, you have the same score!")
                print(f"Your balance before win: {player.player_balance()} "
                      f"and after: {player.player_balance() + player_bets[count]}")
                player.pot(player_bets[count])
                count += 1
            else:
                print(f"\nSorry {player.name} you lose! "
                      f"Your balance is: {player.player_balance()}\n\n")
                count += 1

        choice_game = input("Do you want another game? (Y or N):")
        if choice_game.lower() == 'y':
            blackjack = False
        else:
            blackjack = False
            game_on = False

for player in players:
    print(f"\n{player.name} has {player.player_balance()} money!")



