import copy
import heapq

class WaterSortPuzzle:
    def __init__(self, tubes):
        """
        Initialize the puzzle with the given tubes.
        Each tube is represented as a list of colors (strings).
        Empty spaces are represented as an empty string ''.
        """
        self.tubes = tubes
        self.num_tubes = len(tubes)
        self.tube_capacity = len(tubes[0])  # Assume all tubes have the same capacity

    def is_solved(self):
        """
        Check if the puzzle is solved.
        A tube is solved if it's empty or contains only one color.
        """
        for tube in self.tubes:
            if len(set(tube)) > 1:  # More than one unique color
                return False
        return True

    def get_valid_moves(self):
        """
        Generate all valid moves as (from_tube, to_tube) pairs.
        A move is valid if:
        - The from_tube is not empty.
        - The to_tube is not full and is either empty or has the same color on top as the from_tube.
        """
        moves = []
        for from_tube in range(self.num_tubes):
            # Skip empty tubes
            if not any(color != '' for color in self.tubes[from_tube]):
                continue

            # Find the top color of the from_tube
            from_color = None
            for color in reversed(self.tubes[from_tube]):
                if color != '':
                    from_color = color
                    break

            # Check all possible to_tube destinations
            for to_tube in range(self.num_tubes):
                if from_tube == to_tube:
                    continue

                # Check if the to_tube is empty
                if not any(color != '' for color in self.tubes[to_tube]):
                    moves.append((from_tube, to_tube))
                    continue

                # Find the top color of the to_tube
                to_color = None
                for color in reversed(self.tubes[to_tube]):
                    if color != '':
                        to_color = color
                        break

                # Check if the move is valid
                if to_color == from_color and self.tubes[to_tube].count('') > 0:
                    moves.append((from_tube, to_tube))

        return moves

    def apply_move(self, move):
        """
        Apply a move (from_tube, to_tube) to the puzzle.
        This updates the state of the tubes and moves multiple
        consecutive colors if possible.
        """
        from_tube, to_tube = move

        # Find the top color and how many consecutive colors can be moved
        from_color = None
        num_to_move = 0

        # Identify the top color and count consecutive occurrences
        for i in range(len(self.tubes[from_tube]) - 1, -1, -1):
            if self.tubes[from_tube][i] != '':
                if from_color is None:
                    from_color = self.tubes[from_tube][i]
                    num_to_move = 1
                elif self.tubes[from_tube][i] == from_color:
                    num_to_move += 1
                else:
                    break

        # Check the number of empty slots in the destination tube
        empty_slots = self.tubes[to_tube].count('')

        # Only move as many colors as the destination tube can handle
        num_to_move = min(num_to_move, empty_slots)

        # Perform the move
        for _ in range(num_to_move):
            # Remove from the source tube
            for i in range(len(self.tubes[from_tube]) - 1, -1, -1):
                if self.tubes[from_tube][i] != '':
                    color = self.tubes[from_tube][i]
                    self.tubes[from_tube][i] = ''
                    break

            # Add to the destination tube
            for i in range(len(self.tubes[to_tube])):
                if self.tubes[to_tube][i] == '':
                    self.tubes[to_tube][i] = color
                    break

    def undo_move(self, move, color):
        """
        Undo a move by moving the color back to the original tube.
        """
        from_tube, to_tube = move

        # Remove the color from the to_tube
        for i in range(len(self.tubes[to_tube]) - 1, -1, -1):
            if self.tubes[to_tube][i] != '':
                self.tubes[to_tube][i] = ''
                break

        # Restore the color to the from_tube
        for i in range(len(self.tubes[from_tube])):
            if self.tubes[from_tube][i] == '':
                self.tubes[from_tube][i] = color
                break

    def heuristic(self):
        """
        Heuristic function for A*.
        The heuristic estimates the number of moves needed to solve the puzzle.
        A simple heuristic is to count the number of unsorted tubes.
        """
        cost = 0
        for tube in self.tubes:
            # Count the number of unique colors in the tube
            unique_colors = set([color for color in tube if color != ''])
            if len(unique_colors) > 1:  # Mixed colors in a tube
                cost += len(unique_colors) - 1
            # Penalize empty spaces in unsolved tubes
            if '' in tube and len(unique_colors) > 0:
                cost += tube.count('')
        return cost


def a_star_solver(puzzle):
    """
    Solve the Water Sort Puzzle using the A* algorithm.
    """
    initial_state = copy.deepcopy(puzzle.tubes)
    priority_queue = []  # Min-heap for A* (priority, cost, state)
    heapq.heappush(priority_queue, (0, 0, initial_state, []))  # (priority, cost, state, path)
    visited_states = set()

    while priority_queue:
        # Pop state with the lowest priority
        _, cost, current_state, path = heapq.heappop(priority_queue)

        # Debug: Current state and cost
        print(f"Current State: {current_state}, Cost: {cost}, Path: {path}")

        # Convert current state to a tuple of tuples to hash it
        state_tuple = tuple(tuple(tube) for tube in current_state)
        if state_tuple in visited_states:
            print("State already visited, skipping.")
            continue
        visited_states.add(state_tuple)

        # Check if the current state is a solution
        puzzle.tubes = copy.deepcopy(current_state)
        if puzzle.is_solved():
            print("Solution found!")
            return path  # Return the path of moves to solve the puzzle

        # Generate valid moves and explore them
        valid_moves = puzzle.get_valid_moves()
        print(f"Valid Moves: {valid_moves}")
        for move in valid_moves:
            puzzle.tubes = copy.deepcopy(current_state)
            puzzle.apply_move(move)
            new_state = copy.deepcopy(puzzle.tubes)

            # Debug: Move and resulting state
            print(f"Applying Move: {move}")
            print(f"Resulting State: {new_state}")

            move_cost = 1  # Each move has a uniform cost of 1
            heuristic_cost = puzzle.heuristic()
            total_cost = cost + move_cost + heuristic_cost
            new_path = path + [move]

            # Debug: Costs and heuristic
            print(f"Move Cost: {move_cost}, Heuristic Cost: {heuristic_cost}, Total Cost: {total_cost}")

            heapq.heappush(priority_queue, (total_cost, cost + move_cost, new_state, new_path))

    print("No solution found.")
    return None  # No solution found


# Example Usage
if __name__ == "__main__":
    # Example puzzle: 4 tubes, each with a capacity of 4
    # Note: '' represents empty space
    initial_tubes = [
        ['Y', 'R', 'R', 'R'],
        ['Y', 'R', 'Y', 'Y'],
        ['', '', '', ''],
        ['', '', '', '']
    ]

    puzzle = WaterSortPuzzle(initial_tubes)
    solution = a_star_solver(puzzle)

    if solution:
        print("Solution found!")
        for step, move in enumerate(solution, start=1):
            print(f"Step {step}: Move from tube {move[0] + 1} to tube {move[1] + 1}")
    else:
        print("No solution exists.")