# 3 Jug Problem Solvers

A collection of Python implementations that solve the classic **3 Jug Problem** using various search algorithms. This project demonstrates solutions using:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **Iterative Deepening Search (IDS)**
- **Uniform Cost Search (UCS)**
- **Greedy Search**
- **A\* Search**

Each algorithm searches for a solution path from the initial state `(8, 0, 0)` (representing jugs with capacities 8L, 5L, and 3L) to the goal state `(4, 4, 0)`.

---

## License

```
Copyright (c) 2025 Muhammad Arhum
All rights reserved.

Unauthorized copying, modification, or distribution of this code, via any medium, is strictly prohibited without prior permission.

MuhammadArhum - 2025-03-08
```

## Contact

- **LinkedIn:** [MuhammadArhum](https://www.linkedin.com/in/MuhammadArhum)
- **GitHub:** [MuhammadArhumDev](https://github.com/MuhammadArhumDev)

---

## Table of Contents

- [Description](#description)
- [Algorithms Implemented](#algorithms-implemented)
- [Usage](#usage)
- [Output Format](#output-format)

---

## Description

The **3 Jug Problem** is a classic puzzle where you have three jugs with capacities 8L, 5L, and 3L. The goal is to measure exactly 4 liters of water in one of the jugs. This project applies six different search algorithms to find a solution path that satisfies the goal.

---

## Algorithms Implemented

1. **Breadth-First Search (BFS)**  
   Explores all nodes at the current depth before moving to the next level. Guarantees the shortest path in terms of moves.

2. **Depth-First Search (DFS)**  
   Explores as far as possible along one branch before backtracking. May not return the optimal solution but is simple and effective.

3. **Iterative Deepening Search (IDS)**  
   Combines DFS’s space efficiency with BFS’s optimality by gradually increasing the depth limit until the goal is found.

4. **Uniform Cost Search (UCS)**  
   Expands nodes based on the cumulative cost from the start. Since all moves have equal cost in this problem, UCS behaves similarly to BFS.

5. **Greedy Search**  
   Uses a heuristic function to guide the search towards the goal. It’s fast but not guaranteed to find the optimal solution.

6. **A\* Search**  
   Combines UCS and Greedy Search by using both the cumulative cost and a heuristic estimate of the remaining cost. With an admissible heuristic, it guarantees the optimal solution.

---

## Usage

### Prerequisites

- Python 3.x

### Running the Code

1. Clone or download this repository.
2. Navigate to the project directory.
3. Run the script using:

   ```bash
   python 3JUG_PROBLEM.py
   ```

---

## Output Format

The output will display the sequence of states from the initial state to the goal state for each algorithm. Each state is represented as a tuple `(jug1, jug2, jug3)`.

Example output for BFS:

```
=== BFS SOLUTION PATH ===
(8, 0, 0)  =>  (3, 5, 0)
(3, 5, 0)  =>  (3, 2, 3)
(3, 2, 3)  =>  (6, 2, 0)
(6, 2, 0)  =>  (6, 0, 2)
(6, 0, 2)  =>  (1, 5, 2)
(1, 5, 2)  =>  (1, 4, 3)
(1, 4, 3)  =>  (4, 4, 0)
```
