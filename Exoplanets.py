import numpy as np
from astropy.time import Time
from astropy.time import TimeDelta
import math
data = np.loadtxt('book1.csv', delimiter=",")

now = Time.now()
now.format = 'jd'
months_later = now + 20

dt = TimeDelta(18000, format='sec')
num_transits = 0
times = []


test= Time(2459620.0402760000, format='jd', scale='utc')
#print(test.iso)

#data[13,3]=2459510.217
for i in range(0,15):

    #-----------------------------Checking Date-----------------------------------
    first_transit = Time(data[i, 3], format='jd', scale='utc')
    next_transit = first_transit
    list=[]
    period = data[i,2]
    star_radius = data[i,10] #* 6.957e+8
    semi_major = data[i,9] #* 1.496e+11
    while next_transit < months_later:
        next_transit = next_transit + data[i,2]

        if next_transit > now:# and float(next_transit.jd)%1 >0.458 and float(next_transit.jd)%1<0.8:
            print("Object " + str(i+1) +" transits at " + str(next_transit.iso)+" UTC")


            radius= data[i,1]

            print("next transit " + str(next_transit.iso))


            #v= 2* math.pi * semi_major * 1.496e+11  / period
            Dur = (star_radius * 6.957e+8+ + 2 *  radius* 6.685e+7) * period / (2 * math.pi * semi_major * 1.496e+11)
            ingress = float(next_transit.jd) - Dur
            egress = float(next_transit.jd) + Dur
            ingress_time = Time(ingress, format='jd', scale='utc')
            egress_time = Time(egress, format='jd', scale='utc')
            print("ingress " + str(ingress_time.iso))
            print("egress " + str(egress_time.iso))
            #print(Dur * 2)

