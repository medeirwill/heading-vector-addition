import math 

class HeadingVector: 
    
    epsilon = 0.001
    
    def __init__(self, magnitude, heading):
        self.heading = heading
        self.magnitude = magnitude

    def getNorthSouth(self):
        return self.magnitude * math.cos(math.radians(self.heading))
    
    def getEastWest(self):
        return self.magnitude * math.sin(math.radians(self.heading))
        
    def isZeroVector(): 
        return True if magnitude < epsilon else False 
        
    def __add__(self, other : HeadingVector): 
        
        if (self.isZeroVector()): 
            return other; 
        if (other.isZeroVector()): 
            return self; 
        
        resultantNorthSouth = self.getNorthSouth() + other.getNorthSouth()
        resultantEastWest = self.getEastWest() + other.getEastWest()
        
        if(abs(resultantEastWest) < epsilon and abs(resultantNorthSouth) < epsilon):
            return HeadingVector(0.0, 0.0)
        if(abs(resultantEastWest) < epsilon): 
            return HeadingVector(resultantNorthSouth, 0.0) if resultantNorthSouth > 0 else HeadingVector(resultantNorthSouth, 180.0)
        if(abs(resultantNorthSouth) < epsilon): 
            return HeadingVector(resultantEastWest, 90.0) if resultantEastWest > 0 else HeadingVector(resultantEastWest, 270.0)
        
        resultantMagntitude = sqrt(resultantEastWest**2 + resultantNorthSouth **2)
        resultantHeading = atan2(resultantNorthSouth, resultantEastWest)
        
        if (resultantHeading < 0): 
            resultantHeading = resultantHeading + 360
        return HeadingVector(resultantMagntitude, resultantHeading)
        

        
    
            
        