import dijkastra as d
maze = d.LoadMaze("maze.txt")
print maze
d.PrintSolution(maze,d.Dijkstra(maze,10,maze(6,23),maze(12,15)))