# Sim Game Optimal Strategy

This project implements the optimal strategy for the 2-player Game of Sim, as assigned in the DSC 395T Algorithms and Data Structures course.

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Implementation Details](#implementation-details)
- [File Structure](#file-structure)
- [License](#license)
- [Credits](#credits)

## About the Project

Sim is a pen-and-paper game for two players, played on a graph of 6 nodes where each player colors edges in turns. The goal is to avoid forming a triangle with all edges of one’s own color, and research shows the second player can always force a win with the correct moves[attached_file:1].

This repository provides:
- A full board management system.
- An agent guaranteeing the second player's win via optimal strategy.

## Features

- Board state managed by adjacency matrix
- Comprehensive assistant bot for the second player (blue)
- Functions to extract allowed moves, maximal sets, and miniboards
- Strict adherence to mathematically optimal play

## Getting Started

### Prerequisites

You will need:
- Python (only standard library required)
- Pytest (for running tests)

### Installation

Clone the repository:
