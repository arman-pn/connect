ROWS = 6
COLS = 7


class Connect4:

    EMPTY = 0
    PLAYER = 1
    AI = 2


    def __init__(self):

        self.board = [
            [self.EMPTY for _ in range(COLS)]
            for _ in range(ROWS)
        ]



    def print_board(self):

        symbols = {
            self.EMPTY: ".",
            self.PLAYER: "X",
            self.AI: "O"
        }


        print()

        for row in self.board:

            print(
                "| " +
                " | ".join(
                    symbols[cell]
                    for cell in row
                )
                +
                " |"
            )


        print(
            "  0   1   2   3   4   5   6"
        )

        print()



    def valid_moves(self):

        moves = []

        for col in range(COLS):

            if self.board[0][col] == self.EMPTY:

                moves.append(col)


        return moves




    def make_move(self, col, player):


        if col not in self.valid_moves():

            return False



        for row in range(
            ROWS - 1,
            -1,
            -1
        ):

            if self.board[row][col] == self.EMPTY:

                self.board[row][col] = player

                return True



        return False





    def undo_move(self, col):


        for row in range(ROWS):

            if self.board[row][col] != self.EMPTY:

                self.board[row][col] = self.EMPTY

                break





    def get_next_states(self, player):

        """
        Generate all possible next states.

        Returns:
            [
              (column, new_game_state)
            ]
        """


        states = []


        for col in self.valid_moves():

            new_game = self.copy()


            new_game.make_move(
                col,
                player
            )


            states.append(
                (
                    col,
                    new_game
                )
            )


        return states






    def is_full(self):

        return len(
            self.valid_moves()
        ) == 0






    def check_winner(self, player):



        for r in range(ROWS):

            for c in range(COLS - 3):

                if (
                    self.board[r][c] == player and
                    self.board[r][c+1] == player and
                    self.board[r][c+2] == player and
                    self.board[r][c+3] == player
                ):

                    return True



        for r in range(ROWS - 3):

            for c in range(COLS):

                if (
                    self.board[r][c] == player and
                    self.board[r+1][c] == player and
                    self.board[r+2][c] == player and
                    self.board[r+3][c] == player
                ):

                    return True




        for r in range(ROWS - 3):

            for c in range(COLS - 3):

                if (
                    self.board[r][c] == player and
                    self.board[r+1][c+1] == player and
                    self.board[r+2][c+2] == player and
                    self.board[r+3][c+3] == player
                ):

                    return True


        for r in range(3, ROWS):

            for c in range(COLS - 3):

                if (
                    self.board[r][c] == player and
                    self.board[r-1][c+1] == player and
                    self.board[r-2][c+2] == player and
                    self.board[r-3][c+3] == player
                ):

                    return True



        return False






    def game_over(self):

        return (
            self.check_winner(self.PLAYER)
            or
            self.check_winner(self.AI)
            or
            self.is_full()
        )






    def copy(self):

        new_game = Connect4()


        new_game.board = [
            row.copy()
            for row in self.board
        ]


        return new_game