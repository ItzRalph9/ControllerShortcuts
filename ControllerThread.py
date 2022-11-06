from threading import Thread
import ControllerInput as CI

# Create a seperate thread to detect controller input.
# This is needed for the input loop and the window loop
# to run concurrently
def createThread():
    t1 = Thread(target = CI.Run)
    t1.daemon = True
    t1.start()