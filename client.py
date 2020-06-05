import socket
import json
import random as r
import math as m
import time

def split(input_list):
    input_list_len = len(input_list)
    midpoint = input_list_len // 2
    return input_list[:midpoint], input_list[midpoint:]

def merge_sorted_lists(list_left, list_right):
    # Special case: one or both of lists are empty
    if len(list_left) == 0:
        return list_right
    elif len(list_right) == 0:
        return list_left
    
    # General case
    index_left = index_right = 0
    list_merged = []  # list to build and return
    list_len_target = len(list_left) + len(list_right)
    while len(list_merged) < list_len_target:
        if list_left[index_left] <= list_right[index_right]:
            # Value on the left list is smaller (or equal so it should be selected)
            list_merged.append(list_left[index_left])
            index_left += 1
        else:
            # Right value bigger
            list_merged.append(list_right[index_right])
            index_right += 1
            
        # If we are at the end of one of the lists we can take a shortcut
        if index_right == len(list_right):
            # Reached the end of right
            # Append the remainder of left and break
            list_merged += list_left[index_left:]
            break
        elif index_left == len(list_left):
            # Reached the end of left
            # Append the remainder of right and break
            list_merged += list_right[index_right:]
            break
        
    return list_merged

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        left, right = split(input_list)
        # The following line is the most important piece in this whole thing
        return merge_sorted_lists(merge_sort(left), merge_sort(right))

def monteCarlo(data):
    # Number of darts that land inside.
    inside = 0
    # Total number of darts to throw.
    total = data

    # Iterate for the number of darts.
    for i in range(0, total):
        # Generate random x, y in [0, 1].
        x2 = r.random()**2
        y2 = r.random()**2
        # Increment if inside unit circle.
        if x2 + y2 < 1.0:
            inside += 1

    return inside


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("connecting to Server...")
    s.connect(('3.88.49.118', 1234))
    print('Connected to Server')
    print("Begining handshake")
    port = s.recv(1024)
    s.close()
    print("Handshake complete")
    print("Connecting to Server on " + str(port))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(3)
    s.connect(('3.88.49.118', int(port)))
    print("Connection established")
    End = '}'.encode('utf-8')
    while True:
        print('waiting for data')
        total_data = ''
        while True:
            data = s.recv(8192)
            if End in data:
                total_data += str(data)
                break
            total_data += str(data)
        
        total_data = total_data.replace("b'", "")
        packet = total_data.replace("'", "")

        task = json.loads(packet)

        print('starting tasks')
        start_time = time.time()
        if task['job'] == 'Merge Sort':
            n = len(task['data'])
            result = merge_sort(task['data'])

        else:
            result = monteCarlo(int(task['data']))
        
        print(time.time() - start_time)
        print('finished task')
        resultPacketJSON = {
            'id': task['id'],
            'job': task['job'],
            'result': result
        }

        print('sending result')
        resultPacket = json.dumps(resultPacketJSON)
        s.sendall(resultPacket.encode('utf-8'))

