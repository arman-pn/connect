from game import ROWS, COLS


AI_PLAYER = 2
HUMAN_PLAYER = 1



def evaluate_board(game):

    score = 0



    center_column = [
        game.board[row][COLS//2]
        for row in range(ROWS)
    ]


    center_count = center_column.count(AI_PLAYER)

    score += center_count * 6



    for row in range(ROWS):

        for col in range(COLS-3):

            window = [
                game.board[row][col+i]
                for i in range(4)
            ]

            score += evaluate_window(window)



    for col in range(COLS):

        for row in range(ROWS-3):

            window = [
                game.board[row+i][col]
                for i in range(4)
            ]

            score += evaluate_window(window)



    for row in range(ROWS-3):

        for col in range(COLS-3):

            window = [
                game.board[row+i][col+i]
                for i in range(4)
            ]

            score += evaluate_window(window)



    for row in range(3,ROWS):

        for col in range(COLS-3):

            window = [
                game.board[row-i][col+i]
                for i in range(4)
            ]

            score += evaluate_window(window)



    return score





def evaluate_window(window):


    score = 0


    ai_count = window.count(AI_PLAYER)

    human_count = window.count(HUMAN_PLAYER)

    empty_count = window.count(0)



  

    if ai_count == 4:

        score += 100000




    elif ai_count == 3 and empty_count == 1:

        score += 100




    elif ai_count == 2 and empty_count == 2:

        score += 10



    if human_count == 3 and empty_count == 1:

        score -= 120



    elif human_count == 2 and empty_count == 2:

        score -= 15



    return score