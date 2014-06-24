import sys
import heapq

infinity = sys.maxint-10000

class Maze(list):
    def __init__(self, mazelist):
        list.__init__(self, mazelist)
    def __repr__(self):
        return '\n'.join([''.join([cell.Type for cell in row]) for row in self])
    def __call__(self, r, c):
        return self[r][c]

class Cell:
    def __init__(self, row, col, type):
        self.Row = row
        self.Col = col
        self.Type = type
        self.D = infinity
        self.IsClosed = False
        self.IsInQ = False
    def Children(self, maze):
        for cell in [cell for cell in
                     [maze(self.Row, self.Col-1), maze(self.Row-1, self.Col),
                      maze(self.Row, self.Col+1), maze(self.Row+1, self.Col)] if (cell.Type == 'P') and not cell.IsClosed]:
            yield cell
    def __repr__(self):
        return "Cell at (%i, %i) of Type \'%s\'" % (self.Row, self.Col, self.Type)
    def __cmp__(self, other):
        return cmp(self.D, other.D)
    
def LoadMaze():
    t = input()
    matrix = []
    for i in range(t):
        matrix.append(list(raw_input()))
    return Maze(matrix)


def Dijkstra(maze, cost, scell, ecell):
    scell.D = 0
    scell.Previous = None
    Q = [scell]+[cell for cell in scell.Children(maze)]
    heapq.heapify(Q)
    while len(Q)>0:
        currcell = heapq.heappop(Q)
        if currcell is ecell:
            return ecell
        currcell.IsClosed = True
        for cell in currcell.Children(maze):
            if cell.D > currcell.D + cost:
                cell.D = currcell.D + cost
                cell.Previous = currcell
            if not cell.IsInQ:
                heapq.heappush(Q, cell)
                cell.IsInQ = True
        
def PrintSolution(maze, ecell):
    solmaze = [[cell.Type for cell in row] for row in maze]
    solmaze[ecell.Row][ecell.Col] = 'E'
    pcell = ecell
    while pcell.Previous:
        pcell = pcell.Previous
        solmaze[pcell.Row][pcell.Col] = '-'
    solmaze[pcell.Row][pcell.Col] = 'S'
    print '\n'.join([''.join([type for type in row]) for row in solmaze])

def main():
    maze = LoadMaze()
    print "The given maze is:"
    print maze

    print "\n============================================\n"
    print "Solving the maze:"
    PrintSolution(maze,Dijkstra(maze,5,maze(1,1),maze(4,3)))

if __name__ == "__main__":
    main()