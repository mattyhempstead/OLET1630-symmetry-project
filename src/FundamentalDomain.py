import math
import numpy as np

from lib import print, canvas, ctx, canvas_on_click
from lib_draw import draw_circle, draw_line, draw_polygon, toggle_coord_space, draw_image


class FundamentalDomain:
    def __init__(self):

        self.r = 5

        self.tile_size = 150
        # The side length of the tile
        # For Rhombus tiles, this also means the side length of the equilateral triangles


        self.transform_stack = []


    def __repr__(self):
        return str(self.coord)

    def __hash__(self):
        # Note that this doesn't need to be unique, but it should try to be as much as possible.
        return hash(self.coord)

    def __eq__(self, other):
        return self.coord == other.coord


    def np_coords(self, x, y):
        return np.array([[x],[y]])

    @property
    def mat_rhombus_skew(self):
        return np.array([
            [1, 0.5],
            [0, math.sin(math.pi/3)]
        ])

    @property
    def x(self) -> int:
        pass

    @property
    def y(self) -> int:
        pass

    def draw(self):
        pass
        # draw_circle(
        #     0, 0, self.r,
        #     # stroke_color="black", stroke_width=3
        #     fill_color="black",
        # )


    def transform_stack_pop(self, until_empty:bool=False):
        # Pops most recent transformation on stack and executes it
        while True:
            transformation = self.transform_stack.pop()
            transformation[0](*transformation[1])  # Run method

            if not until_empty or len(self.transform_stack) == 0:
                break

    def transform_translate(self, x, y):
        ctx.translate(x, y)
        transformation = (ctx.translate, [-x, -y])
        self.transform_stack.append(transformation)

    def transform_translate_vector(self, vec):
        """ Translate a 2D vector """
        ctx.translate(vec[0], vec[1])
        transformation = (ctx.translate, [-vec[0], -vec[1]])
        self.transform_stack.append(transformation)

    def transform_rotate(self, radians):
        ctx.rotate(radians)
        transformation = (ctx.rotate, [-radians])
        self.transform_stack.append(transformation)

    def transform_flip(self, x:bool=False, y:bool=False):
        scale_x = -1 if x else 1
        scale_y = -1 if y else 1
        ctx.scale(scale_x, scale_y)
        transformation = (ctx.scale, [scale_x, scale_y])
        self.transform_stack.append(transformation)



class P1(FundamentalDomain):
    signature = "o"

    def __init__(self, tile_x:int=0, tile_y:int=0):
        super().__init__()

        self.tile_x = tile_x
        self.tile_y = tile_y

    @property
    def coord(self):
        return (self.tile_x, self.tile_y)


    def draw(self):
        super().draw()

        map_rhombus_coord = lambda c: self.tile_size * np.matmul(self.mat_rhombus_skew, c)

        grd = ctx.createLinearGradient(0,0,50,50)
        grd.addColorStop(0, "red")
        grd.addColorStop(0.5, "green")
        grd.addColorStop(1, "blue")


        coord_tile = np.array([self.tile_x, self.tile_y])
        coord_tile = map_rhombus_coord(coord_tile)

        coord_BL = np.array([-0.5,-0.5])
        coord_BL = map_rhombus_coord(coord_BL)

        coord_TL = np.array([-0.5, 0.5])
        coord_TL = map_rhombus_coord(coord_TL)

        coord_TR = np.array([ 0.5, 0.5])
        coord_TR = map_rhombus_coord(coord_TR)

        coord_BR = np.array([ 0.5,-0.5])
        coord_BR = map_rhombus_coord(coord_BR)

        self.transform_translate_vector(coord_tile)

        draw_polygon(
            [coord_BL, coord_TL, coord_TR, coord_BR],
            stroke_width = 1,
            fill_color = grd,
        )

        self.transform_stack_pop(until_empty=True)




    @classmethod
    def iteration_types(cls):
        return [
            ("Translate North", P1.next_iteration_T_N),
            ("Translate South", P1.next_iteration_T_S),
            ("Translate East", P1.next_iteration_T_E),
            ("Translate West", P1.next_iteration_T_W),
        ]

    def next_iteration_T_N(self):
        return [
            P1(
                self.tile_x,
                self.tile_y + 1,
            ),
        ]

    def next_iteration_T_S(self):
        return [
            P1(
                self.tile_x,
                self.tile_y - 1,
            ),
        ]

    def next_iteration_T_E(self):
        return [
            P1(
                self.tile_x + 1,
                self.tile_y,
            ),
        ]

    def next_iteration_T_W(self):
        return [
            P1(
                self.tile_x - 1,
                self.tile_y,
            ),
        ]





class P2(FundamentalDomain):
    signature = "2222"

    def __init__(self, tile_x:int = 0, tile_y:int=0, tile_rot:bool=False):
        super().__init__()

        self.tile_x = tile_x
        self.tile_y = tile_y
        self.tile_rot = tile_rot


    @property
    def coord(self):
        return (self.tile_x, self.tile_y, self.tile_rot)


    def draw(self):
        super().draw()

        map_rhombus_coord = lambda c: self.tile_size * np.matmul(self.mat_rhombus_skew, c)

        grd = ctx.createLinearGradient(0,0,50,50)
        grd.addColorStop(0, "red")
        grd.addColorStop(0.5, "green")
        grd.addColorStop(1, "blue")


        coord_tile = np.array([self.tile_x, self.tile_y])
        coord_tile = map_rhombus_coord(coord_tile)

        coord_BL = np.array([-0.5,-0.5])
        coord_BL = map_rhombus_coord(coord_BL)

        coord_TL = np.array([-0.5, 0.5])
        coord_TL = map_rhombus_coord(coord_TL)

        coord_TR = np.array([ 0.5, 0.5])
        coord_TR = map_rhombus_coord(coord_TR)

        coord_BR = np.array([ 0.5,-0.5])
        coord_BR = map_rhombus_coord(coord_BR)

        self.transform_translate_vector(coord_tile)
        self.transform_rotate(-self.tile_rot * math.pi)

        draw_polygon(
            [coord_BL, coord_TL, coord_TR, coord_BR],
            stroke_width = 1,
            fill_color = grd,
        )

        self.transform_stack_pop(until_empty=True)


    @classmethod
    def iteration_types(cls):
        return [
            ("Rotate North", P2.next_iteration_R_N),
            ("Rotate South", P2.next_iteration_R_S),
            ("Rotate East", P2.next_iteration_R_E),
            ("Rotate West", P2.next_iteration_R_W),
        ]

    def next_iteration_R_N(self):
        return [
            P2(
                self.tile_x,
                self.tile_y + 1,
                not self.tile_rot,
            ),
        ]

    def next_iteration_R_S(self):
        return [
            P2(
                self.tile_x,
                self.tile_y - 1,
                not self.tile_rot,
            ),
        ]

    def next_iteration_R_E(self):
        return [
            P2(
                self.tile_x + 1,
                self.tile_y,
                not self.tile_rot,
            ),
        ]

    def next_iteration_R_W(self):
        return [
            P2(
                self.tile_x - 1,
                self.tile_y,
                not self.tile_rot,
            ),
        ]


class P4(FundamentalDomain):
    signature = "442"

    def __init__(self, tile_x:int = 0, tile_y:int=0, tile_rot:int=0):
        super().__init__()

        self.tile_x = tile_x
        self.tile_y = tile_y
        self.tile_rot = tile_rot # 0,1,2,3 clockwise from BL


    @property
    def coord(self):
        return (self.tile_x, self.tile_y, self.tile_rot)


    def draw(self):
        super().draw()

        grd = ctx.createLinearGradient(0,0,50,50)
        grd.addColorStop(0, "red")
        grd.addColorStop(0.5, "green")
        grd.addColorStop(1, "blue")


        coord_tile = self.tile_size * np.array([self.tile_x, self.tile_y])

        coord_BL = np.array([-0.5,-0.5]) * self.tile_size
        coord_TL = np.array([-0.5, 0.5]) * self.tile_size
        coord_TR = np.array([ 0.5, 0.5]) * self.tile_size
        coord_BR = np.array([ 0.5,-0.5]) * self.tile_size

        self.transform_translate_vector(coord_tile)
        self.transform_rotate(-self.tile_rot * math.pi/2)

        draw_polygon(
            [coord_BL, coord_TL, coord_TR, coord_BR],
            stroke_width = 1,
            fill_color = grd,
        )

        self.transform_stack_pop(until_empty=True)

        # draw_image(self.img_rotate4, coord_TR[0], coord_TR[1], 25, 25)
        # draw_image(self.img_rotate4, coord_BL[0], coord_BL[1], 25, 25)
        # draw_image(self.img_rotate2, coord_TL[0], coord_TL[1], 25, 25)
        # draw_image(self.img_rotate2, coord_BR[0], coord_BR[1], 25, 25)


    @classmethod
    def iteration_types(cls):
        return [
            ("Rotate 4 #1", P4.next_iteration_R4_1),
            ("Rotate 4 #2", P4.next_iteration_R4_2),
            ("Rotate 2", P4.next_iteration_R2),
        ]

    def next_iteration_R4_1(self):
        x_delta,y_delta,rot_new = {
            0: ( 0, 1, 1),
            1: ( 1, 0, 2),
            2: ( 0,-1, 3),
            3: (-1, 0, 0),
        }[self.tile_rot]

        return [
            P4(
                self.tile_x + x_delta,
                self.tile_y + y_delta,
                rot_new,
            ),
        ]

    def next_iteration_R4_2(self):
        x_delta,y_delta,rot_new = {
            0: ( 0,-1, 1),
            1: (-1, 0, 2),
            2: ( 0, 1, 3),
            3: ( 1, 0, 0),
        }[self.tile_rot]

        return [
            P4(
                self.tile_x + x_delta,
                self.tile_y + y_delta,
                rot_new
            ),
        ]

    def next_iteration_R2(self):
        x_delta,y_delta,rot_new = {
            0: (-1, 1, 2),
            1: ( 1, 1, 3),
            2: ( 1,-1, 0),
            3: (-1,-1, 1),
        }[self.tile_rot]

        return [
            P4(
                self.tile_x + x_delta,
                self.tile_y + y_delta,
                rot_new
            ),
        ]



class P6(FundamentalDomain):
    signature = "632"

    def __init__(self, tile_x:int = 0, tile_y:int=0, tile_triangle:int=0, tile_rot:int=0):
        super().__init__()

        self.tile_x = tile_x
        self.tile_y = tile_y
        self.tile_triangle = tile_triangle # 0 or 1 (bottom or top)
        self.tile_rot = tile_rot # 0,1,2 clockwise from bottom OR top

        self.tile_size = 300

    @property
    def coord(self):
        return (self.tile_x, self.tile_y, self.tile_triangle, self.tile_rot)


    def draw(self):
        super().draw()

        grd = ctx.createLinearGradient(0,0,50,50)
        grd.addColorStop(0, "red")
        grd.addColorStop(0.5, "green")
        grd.addColorStop(1, "blue")


        coord_tile = self.tile_size * np.array([self.tile_x, self.tile_y])
        coord_tile = np.matmul(self.mat_rhombus_skew, coord_tile)
        ctx.translate(coord_tile[0], coord_tile[1])


        # Coords are positions at center of triangle
        coord_center = np.array([0.5, 0.25*math.tan(math.pi/6)]) * self.tile_size
        coord_B1 = np.array([0,0]) * self.tile_size
        coord_B2 = np.array([1,0]) * self.tile_size
        coord_T = np.array([0.5,0.5*math.tan(math.pi/6)]) * self.tile_size
        coords = np.array([coord_B1, coord_B2, coord_T])
        coords -= coord_center

        # Triangle rotation point
        coord_tri = np.matmul(self.mat_rhombus_skew, [0.5,0.5]) * self.tile_size


        # Make origin the center of triangle
        self.transform_translate_vector(coord_tri-coord_center)

        # Rotate triangle
        self.transform_rotate(self.tile_triangle * math.pi)

        # Make origin the triangle rotation point
        self.transform_translate_vector(-coord_tri)

        # Make center the bottom left
        self.transform_translate_vector(coord_T)

        # Rotate inner 3 from top of triangle
        self.transform_rotate(-self.tile_rot * math.pi * 2/3)

        # Make origin the top middle
        self.transform_translate_vector(-coord_T)

        # Make origin the bottom left
        self.transform_translate_vector(coord_center)

        # Draw origin in middle of triangle
        draw_polygon(
            coords,
            stroke_width = 1,
            fill_color = grd,
        )

        self.transform_stack_pop(until_empty=True)


        # draw_image(self.img_rotate4, coord_TR[0], coord_TR[1], 25, 25)
        # draw_image(self.img_rotate4, coord_BL[0], coord_BL[1], 25, 25)
        # draw_image(self.img_rotate2, coord_TL[0], coord_TL[1], 25, 25)
        # draw_image(self.img_rotate2, coord_BR[0], coord_BR[1], 25, 25)

        ctx.translate(-coord_tile[0], -coord_tile[1])


    @classmethod
    def iteration_types(cls):
        return [
            ("Rotate 2", P6.next_iteration_R2),
            ("Rotate 3", P6.next_iteration_R3),
            ("Rotate 6", P6.next_iteration_R6),
        ]

    def next_iteration_R2(self):
        x_delta,y_delta,tri_new,rot_new = {
            (0,0): (0,-1,1,0),
            (0,1): (-1,0,1,1),
            (0,2): (0,0,1,2),
            (1,0): (0,1,0,0),
            (1,1): (1,0,0,1),
            (1,2): (0,0,0,2),
        }[(self.tile_triangle, self.tile_rot)]

        return [
            P6(
                self.tile_x + x_delta,
                self.tile_y + y_delta,
                tri_new,
                rot_new
            ),
        ]


    def next_iteration_R3(self):
        return [
            P6(
                self.tile_x,
                self.tile_y,
                self.tile_triangle,
                (self.tile_rot+1)%3,
            ),
        ]

    def next_iteration_R6(self):
        
        x_delta,y_delta,tri_new,rot_new = {
            (0,0): (0,-1,1,2),
            (0,1): (-1,0,1,0),
            (0,2): (0,0,1,1),
            (1,0): (0,1,0,2),
            (1,1): (1,0,0,0),
            (1,2): (0,0,0,1),
        }[(self.tile_triangle, self.tile_rot)]

        return [
            P6(
                self.tile_x + x_delta,
                self.tile_y + y_delta,
                tri_new,
                rot_new
            ),
        ]


class PMM(FundamentalDomain):
    signature = "*2222"

    def __init__(self, tile_x:int = 0, tile_y:int=0, flip_x:bool=False, flip_y:bool=False):
        super().__init__()

        self.tile_x = tile_x
        self.tile_y = tile_y
        self.flip_x = flip_x
        self.flip_y = flip_y

    @property
    def coord(self):
        return (self.tile_x, self.tile_y, self.flip_x, self.flip_y)


    def draw(self):
        super().draw()

        grd = ctx.createLinearGradient(0,0,50,50)
        grd.addColorStop(0, "red")
        grd.addColorStop(0.5, "green")
        grd.addColorStop(1, "blue")


        coord_tile = self.tile_size * np.array([self.tile_x, self.tile_y])

        coord_BL = np.array([-0.5,-0.5]) * self.tile_size
        coord_TL = np.array([-0.5, 0.5]) * self.tile_size
        coord_TR = np.array([ 0.5, 0.5]) * self.tile_size
        coord_BR = np.array([ 0.5,-0.5]) * self.tile_size

        self.transform_translate_vector(coord_tile)

        self.transform_flip(x=self.flip_x, y=self.flip_y)

        draw_polygon(
            [coord_BL, coord_TL, coord_TR, coord_BR],
            stroke_width = 1,
            fill_color = grd,
        )

        self.transform_stack_pop(until_empty=True)


    @classmethod
    def iteration_types(cls):
        return [
            ("Mirror North", PMM.next_iteration_M_N),
            ("Mirror South", PMM.next_iteration_M_S),
            ("Mirror East", PMM.next_iteration_M_E),
            ("Mirror West", PMM.next_iteration_M_W),
        ]

    def next_iteration_M_N(self):
        return [
            PMM(
                self.tile_x,
                self.tile_y + 1,
                self.flip_x,
                not self.flip_y,
            ),
        ]

    def next_iteration_M_S(self):
        return [
            PMM(
                self.tile_x,
                self.tile_y - 1,
                self.flip_x,
                not self.flip_y,
            ),
        ]

    def next_iteration_M_E(self):
        return [
            PMM(
                self.tile_x + 1,
                self.tile_y,
                not self.flip_x,
                self.flip_y,
            ),
        ]

    def next_iteration_M_W(self):
        return [
            PMM(
                self.tile_x - 1,
                self.tile_y,
                not self.flip_x,
                self.flip_y,
            ),
        ]
