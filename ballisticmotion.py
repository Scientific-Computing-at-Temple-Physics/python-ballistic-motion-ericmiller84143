#Ballistic Motion in Python

import math as ma

g = input("What is the gravitational acceleration?: ")
v0 = input("What is the initital veloctiy?: ")
theta = input("What is the angle (in degrees) of the velocity above the ground?: ")
y = input("What is the initial height?: ")
t = input("What is the time step?: ")

theta = theta * ma.pi / 180  #convert to radians
x = 0.0 #inital x positon is 0
v_x = v0*ma.cos(theta)  #find velocity of x
v_y = v0*ma.sin(theta)  #find velocity of x
flight_time  = 0.0      #total time of flight
max_h = y               #track max height, starts at initial height


while (h>=0): #do calculations while the projectile is above the ground
    v_y = v_y - g*t   #find v_y after time step
    y = y + v_y*t     #find y position after time step based on new velocity
    if(y> max_h):
        max_h =y
    print "The ball is", y, "meters above the ground."
    x = x + v_x*t     #find x position after time step
    flight_time = flight_time + t   #update the time of flight
