import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
#Empty lists for coordinates of points
listx = []
listy = []
listz = []

#Finding max and min coordinates
for i in point:
    listx.append(i.X)
    listy.append(i.Y)
    listz.append(i.Z)
maxx = max(listx)
minx = min(listx)
maxy = max(listy)
miny = min(listy)
maxz = max(listz)
minz = min(listz)

#Vertical 3D Bounding box 
point1 = rg.Point3d(maxx,maxy,maxz)
point2 = rg.Point3d(minx,miny,minz)
a = rg.Box(rs.WorldXYPlane(), rg.Interval(maxx,minx), rg.Interval(maxy,miny), rg.Interval(maxz,minz))