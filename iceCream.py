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

def draw_cone(tX1, tY1, tX2, tY2, tX3, tY3, tCol, tWin):
    draw_tri(tX1, tY1, tX2, tY2, tX3, tY3, tCol, tWin)

def draw_waffle(wX, wY, wSz, wCol, wWin):
    waffle = Polygon(Point(wX - wSz, wY), Point(wX, wY + wSz * 1.5),
                     Point(wX + wSz, wY), Point(wX, wY - wSz * 1.5))
    waffle.setOutline(wCol)
    waffle.draw(wWin)

icRad = 50
winFactor = 10
winX = icRad * winFactor
winY = icRad * winFactor

icWin = GraphWin("Have a cone!", winX, winY)
icWin.setCoords(0, 0, winX, winY)

draw_circ(winX / 2, winY / 2 + icRad, icRad, "pink", icWin)
draw_cone(winX / 2 - icRad - 2, winY / 2 + icRad * .75,
         winX / 2 + icRad + 2, winY / 2 + icRad * .75,
         winX / 2 , winY / 2 - icRad * 2,
         "orange", icWin)
draw_waffle((winX / 2 - icRad - 2) + icRad / 5,
            (winY / 2 + icRad * .75) - icRad / 5,
            5, "brown", icWin)
            
         
         
