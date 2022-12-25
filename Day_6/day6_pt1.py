datastream_buffer = open("day6_input.txt","r").read()

#start of packet = four characters that are all different

# first position where the four most recently received characters were all different. 
# the number of characters from the beginning of the buffer to the end of the first such four-character marker.

for i in range(len(datastream_buffer)):
    if (datastream_buffer[i] not in datastream_buffer[i+1:i+4]) and (datastream_buffer[i+1] not in datastream_buffer[i+2:i+4]) and (datastream_buffer[i+2] not in datastream_buffer[i+3]):
        print("Your marker is at: {}".format(i+4))
        break
