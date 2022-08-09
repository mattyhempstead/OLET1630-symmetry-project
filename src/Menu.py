from typing import Callable
import random

from lib import print, canvas, ctx, canvas_set_background_color, load_image
from lib import canvas_on_click, canvas_on_resize
from lib_draw import draw_circle, draw_line, draw_polygon, toggle_coord_space, draw_image, draw_text

from Button import Button
import FundamentalDomain as FDomain
from Pattern import Pattern


class Menu:
    def __init__(self, app):
        self.app = app


        self.fd_list = [
            FDomain.P1,
            FDomain.P2,
            FDomain.P4,
            FDomain.P6,
            FDomain.PMM,
        ]


        self.btn_list = []


        for i,fd_class in enumerate(self.fd_list):
            btn = Button(
                x = canvas.width/2,
                y = 300 + 70*i,
                center_x = True,
                text = f"Signature: {fd_class.signature}",
                on_click = self.pick_signature,
                on_click_kw = {"fd": fd_class}
            )
            self.btn_list.append(btn)




    def enable(self):
        for btn in self.btn_list:
            btn.enable()

    def disable(self):
        for btn in self.btn_list:
            btn.disable()


    def pick_signature(self, fd):
        self.app.set_state(Pattern(self.app, fd))


    def draw(self):

        draw_text(
            "Kaleidorate",
            canvas.width/2,
            100,
            text_color = "black",
            font_size = 50,
        )

        for btn in self.btn_list:
            btn.draw()

