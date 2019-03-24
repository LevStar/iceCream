# iceCream by LevStar and LevStar

from graphics import *

def draw_circ(cX, cY, cRad, cCol, cWin):
    circ = Circle(Point(cX, cY), cRad)
    circ.setFill(cCol)
    circ.setOutline(cCol)
    circ.draw(cWin)

def draw_tri(twX, twY, tSz, tCol, tWin):
    tri = Polygon(Point(twX / 2 - tSz - 2, twY / 2 + tSz * .75),
                  Point(twX / 2 + tSz - 2, twY / 2 + tSz * .75),
                  Point(twX / 2,  twY / 2 - tSz * 2))
    tri.setFill(tCol)
    tri.setOutline(tCol)
    tri.draw(tWin)

def draw_cone(twX, twY, tSz, tCol, tWin):
    draw_tri(twX, twY, tSz, tCol, tWin)

def draw_waffle(wX, wY, wSz, wCol, wWin):
    waffle = Polygon(Point(wX - wSz * .75, wY), Point(wX, wY + wSz * 1.5),
                     Point(wX + wSz * .75, wY), Point(wX, wY - wSz * 1.5))
    waffle.setOutline(wCol)
    waffle.draw(wWin)

def draw_waffles(wX, wY, wSz, wCol, wWin):
    for j in range(6):
        for i in range(9 - j * 2):
            draw_waffle(wX + i * wSz * 2 + wSz * j * 2, wY - j * wSz * 5, wSz, wCol, wWin)

icRad = 100
winFactor = 10
winX = icRad * winFactor
winY = icRad * winFactor

icWin = GraphWin("Have a cone!", winX, winY)
icWin.setCoords(0, 0, winX, winY)

draw_circ(winX / 2, winY / 2 + icRad, icRad, "pink", icWin)
draw_cone(winX, winY, icRad, "orange", icWin)
draw_waffles((winX / 2 - icRad - 2) + icRad / 5,
            (winY / 2 + icRad * .75) - icRad / 5,
            icRad/10, "brown", icWin)
            
         
         
