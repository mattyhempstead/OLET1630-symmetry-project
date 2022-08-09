from datetime import datetime
from js import document, Math, setInterval, console
from pyodide import create_proxy

from lib import print, canvas, ctx, canvas_on_click


from App import App


app = App()
app.start()
