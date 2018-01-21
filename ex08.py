# Rock Paper Scissors

choices = ["rock", "paper", "scissors"]
decisions = ["rematch", "exit"]


def get_decision():
    while True:
        choice = input("rematch or exit?")

        if choice in decisions:
            break

    return choice


def get_choice(user):
    while True:
        choice = input("%s, rock, paper or scissors?" % user)

        if choice in choices:
            break

    return choice


def play(u1, u2):
    if u1 == u2:
        return "Draw"
    elif u1 == "rock":
        if u2 == "scissors":
            return "Rock wins!"
        else:
            return "Paper wins!"
    elif u1 == "scissors":
        if u2 == "paper":
            return "Scissors win!"
        else:
            return "Rock wins!"
    elif u1 == "paper":
        if u2 == "rock":
            return "Paper wins!"
        else:
            return "Scissors win!"


while True:
    player1 = get_choice("Player 1")
    player2 = get_choice("Player 2")

    print(play(player1, player2))

    if get_decision() == "exit":
        break






