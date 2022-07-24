from lib import print, canvas, ctx, canvas_on_click


class Button:
    def __init__(
        self,
        x:int = 0,
        y:int = 0,
        w:int = 100,
        h:int = 50,

        text:str = "Button",
        text_color:str = "#000",
        text_size:int = 25,

        fill_color:str = "#888",

        stroke_color:str = "#555",
        stroke_width:str = 5,
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
        if x < self.x or x > self.x + self.w:
            return
        if y < self.y or y > self.y + self.h:
            return
        self.on_click()


    def on_click(self):
        print("Clicked button")

    @property
    def x_center(self):
        return self.x + self.w/2
    
    @property
    def y_center(self):
        return self.y + self.h/2

    def draw(self):

        ctx.fillStyle = self.fill_color
        ctx.beginPath()
        ctx.rect(self.x, self.y, self.w, self.h)
        ctx.fill()

        ctx.strokeStyle = self.stroke_color
        ctx.lineWidth = self.stroke_width
        ctx.beginPath()
        ctx.rect(self.x, self.y, self.w, self.h)
        ctx.stroke()

        ctx.fillStyle = self.text_color
        ctx.font = f"{self.text_size}px Arial"
        ctx.textAlign = "center"
        ctx.fillText(self.text, self.x_center, self.y_center)
