# graph_search_py

A pure python package for graph search algorithms.

Currently still in development.

## Installation

Through `pip`:
```sh 
pip install graph_search_py
```

Through poetry:
```sh
poetry add graph_search_py
```
## Features

- (WIP) Unified interface for discrete graph search algorithms

- (WIP) A* algorithm for graph search
- (WIP) Traditional A* algorithm utilizing heuristic search
- (WIP) Batched A* algorithm for efficient batch calculations of operations
- (WIP) Pruned frontier search
- (WIP) Blind search, where no target goal state is set.
- (WIP) Search after goal is found. This may be used to find a variety of paths to the goal state within a search budget.

- (WIP) Greedy Best First Search (GBFS)
- (WIP) Dijkstra's algorithm

## Usage

To usage the A* search, you need to define the necessary functions.

### `heuristic_fn`

The heuristic function is the base of A* search. It "guides" the search by reordering the priorities of node search through 

