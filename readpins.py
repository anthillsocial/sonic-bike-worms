#!/usr/bin/env python
import liblo, sys, time, math
import Adafruit_BBIO.ADC as ADC
ADC.setup()

# Send all OSC messages to port 1234 on the local machine
try:
    target = liblo.Address(12345)
except liblo.AddressError as err:
    print(err)
    sys.exit()

# Load a sound and start looping it
liblo.send(target, "/load", 0, "Scr1.wav")
liblo.send(target, "/loop", 0, 1)
liblo.send(target, "/play", 0)

# Now loop and send continuous messages
pitch = oldpitch = newpitch = 0.0
#top = 2.0
#bottom = 0.0
#step=0
startA = startB = time.time()
time.clock()
elapsedA = elapsedB = counter = lastcount = rps = oldrps = 0
maxsmooth = 10
smooth = range(maxsmooth+1)
n = 0
incspeed = 0.3
while True:        
    # pitch = (-1*math.sin(step)*(top-bottom))+(top-bottom) # Sine wave used for testing
    # step += 0.2                                           #   |---Used for testing
    elapsedA = time.time() - startA
    elapsedB = time.time() - startB
    # Read the analog input and count how many times
    # it reached the threshold every n seconds
    a = round(ADC.read("AIN0"),2) # returns a value between 0 and 1.0
    b = round(ADC.read("AIN1"),2) # returns a value between 0 and 1.0
    c = round(ADC.read("AIN2"),2) # returns a value between 0 and 1.0
    d = round(ADC.read("AIN3"),2) # returns a value between 0 and 1.0
    e = round(ADC.read("AIN4"),2) # returns a value between 0 and 1.0
    f = round(ADC.read("AIN5"),2) # returns a value between 0 and 1.0
    g = round(ADC.read("AIN6"),2) # returns a value between 0 and 1.0
    # Now determin revolutions per n seconds
    if elapsedA > 0.5:
       startA = time.time()
       print('a1:{} a2:{} a3:{} a4:{} a5:{} a6:{} '.format(a,b,c,d,e,f,g))
    #    startB = time.time()
    #     liblo.send(target, "/volume", 0, pitch)
    
