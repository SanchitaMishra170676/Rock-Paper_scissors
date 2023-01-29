import random
choiceList = ['r', 'p', 's']

def botChoice():
    '''Chooses random item from choiceList for the bot'''
    return random.choice(choiceList)

def validateInput(player = 'x'):
    '''Validates user Input'''
    if player == 'r' or player == 'p' or player == 's':
        return True
    return False

def winner(bot,player):
    '''Program Logic to decide the winner'''
    if player == 'r':
        if bot == 's':
            return "You win!"
        elif bot == 'p':
            return "You Lose!"
        else:
            return "Oops Draw!"
    elif player == 'p':
        if bot == 'r':
            return "You win!"
        elif bot == 's':
            return "You Lose!"
        else:
            return "Oops Draw!"
    else:
        if bot == 'p':
            return "You win!"
        elif bot == 'r':
            return 'you lose!'
        else:
            return "Oops Draw!"
    
# will continuously run the game until explicitly terminated
while True:
    bot = botChoice()
    print("Bot choosing from rock, paper or scissors.\n It's your turn now")
    player = (input("Enter r for rock, s scissors, p for paper:\n")).lower()

    if validateInput(player):
        print("**********\n",winner(bot,player),"\n**********")
        print(f"You chose {player}, bot chose {bot}")
    else:
        print("Invalid Choice")
