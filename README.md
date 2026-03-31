# Pac-Man AI: A* Pathfinding & Heuristic Search

## Overview
An AI agent for Pac-Man developed to solve complex navigation and pathfinding problems. This project implements fundamental AI search algorithms, focusing on highly optimized **A* (A-Star) Search** and the design of admissible, consistent heuristics.

## Core Implementations
* **Search Algorithms (`search.py`):** Implemented Depth-First Search (DFS), Breadth-First Search (BFS), Uniform Cost Search (UCS), and A* Search.
* **Custom Heuristics (`searchAgents.py`):**
  * **Corners Problem:** Designed a heuristic to find the shortest path to visit all four corners of the maze efficiently.
  * **Food Search Problem:** Developed an advanced heuristic to compute the optimal path to eat all dots in the shortest time possible, drastically reducing the number of expanded nodes compared to baseline algorithms.

## Performance
The algorithms were rigorously tested using the official UC Berkeley autograder, achieving optimal node expansion rates and passing all algorithmic efficiency tests (see `autograder_results.txt`).

## How to Run
To watch the A* agent solve the maze using the custom food search heuristic, run the following command in the terminal:

bash
python pacman.py -l bigSearch -p AStarFoodSearchAgent

## Project Architecture & Credits
This project was developed within an game engine given.

* **My Contribution (search.py & searchAgents.py):** I completely designed and implemented, with my team, the search algorithms (DFS, BFS, UCS, A*) and the custom heuristic evaluation functions for complex spatial problems.

* **Provided Framework:** The core game loop, board state management, ghost agents logic, and graphical interface (pacman.py, game.py, etc.) were provided as the base engine for the project by teachers.
