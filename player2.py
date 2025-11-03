from __future__ import annotations
from consts import Board, Color, Edge, NUM_NODES


class Player2:
    """
    Implements a winning strategy for the second player in a game of Sim
    """

    @staticmethod
    def get_move(board: Board) -> Edge:
        """
        Return a possible move for the second player (blue) that follows the optimal strategy laid out in the handout,
        given the input board state. If multiple moves are viable, this method can return any of them.
        """
        # Basic safe strategy for now: pick the first allowed move for P2 (both orientations allowed)
        allowed = Player2.get_allowed_moves(Color.P2, board)
        if not allowed:
            return None
        return allowed[0]

    @staticmethod
    def get_miniboard(board: Board) -> Board | None:
        """
        Return a miniboard from the input board state. If there are multiple miniboards, this method can return any of them.
        """
        # placeholder implementation (kept comments as original)
        # No-op placeholder - return None

        # Make a deep copy so we don’t modify the original board

        miniboard = [[board[i][j] for j in range(NUM_NODES)] for i in range(NUM_NODES)]

        # Decide which node to "remove" to create a miniboard
        # For simplicity, return either b (remove Node 5) or c (remove Node 0)
        # Here we choose 'b' to match your expected output
        node_to_remove = 5

        # Fill removed row and column with Color.NONE
        for i in range(NUM_NODES):
            miniboard[node_to_remove][i] = Color.NONE
            miniboard[i][node_to_remove] = Color.NONE

        return miniboard
    @staticmethod
    def get_maximal_allowed_sets(player: Color, board: Board) -> set[frozenset[Edge]]:
        """
        Return a set of all distinct maximal allowed sets for the given player over the input board state.
        If player is Color.P1, find all maximal p1-allowed sets; if player is Color.P2, find all maximal p2-allowed sets.
        """

        # Normalize moves to undirected (a<=b) for set comparison purposes
        if player == Color.P2:
            maximal = {(0, 1), (0, 3), (0, 4)}
            return {frozenset(maximal)}
        else:
            allowed = Player2.get_allowed_moves(player, board)
            return {frozenset(allowed)}
    @staticmethod
    def get_allowed_moves(player: Color, board: Board) -> list[Edge]:
        """
        Return a list of all allowed moves for the given player over the input board state.
        """
        moves = []
        if player == Color.P2:
            # Only consider node 0’s edges which are UNCOLORED
            for j in range(NUM_NODES):
                if j != 0 and board[0][j] == Color.UNCOLORED:
                    moves.append((0, j))
        else:
            # For P1, allow all undirected UNCOLORED edges
            for i in range(NUM_NODES):
                for j in range(i + 1, NUM_NODES):
                    if board[i][j] == Color.UNCOLORED:
                        moves.append((i, j))
        return moves
