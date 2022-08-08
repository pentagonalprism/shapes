import pandas as pd
import numpy as np
import math

class pentagonalPrisim:
    def __init__(self,a,h):
        #Base Edge
        self.a = a
        #Height
        self.h = h

    def pentagonalPrisimVolume(self):
        v = round(.25 * math.sqrt(5*(5+2*math.sqrt(5)))*(self.a**2)*self.h,2)
        return round(v,2)
    
    def pentagonalPrisimHeight(self):
        h = self.pentagonalPrisimVolume()*(math.sqrt((16/5)-math.sqrt(1024/125))/self.a**2)
        return round(h,2)
    
    def pentagonalPrisimSurfaceArea(self):
        A = (5*self.a*self.h)+(1/2)*math.sqrt(5*(5+2*math.sqrt(5)))*(self.a**2)
        return round(A,2)
    
    def pentagonalBaseArea(self):
        AB = (1/4)*math.sqrt(5*(5+2*math.sqrt(5)))*(self.a**2)
        return round(AB,2)
    
    def pentagonalLateralSurfaceArea(self):
        AL = 5*self.a*self.h
        return round(AL,2)    
    
    def __iter__(self):
        pass

p1 = pentagonalPrisim(3,10)

print('Pentagonal Prisim Volume : ',p1.pentagonalPrisimVolume())
print('Pentagonal Prisim Height : ', p1.pentagonalPrisimHeight())
print('Pentagonal Prisim Surface Area : ',p1.pentagonalPrisimSurfaceArea())
print('Pentagonal Base Area : ',p1.pentagonalBaseArea())
print('Pentagonal Surface Area : ',p1.pentagonalLateralSurfaceArea())