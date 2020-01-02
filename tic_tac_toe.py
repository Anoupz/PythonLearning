class TicTacToe:
    """
    Build the tic tac toe game

     # board
     # display game
     # play game
     # handle turn
     # check win
        # check rows
        # check columns
        # check diagonals
     # check tie
     # flip player
    """

    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    game_still_going = True
    current_player = "X"
    winner = None

    def display_board(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def play_game(self):
        # display initial self.board
        self.display_board()
        while self.game_still_going:
            self.handle_turn(self.current_player)
            self.check_if_game_over()
            self.flip_player(self.current_player)

            # The game has ended
            if self.winner == "X" or self.winner == "O":
                print("Winner is " + self.winner)
            elif self.winner is None and not self.game_still_going:
                print("Tie.")

    def check_if_game_over(self):
        self.check_for_winner()
        self.check_if_tie()

    def check_for_winner(self):
        # check rows
        row_winner = self.check_rows()
        # check columns
        column_winner = self.check_columns()
        # check diagonals
        diagonal_winner = self.check_diagonals()

        if row_winner:
            self.winner = row_winner
        elif column_winner:
            self.winner = column_winner
        elif diagonal_winner:
            self.winner = diagonal_winner
        else:
            self.winner = None
        return

    def check_rows(self):
        row_1 = self.board[0] == self.board[1] == self.board[2] != "-"
        row_2 = self.board[3] == self.board[4] == self.board[5] != "-"
        row_3 = self.board[6] == self.board[7] == self.board[8] != "-"

        if row_1 or row_2 or row_3:
            self.game_still_going = False

        if row_1:
            return self.board[0]
        elif row_2:
            return self.board[3]
        elif row_3:
            return self.board[6]

        return

    def check_columns(self):
        column_1 = self.board[0] == self.board[3] == self.board[6] != "-"
        column_2 = self.board[1] == self.board[4] == self.board[7] != "-"
        column_3 = self.board[2] == self.board[5] == self.board[8] != "-"

        if column_1 or column_2 or column_3:
            self.game_still_going = False

        if column_1:
            return self.board[0]
        elif column_2:
            return self.board[1]
        elif column_3:
            return self.board[2]

        return

    def check_diagonals(self):
        diagonals_1 = self.board[0] == self.board[4] == self.board[8] != "-"
        diagonals_2 = self.board[2] == self.board[4] == self.board[6] != "-"

        if diagonals_1 or diagonals_2:
            self.game_still_going = False

        if diagonals_1:
            return self.board[0]
        elif diagonals_2:
            return self.board[2]

        return

    def check_if_tie(self):
        return

    def flip_player(self, player):
        if player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
        return

    def handle_turn(self, player):
        # get user input
        position = input("Choose a position between 1 to 9 : ")
        position = int(position) - 1
        self.board[position] = player
        self.display_board()


def main():
    game = TicTacToe()
    game.play_game()


if __name__ == "__main__":
    main()
