from typing import Callable
import random

from lib import print, canvas, ctx, canvas_set_background_color, load_image
from lib import canvas_on_click, canvas_on_resize
from lib_draw import draw_circle, draw_line, draw_polygon, toggle_coord_space, draw_image

from Button import Button
import FundamentalDomain as FDomain


class Pattern:
    def __init__(self, app, fd_class):
        self.app = app


        # self.fd_class = FDomain.P1
        # self.fd_class = FDomain.P2
        # self.fd_class = FDomain.P4
        # self.fd_class = FDomain.P6
        # self.fd_class = FDomain.PMM
        self.fd_class = fd_class

        self.fd_set = set()
        self.fd_set.add(self.fd_class())

        # self.fd_set.add(self.fd_class(0,1,True,True))

        # self.fd_set.add(self.fd_class(0,0,0,1))
        # self.fd_set.add(self.fd_class(0,0,0,2))

        # self.fd_set.add(self.fd_class(1,0,0,1))
        # self.fd_set.add(self.fd_class(0,1,0,1))

        # self.fd_set.add(self.fd_class(0,0,1,2))
        
        # self.fd_set.add(self.fd_class(0,0,False))

        # self.fd_set.add(self.fd_class(1,0,False))
        # self.fd_set.add(self.fd_class(1,0,True))

        # self.fd_set.add(self.fd_class(1,1,True))


        self.fd_iteration_types = self.fd_class.iteration_types()
        print(self.fd_iteration_types)
        # print(hash(FundamentalDomain()) in self.fd_set)
        # print(hash(FundamentalDomain(0,1)) in self.fd_set)


        self.btn_list = []

        for i,iter_type in enumerate(self.fd_iteration_types):
            iter_name, iter_method = iter_type
            btn = Button(
                x = -100,
                y = -100 - 70*i,
                text = f"Next Iteration ({iter_name})",
                on_click = self.iterate,
                on_click_kw = {"iter_method": iter_method}
            )
            self.btn_list.append(btn)

        btn = Button(
            x = 50,
            y = 50,
            text = f"Back to Menu",
            on_click = self.open_menu,
            # on_click_kw = {"fd": 1},
        )
        self.btn_list.append(btn)


        # self.fd_class.img_rotate4 = load_image(
        #     "resources/rotate4.png",
        #     on_load = self.draw
        # )

        # self.fd_class.img_rotate2 = load_image(
        #     "resources/rotate2.png",
        #     on_load = self.draw
        # )


    def open_menu(self):
        self.app.set_state(self.app.menu)


    def draw(self):

        toggle_coord_space(True)

        for fd in self.fd_set:
            fd.draw()

        draw_circle(
            0, 0, 4,
            fill_color="blue",
        )

        toggle_coord_space(False)


        for btn in self.btn_list:
            btn.draw()


    def iterate(self, iter_method:Callable):

        fd_next_list = set()

        for fd in self.fd_set:
            fdn_list = iter_method(fd)
            # print("next", fdn_list)
            fdn_list = {fdn for fdn in fdn_list if fdn not in self.fd_set}
            # print("adding", fdn_list)

            fd_next_list |= fdn_list

        # print(str([(x.tile_x, x.tile_y) for x in fd_next_list]))

        # Add one randomly
        # fd_next = random.choice(fd_next_list)
        # self.fd_set.add(fd_next)

        # Add all fds
        for fdn in fd_next_list:
            self.fd_set.add(fdn)

        self.draw()


    def enable(self):
        for btn in self.btn_list:
            btn.enable()

    def disable(self):
        for btn in self.btn_list:
            btn.disable()

