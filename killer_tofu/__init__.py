import muffin


app = muffin.Application('killer_tofu')


@app.register('/', '/hello/{name}')
def hello(request):
    name = request.match_info.get('name', 'anonymous')
    return 'Hello %s!' % name