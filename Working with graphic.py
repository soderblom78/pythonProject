from graphics import *


def main():
    win = GraphWin("Roger", 500, 500)
    win.setBackground(color_rgb(255, 255, 255))


    img = Image(Point(250, 250), "images/green monster.png")
    img.draw(win)

    txt = Text(Point(250, 50), "What´s up")
    txt.setTextColor(color_rgb(0, 255, 200))
    txt.setSize(30)
    txt.setFace("arial")
    txt.draw(win)

    win.getMouse()
    win.close()



main()
