# iceCream by LevStar and LevStar

from graphics import *

def draw_circ(cX, cY, cRad, cCol, cWin):
    circ = Circle(Point(cX, cY), cRad)
    circ.setFill(cCol)
    circ.setOutline(cCol)
    circ.draw(cWin)

icRad = 50
winFactor = 10
winX = icRad * winFactor
winY = icRad * winFactor

icWin = GraphWin("Have a cone!", winX, winY)
icWin.setCoords(0, 0, winX, winY)

draw_circ(winX / 2, winY / 2 + icRad, icRad, "pink", icWin)

