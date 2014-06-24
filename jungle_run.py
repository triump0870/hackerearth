from collections import namedtuple
from sys import stdin
import astar

name = namedtuple("name",["char","dy","dx"])

class Maze:
	start = "S"
	end = "E"
	wall = "T"
	path = "P"
	OPEN = {path,end}
	right = name(">",0,1)
	down = name("v",1,0)
	left = name("<",0,-1)
	up = name("^",-1,0)
	names = [right,down,left,up]

	@classmethod
	def load_maze(cls):
		t = input()
		maze = []
		for i in range(t):
			maze.append(list(raw_input()))
		return cls(maze)

	def __init__(self,maze):
		self.maze = maze


	def __str__(self):
		return "\n".join(''.join(line) for line in self.maze)

	def find_start(self):
		for y,line in enumerate(self.maze):
			try:
				x = line.index("S")
				return y,x
			except ValueError:
				pass

		raise ValueError("Start location not found")

	def find_end(self):
		for y,line in enumerate(self.maze):
			try:
				x = line.index("E")
				return y,x
			except ValueError:
				pass
		raise ValueError("End location not found")

	def solve(self,y,x,ey,ex):
		if self.maze[y][x]==Maze.end:
			return True
		else:
			for name in Maze.names:
				ny,nx = y+name.dy,x+name.dx
				if self.maze[ny][nx] in Maze.OPEN:
					print Maze.right.char
					if self.maze[y][x] != Maze.start:
						self.maze[y][x] = name.char
						if ey>ex and self.maze[ny+1][nx] in Maze.OPEN:
							ny += 1

					if self.solve(ny,nx,ey,ex):
						print "in if ny,nx",ny,nx
						return True

			if self.maze[y][x] != Maze.start:
				self.maze[y][x] = Maze.path
			return False

def main():
	maze = Maze.load_maze()
	print ("Maze Loaded:")
	print (maze)
	try:
		sy,sx = maze.find_start()
		ey,ex = maze.find_end()
		
		print("solving...")
		if astar.astar(maze,0,3):
			print(maze)
		else:
			print ("  no solution found")
	except ValueError:
		print ("No start point found.")

if __name__ == "__main__":
	main()