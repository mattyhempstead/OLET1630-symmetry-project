from typing import Callable
from js import document, Math, setInterval, console, addEventListener
from pyodide import create_proxy


def print(*args, **kwargs):
	console.group("py-script")
	console.log(*args, **kwargs)
	console.groupEnd()


canvas = document.getElementById("canvas")
ctx = canvas.getContext("2d")



"""
    Resize canvas to be same size as window.

    TODO: Probably stop it resizing like 10 times per second while moving.
          Could maybe create a 0.5 timeout which will only execute if the window
          is not resized for the whole 0.5 seconds (meaning we keep cancelling and restarting it).
"""
def canvas_update_size(*args):
    print("Resizing canvas...")
    canvas = document.getElementById("canvas")
    print(canvas, canvas.clientWidth, canvas.clientHeight)
    canvas.width = canvas.clientWidth
    canvas.height = canvas.clientHeight
canvas_update_size()
canvas_update_size_proxy = create_proxy(canvas_update_size)
addEventListener("resize", canvas_update_size_proxy)



def canvas_on_click(func:Callable):
    """
        Adds a trigger which calls func whenever the canvas is clicked.
        Will also pass relevant event kwargs to func.
    """
    canvas = document.getElementById("canvas")

    def temp_func(event):
        # print("Clicked canvas", event)
        # print(event.offsetX, event.offsetY)
        func(
            x = event.offsetX,
            y = event.offsetY,
            w = canvas.width,
            h = canvas.height,
            x_ratio = event.offsetX / canvas.width,  # x pos as a ratio of width
            y_ratio = event.offsetY / canvas.height, # y pos as a ratio of height
        )

    on_canvas_click_proxy = create_proxy(temp_func)
    canvas.addEventListener("click", on_canvas_click_proxy)

