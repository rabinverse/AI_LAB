# 8-Puzzle solver

import tkinter as tk
from tkinter import messagebox
import numpy as np
from collections import deque


# PuzzleState and BFS code (same as above)
class PuzzleState:
    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.parent = parent
        self.move = move
        self.blank_pos = self.find_blank()

    def find_blank(self):
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                if val == 0:
                    return (i, j)

    def generate_successors(self):
        successors = []
        x, y = self.blank_pos
        directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }
        for move, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = np.copy(self.board)
                new_board[x, y], new_board[nx, ny] = new_board[nx, ny], new_board[x, y]
                successors.append(PuzzleState(new_board, self, move))
        return successors

    def __eq__(self, other):
        return np.array_equal(self.board, other.board)

    def __hash__(self):
        return hash(self.board.tobytes())


def bfs(initial_board, goal_board):
    initial_state = PuzzleState(initial_board)
    queue = deque([initial_state])
    visited = set()
    visited.add(initial_state)

    while queue:
        current_state = queue.popleft()
        if np.array_equal(current_state.board, goal_board):
            return reconstruct_path(current_state)

        for successor in current_state.generate_successors():
            if successor not in visited:
                visited.add(successor)
                queue.append(successor)

    return None


def reconstruct_path(state):
    path = []
    while state.parent:
        path.append((state.move, state.board))
        state = state.parent
    path.append(("Start", state.board))
    return path[::-1]


# Tkinter GUI
class PuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Puzzle Solver")
        self.initial_board = np.array([[1, 8, 3], [4, 6, 7], [2, 0, 5]])
        self.goal_board = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        self.tiles = {}
        self.create_widgets()

    def create_widgets(self):
        # Create the board grid
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        for i in range(3):
            for j in range(3):
                tile = tk.Label(
                    self.frame,
                    text="",
                    width=4,
                    height=2,
                    font=("Arial", 24),
                    bg="lightblue",
                    relief="raised",
                )
                tile.grid(row=i, column=j, padx=5, pady=5)
                self.tiles[(i, j)] = tile

        # Buttons
        self.init_button = tk.Button(
            self.root,
            text="Initialize",
            command=self.initialize_board,
            font=("Arial", 14),
        )
        self.init_button.pack(pady=10)

        self.solve_button = tk.Button(
            self.root, text="Solve", command=self.solve_puzzle, font=("Arial", 14)
        )
        self.solve_button.pack(pady=10)

    def initialize_board(self):
        """Initialize the board with the initial state."""
        self.update_board(self.initial_board)

    def update_board(self, board):
        """Update the Tkinter board based on the numpy array."""
        for i in range(3):
            for j in range(3):
                value = board[i, j]
                if value == 0:
                    self.tiles[(i, j)].config(text="", bg="white")
                else:
                    self.tiles[(i, j)].config(text=str(value), bg="lightblue")

    def solve_puzzle(self):
        """Solve the puzzle and animate the solution."""
        solution_path = bfs(self.initial_board, self.goal_board)
        if solution_path:
            self.animate_solution(solution_path)
        else:
            messagebox.showerror("Error", "No solution exists.")

    def animate_solution(self, solution_path):
        """Animate the solution moves."""

        def animate_step(step):
            move, board = step
            self.update_board(board)
            if move != "Start":
                self.root.update()
                self.root.after(500)  # Pause for animation

        for step in solution_path:
            self.root.after(500, animate_step(step))


# Run the Tkinter GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleGUI(root)
    root.mainloop()
