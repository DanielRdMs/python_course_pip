import random


def choose_options():
    options = ('rock', 'paper', 'scissors')
    user_option = input('rock, paper or scissors => ')
    user_option = user_option.lower()

    if user_option not in options:
        print('The given option is not valid.')
        return None, None


    computer_option = random.choice(options)

    print('User option => ', user_option)
    print('Computer option => ', computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Draw!')
    elif user_option == 'rock':
        if computer_option == 'scissors':
            print('Rock wins over scissors...')
            print('Winner: User!')
            user_wins += 1
        else:
            print('Paper wins over rock...')
            print('Winner: Computer!')
            computer_wins += 1
    elif user_option == 'paper':
        if computer_option == 'rock':
            print('Paper wins over rock...')
            print('Winner: User!')
            user_wins += 1
        else:
            print('Scissors wins over paper...')
            print('Winner: Computer!')
            computer_wins += 1
    elif user_option == 'scissors':
        if computer_option == 'paper':
            print('Scissors wins over paper...')
            print('Winner: User!')
            user_wins += 1
        else:
            print('Roc wins over scissors...')
            print('Winner: Computer!')
            computer_wins += 1
    return user_wins, computer_wins


def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('Computer wins: ', computer_wins)
        print('User wins: ', user_wins)
        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        if computer_wins == 3:
            print('Computer wins this game!')
            break

        if user_wins == 3:
            print('User wins this game!')
            break


run_game()