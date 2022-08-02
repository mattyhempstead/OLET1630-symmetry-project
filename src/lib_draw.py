from typing import List, Tuple
from lib import print, canvas, ctx, canvas_on_click
from js import Math


def draw_circle(
    x:int,
    y:int,
    r:int,
    stroke_color: str = None,
    stroke_width: int = 1,
    fill_color: str = None,
):

    ctx.beginPath()
    ctx.arc(x, y, r, 0, 2*Math.PI)

    if fill_color is not None:
        ctx.fillStyle = fill_color
        ctx.fill()

    if stroke_color is not None:
        ctx.strokeStyle = stroke_color
        ctx.lineWidth = stroke_width
        ctx.stroke()


def draw_line(
    x1:int,
    y1:int,
    x2:int,
    y2:int,
    stroke_color: str = "black",
    stroke_width: int = 1,
):
    ctx.lineCap = "round"
    ctx.lineWidth = stroke_width
    ctx.strokeStyle = stroke_color

    ctx.beginPath()
    ctx.moveTo(x1, y1)
    # ctx.rotate(pos)
    ctx.lineTo(x2, y2)
    ctx.closePath()
    ctx.stroke()
    # ctx.rotate(-pos)


def draw_polygon(
    points:List[Tuple[int,int]], # (x,y) tuples
    stroke_color: str = "black",
    stroke_width: int = 1,
):
    print(points)

    if len(points) < 2:
        raise Exception("Polygon has at least two points")

    ctx.lineCap = "round"
    ctx.lineWidth = stroke_width
    ctx.strokeStyle = stroke_color

    ctx.beginPath()
    ctx.moveTo(points[0][0], points[0][1])
    for p in points[1:]:
        ctx.lineTo(p[0], p[1])

    ctx.closePath()
    ctx.stroke()

