# Bike Worms
A series of scripts experimenting with analog input and OSC output on the beaglebone black.

## Install

First we need to install adafruit's beaglebone-io-python libarary

    git clone THIS REPOSITORY
    ntpdate -b -s -u pool.ntp.org
    git clone git://github.com/adafruit/adafruit-beaglebone-io-python.git
    cd adafruit-beaglebone-io-python/
    sudo python ./setup.py install 

Then run the script

    sudo ./pitch.py

# Setup
Tachometer wiring

Pin34<-->10kesitor<-->switch<-->Pin32
                    |            
                    --->Pin40     



