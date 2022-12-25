from parse import parse
###### Starting out with some pseudocode of things I need to write ######

## Data Structure needed ##
class Graph:
    def __init__(self,vertices,edges,vertex_weights):
        self.vertices = vertices
        self.edges = edges 
        self.vertex_weights = vertex_weights #dict of weights
        self.non_zero_valves = [vertex for vertex in self.vertices if not self.vertex_weights[vertex] == 0]
    
    #def get_shortest_walk(self):
    #    return list_of_shortest_walks

    
## Parse Input into a graph ##

def parse_input(input_file):
    valves = set() #vertices
    tunnels = [] #list of sets
    flow_rates = dict() #vertex weights
    
    for line in open(input_file,"r").read().split("\n"):
        values = parse("Valve {valve} has flow rate={flow_rate:d}; tunnels lead to valves {list_of_valves}",line)
        if values == None: # if there's only 1 tunnel:
            values = parse("Valve {valve} has flow rate={flow_rate:d}; tunnel leads to valve {list_of_valves}",line)
        
        # save values:
        valves.add(values['valve'])
        flow_rates[values['valve']] = values['flow_rate']
        for dest_valve in values['list_of_valves'].split(", "):
            tunnel = {values['valve'],dest_valve}
            if tunnel not in tunnels:
                tunnels.append(tunnel)
    return Graph(valves,tunnels,flow_rates)

## Do the Thing ##

#def path_with_most_release(start_point, time, unvisited_vertices, graph):
#    return pressure_released
parse_input("day16_test_input.txt")
