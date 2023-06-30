from MQ136 import *
import sys, time

try:
    print("Press CTRL+C to abort.")
    
    mq = MQ();
    while True:
        perc = mq.MQPercentage()
        print("\r")
        print("\033[K")
        print("NH4: %g ppm, CO: %g ppm, H2S: %g ppm" % (perc["NH4"], perc["CO"], perc["H2S"]))
        
        time.sleep(0.1)

except Exception as e:
    print(e)

