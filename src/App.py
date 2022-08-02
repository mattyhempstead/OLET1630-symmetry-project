from lib import print, canvas, ctx, canvas_set_background_color
from lib import canvas_on_click, canvas_on_resize

from Button import Button
from FundamentalDomain import FundamentalDomain


class App:
    def __init__(self):
        canvas_set_background_color("#ddd")

        self.btn_next = Button(
            x = -100,
            y = -100,
            text = "Next Iteration"
        )

        self.fd_set = set()
        self.fd_set.add(FundamentalDomain())



    def start(self):
        self.draw() 

        canvas_on_resize(self.draw)


    def draw(self):

        for fd in self.fd_set:
            fd.draw()


        self.btn_next.draw()

