import suncalc
from datetime import datetime
from math import atan,tan,pi

#Get position of mirror
def getHL(HG,TP,time):#Global position of heliostat(lat,lon), Position of Tower(azimuth due to the south,altitude), time(in the type of datetime)
    sun=suncalc.getPosition(time,HG[0],HG[1])
    return {"azimuth":(sun["azimuth"]+TP[0])/2,"altitude":atan(-1/tan((sun["altitude"]+TP[1])/2))}
#Get normal of mirror
def getHN(HG,TP,time):#Global position of heliostat(lat,lon), Position of Tower(azimuth due to the south,altitude), time(in the type of datetime)
    sun=suncalc.getPosition(time,HG[0],HG[1])
    return {"azimuth":(sun["azimuth"]+TP[0])/2,"altitude":(sun["altitude"]+TP[1])/2}