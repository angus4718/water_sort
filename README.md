# Water Sort Puzzle Solver README

This repository contains an implementation of the **Water Sort Puzzle Solver** using the **A\* algorithm**. The Water Sort Puzzle is a logic-based game where the goal is to sort colored liquids into separate tubes. This solver uses heuristics to efficiently find solutions.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [How It Works](#how-it-works)
4. [Setup and Usage](#setup-and-usage)
5. [Configuration](#configuration)
6. [Outputs](#outputs)
7. [Limitations](#limitations)
8. [License](#license)

---

## Overview

The Water Sort Puzzle involves tubes containing stacks of colored liquids. The objective is to sort the liquids so that each tube contains only one color or is empty.

This Python implementation provides:
- A class for representing the puzzle state (`WaterSortPuzzle`).
- The **A\* algorithm** (`a_star_solver`) to find an optimal solution.
- A heuristic function to estimate the number of moves required to solve the puzzle.

---

## Features

- **Valid Move Detection**: Identifies legal moves based on the rules of the puzzle.
- **State Validation**: Checks if the puzzle is solved at any given state.
- **A\* Algorithm**:
  - Uses a priority queue to explore states with the lowest cost.
  - Incorporates a heuristic for efficient state exploration.
- **Undo Functionality**: Enables backtracking for testing purposes.
- **Customizable Puzzle Input**: Supports puzzles with any number of tubes and tube capacities.

---

## How It Works

### Puzzle Representation

The puzzle is represented as a list of tubes, where each tube is a list of strings. Each string is a color (e.g., `'R'` for red, `'Y'` for yellow), and empty spaces are represented as `''`. 

**Example Puzzle:**
```python
initial_tubes = [
    ['Y', 'R', 'R', 'R'],  # Tube 1
    ['Y', 'R', 'Y', 'Y'],  # Tube 2
    ['', '', '', ''],      # Tube 3 (empty)
    ['', '', '', '']       # Tube 4 (empty)
]
```

### A* Search Algorithm

The **A\* algorithm** is used to solve the puzzle:
1. **Initial State**: Start with the given puzzle configuration.
2. **Heuristic Function**: Estimates the number of moves needed to solve the puzzle by counting unsorted tubes and penalizing unsolved gaps.
3. **Priority Queue**: States are explored in order of their estimated cost (`actual cost + heuristic cost`).
4. **Valid Moves**: At each state, valid moves are generated and explored.
5. **Solution Check**: If the puzzle is solved, the path of moves is returned.

---

## Setup and Usage

### Prerequisites

- Python 3.7+ (No external libraries required).

### Running the Solver

1. Save the script as `water_sort_solver.py`.
2. Customize the initial puzzle in the `__main__` block.
3. Run the script:
   ```bash
   python water_sort_solver.py
   ```

### Example Input

```python
initial_tubes = [
    ['Y', 'R', 'R', 'R'],
    ['Y', 'R', 'Y', 'Y'],
    ['', '', '', ''],
    ['', '', '', '']
]
```

This represents a puzzle with 4 tubes, each with a capacity of 4. `'Y'` represents yellow, `'R'` represents red, and `''` represents an empty space.

---

## Configuration

You can customize the following:

1. **Initial Puzzle State**: Modify the `initial_tubes` variable in the `__main__` block. The number of tubes and their capacities can be adjusted as needed.

2. **Heuristic Function**: The heuristic function can be modified in the `heuristic` method of the `WaterSortPuzzle` class to experiment with different approaches for estimating the cost.

---

## Outputs

### Console Output

The script prints the following:

1. **Debug Information**: 
   - Current state of the puzzle.
   - Valid moves and their costs.
   - States being explored.

   Example:
   ```
   Current State: [['Y', 'R', 'R', 'R'], ['Y', 'R', 'Y', 'Y'], ['', '', '', ''], ['', '', '', '']], Cost: 0, Path: []
   Valid Moves: [(0, 2), (0, 3), (1, 2), (1, 3)]
   ```

2. **Solution Steps**:
   If a solution is found, the sequence of moves is displayed:
   ```
   Solution found!
   Step 1: Move from tube 1 to tube 3
   Step 2: Move from tube 2 to tube 4
   ...
   ```

3. **No Solution**:
   If no solution exists:
   ```
   No solution exists.
   ```

---

## Limitations

1. **Performance**: The A* algorithm may be slow for puzzles with many tubes or high complexity due to the large state space.
2. **Heuristic Accuracy**: The heuristic is simple and may not always lead to the most efficient solution.
3. **Valid Input**: The initial puzzle state must be well-formed (e.g., all tubes should have the same capacity, and colors must be properly defined).

---

## License

This project is open-source and free to use. Feel free to modify and distribute as needed!
