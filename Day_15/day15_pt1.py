def parse_input(input_file):
    sensors = dict()
    for line in open(input_file,"r").read().split("\n"):
        line = line.split()
        sensor_x = line[2].split("=")[1].split(",")[0]
        sensor_y = line[3].split("=")[1].split(":")[0]
        beacon_x = line[8].split("=")[1].split(",")[0]
        beacon_y = line[9].split("=")[1]
        sensors[(int(sensor_x),int(sensor_y))] = (int(beacon_x),int(beacon_y))
    return sensors

#dict.keys() gets keys
#dict.values() gets values
#dict.items() gets (key,value)

def distance(spot1,spot2):
    return abs(spot1[0]-spot2[0]) + abs(spot1[1]-spot2[1])

def get_min_pair(sensors):
    x = min(sensors.keys(),sensors.items(),key=lambda i: i[0])[0]
    y = min(sensors.keys(),sensors.items(),key=lambda i: i[1])[1]
    return (x,y)

def get_max_pair(sensors):
    x = max(sensors.keys(),sensors.items(),key=lambda i: i[0])[0]
    y = max(sensors.keys(),sensors.items(),key=lambda i: i[1])[1]
    return (x,y)

def get_radius(sensor,sensors_map):
    impossible_squares = set()
    # get distance to closest beacon
    beacon = sensors_map[sensor]
    dist = distance(sensor,beacon)
    x = sensor[0]
    y = sensor[1]
    for x_dist in range(0,dist+1):
        y_dist = dist - x_dist
        for y_chg in range(0,y_dist+1):
            impossible_squares.add((x+x_dist,y+y_chg))
            impossible_squares.add((x+x_dist,y-y_chg))
            impossible_squares.add((x-x_dist,y+y_chg))
            impossible_squares.add((x-x_dist,y-y_chg))
    return impossible_squares

def get_impossible_blocks_in(line,sensors_map):
    all_impossible_squares = set()
    for sensor in sensors_map.keys():
        all_impossible_squares.update(get_radius(sensor,sensors_map))
    impossible_counter = 0
    for square in all_impossible_squares:
        # gotta also make sure the square doesn't already contain a sensor
        if square[1] == line and square not in sensors_map.values():
            impossible_counter+=1
    return impossible_counter

print("Test:")
print(f"There are {get_impossible_blocks_in(10,parse_input('day15_test_input.txt'))} positions that cannot contain a beacon.")
print("Real:")
print(f"There are {get_impossible_blocks_in(2000000,parse_input('day15_input.txt'))} positions that cannot contain a beacon.")
