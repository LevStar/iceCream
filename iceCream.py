# iceCream by LevStar and LevStar

from graphics import *

def draw_circ(cX, cY, cRad, cCol, cWin):
    circ = Circle(Point(cX, cY), cRad)
    circ.setFill(cCol)
    circ.setOutline(cCol)
    circ.draw(cWin)

def draw_tri(tX1, tY1, tX2, tY2, tX3, tY3, tCol, tWin):
    tri = Polygon(Point(tX1, tY1), Point(tX2, tY2), Point(tX3, tY3))
    tri.setFill(tCol)
    tri.setOutline(tCol)
    tri.draw(tWin)

icRad = 50
winFactor = 10
winX = icRad * winFactor
winY = icRad * winFactor

icWin = GraphWin("Have a cone!", winX, winY)
icWin.setCoords(0, 0, winX, winY)

draw_circ(winX / 2, winY / 2 + icRad, icRad, "pink", icWin)
draw_tri(winX / 2 - icRad - 2, winY / 2 + icRad * .75,
         winX / 2 + icRad + 2, winY / 2 + icRad * .75,
         winX / 2 , winY / 2 - icRad * 2,
         "orange", icWin)
         
         
