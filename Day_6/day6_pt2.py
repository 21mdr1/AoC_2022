datastream_buffer = open("day6_input.txt","r").read()

#start of message = fourteen characters that are all different

# first position where the four most recently received characters were all different. 
# the number of characters from the beginning of the buffer to the end of the first such four-character marker.

for i in range(len(datastream_buffer)):
    if ((datastream_buffer[i] not in datastream_buffer[i+1:i+14]) and
        (datastream_buffer[i+1] not in datastream_buffer[i+2:i+14]) and
        (datastream_buffer[i+2] not in datastream_buffer[i+3:i+14]) and
        (datastream_buffer[i+3] not in datastream_buffer[i+4:i+14]) and
        (datastream_buffer[i+4] not in datastream_buffer[i+5:i+14]) and
        (datastream_buffer[i+5] not in datastream_buffer[i+6:i+14]) and
        (datastream_buffer[i+6] not in datastream_buffer[i+7:i+14]) and
        (datastream_buffer[i+7] not in datastream_buffer[i+8:i+14]) and
        (datastream_buffer[i+8] not in datastream_buffer[i+9:i+14]) and
        (datastream_buffer[i+9] not in datastream_buffer[i+10:i+14]) and
        (datastream_buffer[i+10] not in datastream_buffer[i+11:i+14]) and
        (datastream_buffer[i+11] not in datastream_buffer[i+12:i+14]) and
        (datastream_buffer[i+12] not in datastream_buffer[i+13])):
            print("Your marker is at: {}".format(i+14))
            break
