import tkinter as tk
from tkinter import messagebox

from game import Connect4
from minimax import MinimaxAI



class Connect4GUI:


    ROWS = 6
    COLS = 7

    CELL_SIZE = 85
    BG_COLOR = "#0F172A"
    PANEL_COLOR = "#111827"
    BOARD_COLOR = "#1E3A5F"

    TEXT_COLOR = "#E5E7EB"
    ACCENT_COLOR = "#38BDF8"

    HUMAN_COLOR = "#EF4444"
    AI_COLOR = "#FACC15"

    SHADOW_COLOR = "#020617"

    def __init__(self):


        self.window = tk.Tk()

        self.window.title("Connect 4 AI - Alpha Beta")
        self.window.geometry("760x650")
        self.window.configure(
            bg=self.BG_COLOR
        )



        self.game = Connect4()


        self.ai = MinimaxAI(
            depth=5
        )


        self.create_ui()


        self.draw_board()


    def create_ui(self):


        title = tk.Label(

            self.window,

            text="CONNECT 4 AI",

            font=(
                "Arial",
                28,
                "bold"
            ),

            fg=self.ACCENT_COLOR,

            bg=self.BG_COLOR

        )


        title.pack(
            pady=15
        )



        subtitle = tk.Label(

            self.window,

            text="Minimax + Alpha Beta Pruning",

            font=(
                "Arial",
                12
            ),

            fg=self.TEXT_COLOR,

            bg=self.BG_COLOR

        )


        subtitle.pack()



        container = tk.Frame(

            self.window,

            bg=self.BG_COLOR

        )


        container.pack(
            pady=20
        )




        self.canvas = tk.Canvas(

            container,

            width=self.COLS*self.CELL_SIZE,

            height=self.ROWS*self.CELL_SIZE,

            bg=self.BOARD_COLOR,

            highlightthickness=0

        )


        self.canvas.grid(
            row=0,
            column=0,
            padx=20
        )


        self.canvas.bind(
            "<Button-1>",
            self.player_click
        )



        panel = tk.Frame(

            container,

            bg=self.PANEL_COLOR,

            width=220,

            height=500

        )


        panel.grid(
            row=0,
            column=1,
            sticky="ns"
        )




        self.status_label = tk.Label(

            panel,

            text="Your Turn",

            font=(
                "Arial",
                15,
                "bold"
            ),

            fg=self.ACCENT_COLOR,

            bg=self.PANEL_COLOR

        )


        self.status_label.pack(
            pady=25
        )





        difficulty_title = tk.Label(

            panel,

            text="Difficulty",

            font=(
                "Arial",
                13,
                "bold"
            ),

            fg=self.ACCENT_COLOR,

            bg=self.PANEL_COLOR

        )


        difficulty_title.pack(
            pady=10
        )




        self.difficulty = tk.StringVar(
            value="Medium"
        )



        difficulties = [

            ("Easy",3),

            ("Medium",5),

            ("Hard",7)

        ]



        for name,depth in difficulties:


            tk.Radiobutton(

                panel,

                text=name,

                variable=self.difficulty,

                value=name,

                command=lambda d=depth:self.change_depth(d),

                font=(
                    "Arial",
                    11
                ),

                fg=self.TEXT_COLOR,

                bg=self.PANEL_COLOR,

                activebackground=self.PANEL_COLOR,

                activeforeground=self.ACCENT_COLOR,

                selectcolor=self.PANEL_COLOR

            ).pack(
                pady=5
            )






        self.info_label = tk.Label(

            panel,

            text=
            """
Human : Red

AI : Yellow

Connect 4 pieces
to win
            """,

            font=(
                "Arial",
                10
            ),

            fg=self.TEXT_COLOR,

            bg=self.PANEL_COLOR

        )


        self.info_label.pack(
            pady=20
        )





        restart = tk.Button(

            panel,

            text="NEW GAME",

            command=self.restart,

            width=15,

            height=2,

            bg="#2563EB",

            fg="white",

            font=(
                "Arial",
                11,
                "bold"
            )

        )


        restart.pack(
            pady=20
        )

    def draw_board(self):


        self.canvas.delete(
            "all"
        )


        for row in range(self.ROWS):

            for col in range(self.COLS):


                x1 = col*self.CELL_SIZE

                y1 = row*self.CELL_SIZE


                x2 = x1+self.CELL_SIZE

                y2 = y1+self.CELL_SIZE



                value = self.game.board[row][col]



                self.canvas.create_oval(

                    x1+10,

                    y1+12,

                    x2-5,

                    y2-3,

                    fill=self.SHADOW_COLOR,

                    outline=""

                )




                color = self.BG_COLOR



                if value == Connect4.PLAYER:

                    color = self.HUMAN_COLOR



                elif value == Connect4.AI:

                    color = self.AI_COLOR




                self.canvas.create_oval(

                    x1+8,

                    y1+8,

                    x2-8,

                    y2-8,

                    fill=color,

                    outline=""

                )



    def player_click(self,event):


        column = event.x // self.CELL_SIZE



        if column not in self.game.valid_moves():

            return



        self.game.make_move(

            column,

            Connect4.PLAYER

        )



        self.draw_board()



        if self.game.check_winner(
            Connect4.PLAYER
        ):

            self.end_game(
                "You Win!"
            )

            return




        if self.game.is_full():

            self.end_game(
                "Draw Game"
            )

            return




        self.status_label.config(
            text="AI Thinking..."
        )


        self.window.after(
            500,
            self.ai_move
        )




    def ai_move(self):


        move = self.ai.get_best_move(

            self.game

        )



        if move is not None:

            self.game.make_move(

                move,

                Connect4.AI

            )



        self.draw_board()



        self.status_label.config(
            text="Your Turn"
        )



        if self.game.check_winner(
            Connect4.AI
        ):

            self.end_game(
                "AI Wins!"
            )



        elif self.game.is_full():

            self.end_game(
                "Draw Game"
            )




    def change_depth(self, depth):

        self.ai.depth = depth




    def restart(self):


        self.game = Connect4()


        self.draw_board()


        self.status_label.config(
            text="Your Turn"
        )






    def end_game(self,message):


        messagebox.showinfo(

            "Game Over",

            message

        )


        self.restart()






    def run(self):

        self.window.mainloop()






if __name__ == "__main__":


    app = Connect4GUI()

    app.run()