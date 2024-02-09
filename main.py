######################################################################################################
## Author: Aleksi Nurmento                                                                          ##
##                                                                                                  ##
## Main function reads the input graph from a txt file and runs the _modified_ Dijkstra's algorithm ##
## Modified Dijkstra's: finds a path from start node to destination where the maximum single weight ##
## is minimized.                                                                                    ##
##                                                                                                  ##
######################################################################################################

from weightedgraph import *
import time

def main():

    # Reading the text file and forming the graph
    file = input("Type file in form: file.txt: ")
    start_time = time.time()    #timer
    graph = open(file)
    line1 = graph.readline().split()
    n_egdes = int(line1[1])
    n_nodes = int(line1[0])
    graph = graph.readlines()
    destination = int(graph[len(graph) - 1].rstrip())
    del graph[len(graph) - 1]

    g = WeightedGraph(n_nodes)

    for line in graph:
        fro, to, weight = map(int, line.split())
        add_edge(g,fro,to,weight)
    # Running the algorithm and printing the results
    dijkstra(g,1)													
    print('Path from 1 to {} with current highest weight'.format(destination))	
    print_path(g,destination)												
    print("--- %s seconds ---" % (time.time() - start_time))

main()