import urllib2
import exchange_rates
from math import log, exp

def find_negative_cycle(graph, distance, predecessor, src, curr_list):
	tot = 1.0
	v = src
	u = predecessor[src]
	visited = set([src])
	print 
	while u not in visited:
		print curr_list[v],"-->", curr_list[u], exp(-graph[u][v])
		tot*= exp(-graph[u][v])
		visited.add(u)
		v = u
		u = predecessor[u]
	tot *= exp(-graph[src][v])
	print curr_list[v],"-->", curr_list[src], exp(-graph[u][v])
	print "Total:", tot

	if tot < 1.0:
		print "No Arbitrage opportunities"

def bellman_ford(graph, edge_list, src, V):
	distance = [float("inf") for x in range(0, V)]
	predecessor = [-1 for x in range(0, V)]

	distance[src] = 0

	for x in xrange(0,V-1):
		for edge in edge_list:
			u = edge[0]
			v = edge[1]
			weight = edge[2]
			if distance[u] + weight < distance[v]:
				distance[v] = distance[u] + weight
				predecessor[v] = u
	for edge in edge_list:
			u = edge[0]
			v = edge[1]
			weight = edge[2]
			if distance[u] + weight < distance[v]:
				# print "negative weight cycle present!"
				distance[v] = distance[u] + weight
				predecessor[v] = u
		
	return distance, predecessor


def create_graph(no_of_vertices):
	with open('graph_edges.txt', 'r') as edges:
		graph = [[0 for x in range(0, no_of_vertices)] for y in range(0, no_of_vertices)]
		for x in range(0, no_of_vertices):
			graph[x][x] = 1
		edge_list = []
		for line in edges:
			x = line.split(' ')
			u = int(x[0])
			v = int(x[1])
			edge_list.append([u, v, -log(float(x[2].strip('\n')))])
			graph[u][v] = -log(float(x[2].strip('\n')))
	return graph, edge_list

def main():
    curr_list = exchange_rates.get_rate()
    print curr_list
    no_of_vertices = len(curr_list)
    graph, edge_list = create_graph(no_of_vertices)
    
    for x in curr_list:
		src = curr_list.index(x)
		dist, pred = bellman_ford(graph, edge_list, src, no_of_vertices)
		find_negative_cycle(graph, dist, pred, src, curr_list)

if __name__ == '__main__':
    main()