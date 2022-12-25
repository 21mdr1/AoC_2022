from parse import parse

def distance(spot1,spot2):
    return abs(spot1[0]-spot2[0]) + abs(spot1[1]-spot2[1])

def parse_input(input_file):
    beacons_and_sensors = dict(); distances = dict()
    for line in open(input_file,"r").read().split("\n"):
        sensor_x,sensor_y,beacon_x,beacon_y = parse("Sensor at x={}, y={}: closest beacon is at x={}, y={}",line)
        sensor = (int(sensor_x),int(sensor_y))
        beacon = (int(beacon_x),int(beacon_y))
        beacons_and_sensors[sensor] = beacon
        distances[sensor] = distance(sensor,beacon)
    return beacons_and_sensors,distances


#dict.keys() gets keys
#dict.values() gets values
#dict.items() gets (key,value)


def get_impossible_blocks(distances,limit_x,limit_y):
    print("Getting blocks") # debug
    impossible_blocks = set(distances.keys())
    for sensor in distances.keys():
        print(" sensor",sensor)
        dist = distances[sensor]
        print(" distance",dist)
        for x_diff in range(0,dist+1):
            print("  x distance",x_diff)
            for y_diff in range(0,dist-x_diff+1):
                x = sensor[0] + x_diff; y = sensor[1] + y_diff
                if x >= 0 and x <= limit_x and y >= 0 and y <= limit_y:
                    impossible_blocks.add((x,y))
                
                x = sensor[0] - x_diff; y = sensor[1] + y_diff
                if x >= 0 and x <= limit_x and y >= 0 and y <= limit_y:
                    impossible_blocks.add((x,y))
                
                x = sensor[0] + x_diff; y = sensor[1] - y_diff
                if x >= 0 and x <= limit_x and y >= 0 and y <= limit_y:
                    impossible_blocks.add((x,y))
                
                x = sensor[0] - x_diff; y = sensor[1] - y_diff
                if x >= 0 and x <= limit_x and y >= 0 and y <= limit_y:
                    impossible_blocks.add((x,y))
    return impossible_blocks

def get_tuning_frequency(beacons_and_sensors,distances,x,y):
    impossible_blocks = get_impossible_blocks(distances,x,y)
    print("Getting tuning freq") # debug
    
    for x_spot in range(0,x+1):
        print("X",x_spot) # debug
        for y_spot in range(0,y+1):
            if y%1000000 == 0: print("  Y",y_spot) # debug
            if (x_spot,y_spot) not in impossible_blocks:
                return x*4000000 + y


def visualize(beacons_and_sensors,distances):
    sensors = beacons_and_sensors.keys()
    beacons = beacons_and_sensors.values()
    
    
    max_distance = max(distances.values())
    min_x,min_y = tuple(map(lambda i: i - max_distance,get_min_pair(beacons_and_sensors)))
    max_x,max_y = tuple(map(lambda i: i + max_distance,get_max_pair(beacons_and_sensors)))
    
    for y in range(min_y, max_y+1):
        spaces = 10 - len(str(y))
        row = str(y) + ' '*spaces
        for x in range(min_x, max_x+1):
            if (x,y) in sensors:
                row += 'S'
            elif (x,y) in beacons:
                row += 'B'
            else:
                blocked = False
                for sensor in sensors:
                    if distance((x,y),sensor) <= distances[sensor]:
                        blocked = True; break
                if blocked:
                    row += '#'
                else: row += '.'
        print(row)


#beacons_and_sensors,distances = parse_input("day15_test_input.txt")
#visualize(beacons_and_sensors,distances)
#print("Test:")
#print(f"The tuning frequency {get_tuning_frequency(beacons_and_sensors,distances,14,11)}")

beacons_and_sensors,distances = parse_input("day15_input.txt")
#visualize(beacons_and_sensors,distances)
print("Real:")
print(f"The tuning frequency {get_tuning_frequency(beacons_and_sensors,distances,4000000,4000000)}")
