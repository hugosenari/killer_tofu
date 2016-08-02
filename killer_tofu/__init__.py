import muffin

from .app import killer_tofu as app
from .music import Music

@app.register('/', '/hello/{name}')
def hello(request):
    name = request.match_info.get('name', 'anonymous')
    return 'Hellos %s!' % name
