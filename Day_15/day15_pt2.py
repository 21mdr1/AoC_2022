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


def get_min_pair(beacons_and_sensors):
    sensors = list(beacons_and_sensors.keys())
    beacons = list(beacons_and_sensors.values())
    x = min(sensors+beacons,key=lambda i: i[0])[0]
    y = min(sensors+beacons,key=lambda i: i[1])[1]
    return (x,y)

def get_max_pair(beacons_and_sensors):
    sensors = list(beacons_and_sensors.keys())
    beacons = list(beacons_and_sensors.values())
    x = max(sensors+beacons,key=lambda i: i[0])[0]
    y = max(sensors+beacons,key=lambda i: i[1])[1]
    return (x,y)

def get_tuning_frequency(beacons_and_sensors,distances,x,y):
    #print(beacons_and_sensors) # debug
    
    sensors = beacons_and_sensors.keys()
    beacons = beacons_and_sensors.values()
    
    for y in range(0,y+1):
        print("Y",y) # debug
        #if y%1000==0: print("Y",y) # debug
        for x in range(0, x+1):
            #print(x,y) # debug
            if x%1000000==0: print("  X",x) # debug
            if (x,y) in beacons: continue
            #print(" Not a beacon") # debug
            possible = True
            for sensor in sensors:
                #print(" sensor",sensor) # debug
                if distance((x,y),sensor) <= distances[sensor]:
                    possible = False
                    break
            if possible: return x*4000000 + y


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
