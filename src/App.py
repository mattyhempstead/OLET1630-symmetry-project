from typing import Callable
import random

from lib import print, canvas, ctx, canvas_set_background_color, load_image
from lib import canvas_on_click, canvas_on_resize
from lib_draw import draw_circle, draw_line, draw_polygon, toggle_coord_space, draw_image

from Button import Button
from Menu import Menu
from Pattern import Pattern
import FundamentalDomain as FDomain


class App:
    def __init__(self):


        self.menu = Menu(self)

        self.state = self.menu



    def start(self):
        canvas_set_background_color("#ddd")
        canvas_on_resize(self.draw)

        self.state.enable()
        self.draw() 


    def draw(self):
        ctx.clearRect(0, 0, canvas.width, canvas.height)

        self.state.draw()


    def set_state(self, state):
        print("Changing state")

        self.state.disable()
        self.state = state
        self.state.enable()

        self.draw()
