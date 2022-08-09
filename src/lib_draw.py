from typing import List, Tuple
from lib import print, canvas, ctx, canvas_on_click
from js import Math, document


def toggle_coord_space(toggle:bool):
    if toggle:
        ctx.translate(canvas.width, 0)
        ctx.scale(1, -1)
        ctx.translate(-canvas.width/2, -canvas.height/2)
    else:
        ctx.translate(canvas.width/2, canvas.height/2)
        ctx.scale(1, -1)
        ctx.translate(-canvas.width, 0)


def draw_circle(
    x:int,
    y:int,
    r:int,
    stroke_color: str = None,
    stroke_width: int = 1,
    fill_color: str = None,
):
    # toggle_coord_space(True)

    ctx.beginPath()
    ctx.arc(x, y, r, 0, 2*Math.PI)

    if fill_color is not None:
        ctx.fillStyle = fill_color
        ctx.fill()

    if stroke_color is not None:
        ctx.strokeStyle = stroke_color
        ctx.lineWidth = stroke_width
        ctx.stroke()

    # toggle_coord_space(False)



def draw_line(
    x1:int,
    y1:int,
    x2:int,
    y2:int,
    stroke_color: str = "black",
    stroke_width: int = 1,
):
    # toggle_coord_space(True)

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

    # toggle_coord_space(False)


def draw_polygon(
    points:List[Tuple[int,int]], # (x,y) tuples
    stroke_color: str = "black",
    stroke_width: int = 1,
    fill_color: str = None,
):
    # toggle_coord_space(True)
    # print(points)

    if len(points) < 2:
        raise Exception("Polygon has at least two points")

    if stroke_color is not None:
        ctx.lineCap = "round"
        ctx.lineWidth = stroke_width
        ctx.strokeStyle = stroke_color
    if fill_color is not None:
        ctx.fillStyle = fill_color

    ctx.beginPath()
    ctx.moveTo(points[0][0], points[0][1])
    for p in points[1:]:
        ctx.lineTo(p[0], p[1])
    ctx.closePath()

    if stroke_color is not None:
        ctx.stroke()
    if fill_color is not None:
        ctx.fill()



    # Write an F in the middle to show rotation
    # ctx.rotate(Math.PI)
    ctx.scale(1,-1)
    ctx.fillStyle = "black"
    ctx.font = "20px Arial"
    ctx.textAlign = "center"
    ctx.textBaseline = "middle"
    ctx.fillText("F", 0, 0)
    ctx.scale(1,-1)
    # ctx.rotate(Math.PI)

    # toggle_coord_space(False)



def draw_image(
    img,
    x:int,
    y:int,
    w:int,
    h:int,
    center:bool = True
):
    if center:
        x -= w/2
        y -= h/2

    ctx.drawImage(img, x, y, w, h)


def draw_text(
    text:str,
    x:int,
    y:int,
    text_color:str = "black",
    font_size:int = 20,
    center:bool = True,
):
    ctx.fillStyle = text_color
    ctx.font = f"{font_size}px Arial"

    if center:
        ctx.textAlign = "center"
        ctx.textBaseline = "middle"

    ctx.fillText(text, x, y)
