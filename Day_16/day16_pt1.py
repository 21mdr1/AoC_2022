from parse import parse
###### Starting out with some pseudocode of things I need to write ######

## Data Structure needed ##
class Graph:
    def __init__(self,vertices,edges,vertex_weights):
        self.vertices = vertices #set
        self.edges = edges #list of sets
        self.vertex_weights = vertex_weights #dict
        self.non_zero_valves = [vertex for vertex in self.vertices if not self.vertex_weights[vertex] == 0]
        self.shortest_walks = self.get_shortest_walk() #form: {(node1,node2):[node1,...,node2]}

    def setup_for_dijkstras(self,start_node):
        # not 100% sure that we have to remove ourselves, but we'll see
        unvisited_nodes = self.vertices.copy() #set
        tentative_distances = dict() #dict
        for node in self.vertices:
            if node == start_node:
                tentative_distances[node] = 0
            else:
                tentative_distances[node] = float('inf')
        return unvisited_nodes,tentative_distances

    def get_unvisited_neighbors(self,vertex,unvisited_nodes):
        neighbors = set()
        for neighbor_node in unvisited_nodes:
            if {neighbor_node,vertex} in self.edges:
                neighbors.add(neighbor_node)
        return neighbors

    def smallest_distance_is_inf(self,unvisited_nodes,tentative_distances):
        for node in unvisited_nodes:
            if not tentative_distances[node] == float('inf'):
                return False
        return True

    def get_closest_node(self,unvisited_nodes,tentative_distances):
        #sorted(list(unvisited_squares),key=lambda x: tentative_distances[x])[0]
        return min(unvisited_nodes,key=lambda x: tentative_distances[x])

    def get_shortest_walk(self):
        # we shall do dijkstra's
        shortest_paths = dict() #form: {(node1,node2):[node1,...,node2]}
        for start_node in self.non_zero_valves + ['AA']:
            # Steps 1 & 2: Setup
            unvisited_nodes,tentative_distances = self.setup_for_dijkstras(start_node)
            current_node = start_node
            shortest_paths[(start_node,start_node)] = [start_node]

            while True:
                # Step 3: Look at neighbors
                neighbors = self.get_unvisited_neighbors(current_node,unvisited_nodes)
                for neighbor in neighbors:
                    if tentative_distances[current_node] + 1 < tentative_distances[neighbor]:
                        tentative_distances[neighbor] = tentative_distances[current_node] + 1
                        shortest_paths[(start_node,neighbor)] = shortest_paths[(start_node,current_node)] + [neighbor]
                # Step 4: mark as visited
                unvisited_nodes.remove(current_node)
                # Step 5: are we done?
                if self.smallest_distance_is_inf(unvisited_nodes,tentative_distances):
                    break

                # Step 6: continue
                current_node = self.get_closest_node(unvisited_nodes,tentative_distances)
        return shortest_paths

        def __str__(self):
            # tbh this is just for debugging
            return self.shortest_walks

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

def path_with_most_release(start_point, time, unvisited_valves, graph):
    if len(unvisited_valves) == 0:
        return time * graph.vertex_weights[start_point]
    most_release=0
    for valve in unvisited_valves:
        #calculate time
        new_time = time - len(graph.shortest_walks[(start_point,valve)])
        new_unvisited_valves = unvisited_valves.copy()
        new_unvisited_valves.remove(valve)
        release = path_with_most_release(valve,new_time,new_unvisited_valves,graph)
        if release > most_release: most_release = release
    return time * graph.vertex_weights[start_point] + most_release


## Print Things ##
print("Test run:")
test_graph = parse_input("day16_test_input.txt")
unvisited_valves = test_graph.non_zero_valves.copy()
pressure_released = path_with_most_release('AA', 30, unvisited_valves, test_graph)
print(f'The most pressure you can release is {pressure_released}')

print("Real run:")
graph = parse_input("day16_input.txt")
unvisited_valves = graph.non_zero_valves.copy()
if 'AA' in unvisited_valves: unvisited_valves.remove('AA')
pressure_released = path_with_most_release('AA', 30, unvisited_valves, graph)
print(f'The most pressure you can release is {pressure_released}')
