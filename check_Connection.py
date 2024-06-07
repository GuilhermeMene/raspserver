#Script to check the internet connection 

import socket 
from datetime import datetime 
import time 

hostname = "1.1.1.1"
port = 53

def logger(message):
    print(message)
    with open('connection.log', "a") as file:
        file.write(message + "\n")
    file.close()

def isConnected(hostname, port):
    #Check the connection 
    try:
        soc = socket.create_connection((hostname, port))    

        #Close connection if is OK
        if soc is not None:
            logger(f"** Closing sucessful connection...! - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            soc.close()
    except Exception as e:
        logger(f"## An error ocurred: {e} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def run():
    logger("\n\n\n") #Creating a space in the log to identify easy interruption of the code running  
    logger(f"-- Starting script... - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    while True:
        isConnected(hostname, port)

        #Wait 10 seconds to check again 
        time.sleep(10)

#Run the script 
run()
