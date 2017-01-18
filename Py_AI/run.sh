#!/bin/bash
xdg-open smallmaze.png #eog smallmaze.png
python Maze_Mapping.py > maze.data
cat maze.data
echo "___________Maze Loaded_____________"
python Path_search_V_1.py