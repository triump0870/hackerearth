#!usr/bin/env Python
'''This program demonstrate the use of A* Algorithm'''
import heapq

def astar(graph,current,end):
	openset = set()
	openheap = []
	closeset = set()

	def retracepath(c):
		path = [c]
		while c.parent is not None:
			c = c.parent
			path.append(c)
		path.reverse()
		return path
	openset.add(current)
	openheap.append((0,current))
	while  openset:
		current = heapq.heappop(openheap)[1]
		if current == end:
			return retracepath(current)
		openset.remove(current)
		closeset.add(current)
		for tile in graph[current]:
			if tile not in closeset:
				tile.H = (abs(end.x- tile.x)+abs(end.y-tile.y))*10
				if tile not in openset:
					openset.add(tile)
					heapq.heappush(openheap,(tile.H,tile))
				tile.parent = current
	return []