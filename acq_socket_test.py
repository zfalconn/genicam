from harvesters.core import Harvester
from harvesters.util.pfnc import mono_location_formats, \
    rgb_formats, bgr_formats, \
    rgba_formats, bgra_formats
import numpy as np
import matplotlib.pyplot as plt
import cv2

import zmq
import time

import json


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")
  

h = Harvester()

h.add_file('C:/Program Files/Daheng Imaging/GalaxySDK/GenTL/Win64/GxGVTL.cti')
print(h.files)
h.update()
print(h.device_info_list)


custom_device_xml = "C:/Users/Linh/Desktop/Fraunhofer/genicam/MER2-160-75GC(169.254.48.129[00-21-49-05-EE-A2]).XML" #not necessary if device preconfig with GalaxyViewer
ia = h.create()

ia.start()


try:
    for i in range(100):
        # Fetch an image
        with ia.fetch_buffer() as buffer:
            # Access the image data
            print(buffer)
            component = buffer.payload.components[0]
            width = component.width
            height = component.height
            data = component.data

            

            #send data via json string
            # json_array = data.tolist()
            # socket.send_string(json.dumps(json_array))

        
            
            # Convert the raw data to a numpy array and reshape it
            image = np.frombuffer(data, dtype=np.uint8).reshape(height, width)

            rgb_image = cv2.cvtColor(image, cv2.COLOR_BAYER_RG2RGB)

            # Display the image using OpenCV
            cv2.imshow('RGB Image', rgb_image)
            #time.sleep(2)
            # Break the loop on key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                #cv2.imwrite('captured_image.jpg', rgb_image)
                break
finally:
    # Stop acquisition
    
    ia.stop_acquisition()

    # Destroy the image acquirer
    ia.destroy()

    # Clear the Harvester
    h.reset()
    
    # Close OpenCV windows
    cv2.destroyAllWindows()
