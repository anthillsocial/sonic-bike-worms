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
    value = ADC.read("AIN1") # returns a value between 0 and 1.0
    if value > 0.7:
        counter += 1
    # Now determin revolutions per n seconds
    if elapsedA > 0.5:
        #if counter != 0:
        #print("{4} newptch {0} pitch {1} revolutions per {2} seconds {3} lastcount".format(pitch, counter, interval, lastcount, newpitch))
        #smooth[n] = counter*0.1
        #pitch = sum(smooth)/(len(smooth)
        #if counter != 0:
        oldrps = rps
        rps = counter*0.5
        counter = elapsedA = 0
        startA = time.time()
    # The fastest we can send OSC messages is every 0.1 seconds
    if elapsedB > 0.2:
        #print("pitch {0}".format(pitch))
        smooth[n] = rps
        avrps = sum(smooth)/(len(smooth))
        n = n+1
        if n > maxsmooth: n = 0    
        if rps > oldrps:
            pitch = pitch+incspeed
        elif rps < oldrps:
            pitch = pitch-incspeed
        if pitch>2.0: pitch = 2.0
        if pitch<0.3: pitch = 0.3
        print("pitch:{0} rps:{1} oldrps:{2} avrps:{3} value:{4}".format(pitch, rps, oldrps, avrps, value))
        elapsedB = 0
        startB = time.time()
        liblo.send(target, "/volume", 0, pitch)
    
