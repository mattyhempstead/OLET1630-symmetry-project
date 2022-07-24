
from datetime import datetime
from js import document, Math, setInterval, console
from pyodide import create_proxy

from lib import print, canvas, ctx, canvas_on_click

from Button import Button


btn = Button()


def drawClock(ctx, radius):
	drawFace(ctx, radius)
	drawNumbers(ctx, radius)
	drawTime(ctx, radius)

	btn.draw()

 
def drawFace(ctx, radius):
	ctx.beginPath()
	ctx.arc(0, 0, radius, 0, 2 * Math.PI)
	ctx.fillStyle = 'white'
	ctx.fill()
	grad = ctx.createRadialGradient(0,0,radius*0.95, 0,0,radius*1.05)
	grad.addColorStop(0, '#333')
	grad.addColorStop(0.5, 'white')
	grad.addColorStop(1, '#333')
	ctx.strokeStyle = grad
	ctx.lineWidth = radius * 0.1
	ctx.stroke()
	ctx.beginPath()
	ctx.arc(0, 0, radius*0.1, 0, 2 * Math.PI)
	ctx.fillStyle = '#333'
	ctx.fill()
 
def drawNumbers(ctx, radius):
	ctx.font = str(radius * 0.15) + "px arial"
	ctx.textBaseline = "middle"
	ctx.textAlign = "center"
	for num in range(1, 13):
		ang = num * Math.PI / 6
		ctx.rotate(ang)
		ctx.translate(0, -radius * 0.85)
		ctx.rotate(-ang)
		ctx.fillText(str(num), 0, 0)
		ctx.rotate(ang)
		ctx.translate(0, radius * 0.85)
		ctx.rotate(-ang)
 
def drawTime(ctx, radius):
	now = datetime.now()
 
	hour = now.hour
	minute = now.minute
	second = now.second
 
	# hour
	hour = hour % 12
	hour = (hour * Math.PI / 6)
	hour += (minute * Math.PI / (6*60))
	hour += (second * Math.PI / (360 * 60))
 
	drawHand(ctx, hour, radius*0.5, radius*0.07)
 
	# minute
	minute = (minute * Math.PI / 30)
	minute += (second * Math.PI / (30 * 60))
 
	drawHand(ctx, minute, radius * 0.8, radius * 0.07)
 
	#  second
	second = second * Math.PI / 30
	drawHand(ctx, second, radius * 0.9, radius * 0.02)
 
def drawHand(ctx, pos, length, width):
	ctx.beginPath()
	ctx.lineWidth = width
	ctx.lineCap = "round"
	ctx.moveTo(0,0)
	ctx.rotate(pos)
	ctx.lineTo(0, -length)
	ctx.stroke()
	ctx.rotate(-pos)
 


radius = canvas.height / 2
ctx.translate(radius, radius)
radius = radius * 0.90

drawClock(ctx, radius)

drawClock_proxy = create_proxy(drawClock)

interval_id = setInterval(drawClock_proxy, 1000, ctx, radius)
 


# def canvas_click(x, y, **kwargs):
# 	print("Clicked canvas", x, y)
# 	print(**kwargs)

# canvas_on_click(canvas_click)
