import zmq
import json
import time

def subscriber():
    
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5555")
    
    # Subscribe to the "coordinates" topic
    socket.setsockopt_string(zmq.SUBSCRIBE, "")
    
    # while True:
        # Receive a message
        
    message = socket.recv_string()
    message_list = json.loads(message)
    #print(f"Received 1D-array: {message_list}") #with print: 6ms, without print: 2ms

if __name__ == "__main__":
    starttime = time.time()
    
    subscriber()

    endtime = time.time() - starttime
    print(f"Command takes: {endtime} seconds")