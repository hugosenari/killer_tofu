import muffin

from .app import killer_tofu as app
from .music import Music

@app.register('/', '/hello/{name}')
def hello(request):
    return '{"msgs":["Hello anonymous!"]}'