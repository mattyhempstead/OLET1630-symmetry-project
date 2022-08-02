from lib import print, canvas, ctx, canvas_on_click


class Button:
    def __init__(
        self,
        x:int = 0,
        y:int = 0,
        w:int = None,
        h:int = None,

        text:str = "Button",
        text_color:str = "#000",
        text_size:int = 25,

        fill_color:str = "#888",

        stroke_color:str = "#555",
        stroke_width:str = 3,
    ):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.fill_color = fill_color

        self.stroke_color = stroke_color
        self.stroke_width = stroke_width

        self.text = text
        self.text_color = text_color
        self.text_size = text_size

        canvas_on_click(self.on_click_listener)


    def on_click_listener(self, x, y, **kwargs):
        if x < self._x or x > self._x + self._w:
            return
        if y < self._y or y > self._y + self._h:
            return
        self.on_click()

    def on_click(self):
        print("Clicked button")

    @property
    def _font(self):
        return f"{self.text_size}px Arial"

    @property
    def _x(self):
        if self.x >= 0:
            return self.x
        else:
            return canvas.width - self._w + self.x

    @property
    def _y(self):
        if self.y >= 0:
            return self.y
        else:
            return canvas.height - self._h + self.y

    @property
    def _w(self):
        if self.w is None:
            temp_font = ctx.font
            ctx.font = self._font
            text_width = ctx.measureText(self.text).width
            ctx.font = temp_font
            return text_width + self.text_size
        else:
            return self.w

    @property
    def _h(self):
        if self.h is None:
            return self.text_size*2
        else:
            return self.h

    @property
    def x_center(self):
        return self._x + self._w/2
    
    @property
    def y_center(self):
        return self._y + self._h/2

    def draw(self):

        ctx.fillStyle = self.fill_color
        ctx.beginPath()
        ctx.rect(self._x, self._y, self._w, self._h)
        ctx.fill()

        ctx.strokeStyle = self.stroke_color
        ctx.lineWidth = self.stroke_width
        ctx.beginPath()
        ctx.rect(self._x, self._y, self._w, self._h)
        ctx.stroke()

        ctx.fillStyle = self.text_color
        ctx.font = self._font
        ctx.textAlign = "center"
        ctx.textBaseline = "middle"
        ctx.fillText(self.text, self.x_center, self.y_center)
