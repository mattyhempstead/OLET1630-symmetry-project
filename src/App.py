import random

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
        self.btn_next.on_click = self.iterate

        self.fd_set = set()
        self.fd_set.add(FundamentalDomain())

        print(hash(FundamentalDomain()) in self.fd_set)
        print(hash(FundamentalDomain(0,1)) in self.fd_set)


    def start(self):
        self.draw() 

        canvas_on_resize(self.draw)


    def draw(self):

        for fd in self.fd_set:
            fd.draw()


        self.btn_next.draw()


    def iterate(self):

        fd_next_list = []

        for fd in self.fd_set:
            fd_next_list += [fdn for fdn in fd.next_iteration() if fdn not in self.fd_set]

        fd_next = random.choice(fd_next_list)
        self.fd_set.add(fd_next)

        self.draw()
