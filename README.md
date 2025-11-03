# Sim Game - Optimal Strategy (DSC 395T Assignment)

This project implements the **Game of Sim**, a two-player graph-based game where players alternately color edges and aim to avoid forming a triangle of their own color. The goal is to implement the **optimal winning strategy** for the second player.

## Files
- `sim_board.py` — Manages the game board using an adjacency matrix.
- `player2.py` — Implements the optimal strategy for Player 2.
- `tests/` — Contains unit tests using **pytest**.

## How to Run
```bash
python sim_board.py
pytest
Rules Summary
6 nodes, all connected (complete graph).

Player 1: Red, Player 2: Blue.

First to complete a triangle of their own color loses.

Player 2 uses a deterministic winning strategy based on allowed and maximal allowed sets.

Requirements
Python 3.10+

pytest (for testing)