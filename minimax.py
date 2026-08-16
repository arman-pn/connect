from heuristic import evaluate_board
from game import Connect4

import math



class MinimaxAI:


    def __init__(self, depth=5):

        self.depth = depth
        self.nodes_explored = 0

    def get_best_move(self, game):


        self.nodes_explored = 0


        valid_moves = game.valid_moves()

        for col in valid_moves:


            game.make_move(
                col,
                Connect4.AI
            )


            if game.check_winner(
                Connect4.AI
            ):


                game.undo_move(col)

                return col



            game.undo_move(col)




        for col in valid_moves:


            game.make_move(
                col,
                Connect4.PLAYER
            )


            player_can_win = game.check_winner(
                Connect4.PLAYER
            )


            game.undo_move(col)



            if player_can_win:

                return col



        best_score = -math.inf
        best_move = None



        ordered_moves = self.order_moves(
            valid_moves
        )



        for col in ordered_moves:


            game.make_move(
                col,
                Connect4.AI
            )



            score = self.alpha_beta(
                game,
                self.depth - 1,
                -math.inf,
                math.inf,
                False
            )



            game.undo_move(col)



            if score > best_score:


                best_score = score
                best_move = col



        return best_move



    def alpha_beta(
            self,
            game,
            depth,
            alpha,
            beta,
            maximizing_player
    ):


        self.nodes_explored += 1


        if game.check_winner(
            Connect4.AI
        ):

            return 1000000 + depth




        if game.check_winner(
            Connect4.PLAYER
        ):

            return -1000000 - depth




        if game.is_full():

            return 0

        if depth == 0:

            return evaluate_board(game)





        moves = self.order_moves(
            game.valid_moves()
        )


        if maximizing_player:


            value = -math.inf



            for col in moves:



                game.make_move(
                    col,
                    Connect4.AI
                )



                value = max(
                    value,
                    self.alpha_beta(
                        game,
                        depth - 1,
                        alpha,
                        beta,
                        False
                    )
                )



                game.undo_move(col)



                alpha = max(
                    alpha,
                    value
                )



                if alpha >= beta:

                    break




            return value






        else:


            value = math.inf



            for col in moves:



                game.make_move(
                    col,
                    Connect4.PLAYER
                )



                value = min(
                    value,
                    self.alpha_beta(
                        game,
                        depth - 1,
                        alpha,
                        beta,
                        True
                    )
                )



                game.undo_move(col)



                beta = min(
                    beta,
                    value
                )



                if alpha >= beta:

                    break




            return value


    def order_moves(self, moves):


        center = 3


        return sorted(
            moves,
            key=lambda x: abs(center - x)
        )