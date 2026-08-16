from game import Connect4
from minimax import MinimaxAI



def print_title():

    print("=" * 45)
    print("             CONNECT 4 AI")
    print("       Human Player vs AI Agent")
    print("      Minimax with Alpha-Beta Pruning")
    print("=" * 45)


def get_player_move(game):
    while True:
        try:
            column = int(input("\nChoose a column (0-6): "))


            if column not in game.valid_moves():
                print("Invalid move! Choose another column.")
                continue
            return column
        except ValueError:


            print("Please enter a valid number.")







def play_game():
    print_title()
    print("\nGame Rules:")
    print("- Board size: 6 rows x 7 columns")
    print("- Connect four pieces to win")
    print("- Human = X")
    print("- AI    = O")
    game = Connect4()
    ai = MinimaxAI(depth=5)
    game.print_board()
    while True:
        player_move = get_player_move(game)
        game.make_move(
            player_move,
            Connect4.PLAYER
        )
        print("\nCurrent Board:")
        game.print_board()
        if game.check_winner(Connect4.PLAYER):
            print("\nCongratulations! You win!")
            break
        if game.is_full():
            print("\nGame Draw!")
            break
        print("\nAI is thinking...")
        ai_move = ai.get_best_move(
            game
        )
        game.make_move(
            ai_move,
            Connect4.AI
        )
        print(
            f"AI selected column: {ai_move}"
        )
        print(
            f"Nodes explored: {ai.nodes_explored}"
        )
        print("\nCurrent Board:")
        game.print_board()
        if game.check_winner(
            Connect4.AI
        ):
            print("\nAI wins! Better luck next time.")
            break





        if game.is_full():

            print(
                "\nGame Draw!"
            )

            break






if __name__ == "__main__":

    play_game()