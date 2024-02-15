# AStar-py

A pure python package for astar search.

Currently still in development.

## Installation

Through `pip`:
```sh 
pip install astar_py
```

Through poetry:
```sh
poetry add astar_py
```
## Features

- (WIP) Traditional A* algorithm utilizing heuristic search
- (WIP) Batched A* algorithm for efficient batch calculations of operations
- (WIP) Pruned frontier search
- (WIP) Blind search, where no target goal state is set.
- (WIP) Search after goal is found. This may be used to find a variety of paths to the goal state within a search budget.

## Usage

To usage the A* search, you need to define the necessary functions.

### `heuristic_fn`

The heuristic function is the base of A* search. It "guides" the search by reordering the priorities of node search through 

