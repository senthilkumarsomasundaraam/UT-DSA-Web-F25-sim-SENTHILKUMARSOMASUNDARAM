from __future__ import annotations
from consts import Board, Color, Edge, NUM_NODES


class GameBoard:
    """
    Game board manager class. Encapsulates behaviors concerning the state of the board.
    """

    def __init__(self):
        """
        Initialize `board` as the adjacency matrix for the starting board.
        Use `Color.NONE` for edges that do not exist, and `Color.UNCOLORED` for the other edges.
        """
        self.board: Board = []
        for i in range(NUM_NODES):
            row = []
            for j in range(NUM_NODES):
                if i == j:
                    row.append(Color.NONE)
                else:
                    row.append(Color.UNCOLORED)
            self.board.append(row)

    def color_edge(self, edge: Edge, color: Color) -> None:
        """
        Update `board` to reflect coloring the given edge.
        """
        a, b = edge
        self.board[a][b] = color
        self.board[b][a] = color

    def get_winner(self) -> Color | None:
        """
        Return the color of the player that has won (Color.P1 or Color.P2).
        If the game is still in progress (no one has won yet), return None.
        """
        # Check all triples for a monochromatic triangle
        for i in range(NUM_NODES):
            for j in range(i + 1, NUM_NODES):
                for k in range(j + 1, NUM_NODES):
                    c1 = self.board[i][j]
                    c2 = self.board[j][k]
                    c3 = self.board[i][k]
                    if c1 == c2 == c3 and (c1 == Color.P1 or c1 == Color.P2):
                        # The player who forms a triangle loses, so the opponent wins
                        return Color.P1 if c1 == Color.P2 else Color.P2
        return None

    def __str__(self):
        """
        Formats the board as a string. Provided for your convenience while debugging.
        """
        string = ""
        for row in self.board:
            for item in row:
                string += "{edge:<10}".format(edge=item.name)
            string += "\n"
        return string
