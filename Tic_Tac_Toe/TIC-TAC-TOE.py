import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # Initialize an empty board
        self.human_player = "X"
        self.ai_player = "O"

    def print_board(self):
        for row in [self.board[i:i+3] for i in range(0, 9, 3)]:
            print("|", " | ".join(row), "|")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, position, player):
        self.board[position] = player

    def check_winner(self, player):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            # Check rows
            if all(self.board[i*3 + j] == player for j in range(3)):
                return True
            # Check columns
            if all(self.board[i + j*3] == player for j in range(3)):
                return True
        # Check diagonals
        if all(self.board[i] == player for i in [0, 4, 8]) or all(self.board[i] == player for i in [2, 4, 6]):
            return True
        return False

    def check_draw(self):
        return " " not in self.board

    def game_over(self):
        return self.check_winner(self.human_player) or self.check_winner(self.ai_player) or self.check_draw()

    def minimax(self, depth, maximizing_player):
        if self.check_winner(self.human_player):
            return -1
        if self.check_winner(self.ai_player):
            return 1
        if self.check_draw():
            return 0

        if maximizing_player:
            max_eval = -math.inf
            for move in self.available_moves():
                self.make_move(move, self.ai_player)
                eval = self.minimax(depth + 1, False)
                self.make_move(move, " ")
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = math.inf
            for move in self.available_moves():
                self.make_move(move, self.human_player)
                eval = self.minimax(depth + 1, True)
                self.make_move(move, " ")
                min_eval = min(min_eval, eval)
            return min_eval

    def get_best_move(self):
        best_move = None
        best_eval = -math.inf
        for move in self.available_moves():
            self.make_move(move, self.ai_player)
            eval = self.minimax(0, False)
            self.make_move(move, " ")
            if eval > best_eval:
                best_eval = eval
                best_move = move
        return best_move

    def play(self):
        print("Welcome to Tic-Tac-Toe! You are 'X', and the AI is 'O'.")
        while not self.game_over():
            self.print_board()

            # Human player's turn
            try:
                human_move = int(input("Enter your move (1-9): ")) - 1
                if self.board[human_move] == " ":
                    self.make_move(human_move, self.human_player)
                else:
                    print("Invalid move. The spot is already taken.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            if self.game_over():
                break

            # AI player's turn
            ai_move = self.get_best_move()
            print(f"\nAI plays at position {ai_move + 1}")
            self.make_move(ai_move, self.ai_player)

        self.print_board()
        if self.check_winner(self.human_player):
            print("Congratulations! You win!")
        elif self.check_winner(self.ai_player):
            print("AI wins! Better luck next time.")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
