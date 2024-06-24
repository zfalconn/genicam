import zmq
import time
import random

def publisher():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5555")

    while True:
        # Simulate data generation (e.g., a pair of coordinates)
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        data = f"{x},{y}"
        
        # Send the data with a topic
        socket.send_string(f"coordinates {data}")
        
        # Sleep for a while before sending the next data
        time.sleep(0.1)

if __name__ == "__main__":
    publisher()