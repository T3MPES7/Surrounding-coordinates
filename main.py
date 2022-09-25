#Main function
def co():
    global Earths_Radius ,lat ,lon, Distance, n
    #In Meters
    Earths_Radius=6378137
    Coordinat=[]

    #Center of the square
    location=(input("Enter coordinates in (Lat, Lon) form: ").split(','))
    lat,lon=location

    #In meters length of the square in distanceXdistance form
    Distance=int(input("Enter distance: "))

    #Number of circles per line 
    Mini_radius=Distance//400
    MaxLC=Mini_radius-1
    #incase a smaller circle is needed 
    Estimate=Distance%400
    if Estimate < 200:
        Estimate=0
    if Estimate > 200:
        Mini_radius+=1

    #number of smaller circles per quarter of the square
    x1,y1=400,400
    #positions
    n=0

    #for changing signs +/-
    pnx=1
    pny=1


    Run=0
    grid=False
    def cord(x,y):
        import math

        #Coordinate offsets in radians
        dLat= x/Earths_Radius
        dLon= y/(Earths_Radius*math.cos(math.pi*float(lat)/180))

        #OffsetPosition, decimal degrees
        latO = float(lat) + dLat * 180/math.pi
        lonO = float(lon) + dLon * 180/math.pi

        return(latO,lonO)

    while grid==False:
        


        for i in range(Mini_radius):
            for j in range(Mini_radius):
                
                n+=1
                x=pnx*(200+(400*i))
                y=pny*(200+(400*j))
                Coordinat.append(cord(x,y))
        if Mini_radius> 1:
            Run+=1
        #changing signs 
        if Run ==1:
            pnx=-1
            pny=1
        if Run ==2:
            pnx=1
            pny=-1
        if Run ==3:
            pnx=-1
            pny=-1
        if Run==4:
            pny=1
            pnx=1
            for z in range(2):
                for q in range(Mini_radius):
                    
                    n+=1
                    x=0
                    y=pny*(200+(400*q))
                    Coordinat.append(cord(x,y))
                pny=-1
                
            for zz in range(2):
                for qq in range(Mini_radius):
                    
                    n+=1
                    x=pnx*(200+(400*qq))
                    y=0
                    Coordinat.append(cord(x,y))
                pnx=-1
            
            grid=True
    
    return(Coordinat)
#outputs all the surrounding coordinate
print(co())
#outputs the number of coordinates that fit within the square 
print(n)
