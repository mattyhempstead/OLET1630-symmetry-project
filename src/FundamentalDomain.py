import math

from lib import print, canvas, ctx, canvas_on_click
from lib_draw import draw_circle, draw_line, draw_polygon


class FundamentalDomain:
    def __init__(self, tile_x:int=0, tile_y:int=0):

        self.tile_x = tile_x
        self.tile_y = tile_y


        self.r = 7

        self.tile_size = 200
        # The side length of the tile
        # For Rhombus tiles, this also means the side length of the equilateral triangles


    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.tile_x, self.tile_y))

    @property
    def x(self):
        return canvas.width/2 + self.tile_x*self.tile_size - self.tile_y*self.tile_size_30

    @property
    def y(self):
        return canvas.height/2 + self.tile_y*self.tile_size_60

    @property
    def tile_size_30(self):
        """ sin(30 degrees) * tile_size """
        return math.sin(math.pi/6) * self.tile_size

    @property
    def tile_size_60(self):
        """ sin(60 degrees) * tile_size """
        return math.sin(math.pi/3) * self.tile_size

    @property
    def tile_TL(self):
        return (
            self.x - self.tile_size_30/2,
            self.y - self.tile_size_60/2,
        )

    @property
    def tile_TR(self):
        return (
            self.x + self.tile_size_60 * math.sin(math.pi/3),
            self.y - self.tile_size_60/2,
        )

    @property
    def tile_BR(self):
        return (
            self.x + self.tile_size_30/2,
            self.y + self.tile_size_60/2,
        )

    @property
    def tile_BL(self):
        return (
            self.x - self.tile_size_60 * math.sin(math.pi/3),
            self.y + self.tile_size_60/2,
        )

    def draw(self):

        draw_circle(
            self.x, self.y, self.r,
            # stroke_color="black", stroke_width=3
            fill_color="black",
        )

        # draw_line(
        #     self.x, self.y,
        #     self.x + 100, self.y,
        #     stroke_width = 3
        # )

        draw_polygon(
            [
                self.tile_TL,
                self.tile_TR,
                self.tile_BR,
                self.tile_BL,
            ],
            stroke_width = 3
        )



    def draw_recursive(self):
        pass


    def next_iteration(self):
        """
            For now, return a random next sequence.
            The pure translation signature allows for 4 directions of movement (NESW).
        """
        return [
            FundamentalDomain(
                tile_x = self.tile_x + 1,
                tile_y = self.tile_y
            ),
            FundamentalDomain(
                tile_x = self.tile_x - 1,
                tile_y = self.tile_y
            ),
            FundamentalDomain(
                tile_x = self.tile_x,
                tile_y = self.tile_y + 1
            ),
            FundamentalDomain(
                tile_x = self.tile_x,
                tile_y = self.tile_y - 1
            ),
        ]

