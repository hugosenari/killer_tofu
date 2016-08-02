from .app import killer_tofu as app

import muffin
import asyncio


@app.register('/music', '/music/{mid}')
class Music(muffin.Handler):

    @asyncio.coroutine
    def post(self, request):
        mid = request.match_info.get('mid', False)
        if mid:
            return mid
        return 'POST'

    @asyncio.coroutine
    def get(self, request):
        mid = request.match_info.get('mid', False)
        if mid:
            return mid
        return dir(request)

    @asyncio.coroutine
    def delete(self, request):
        mid = request.match_info.get('mid', False)
        if mid:
            return mid
        return 'DELETE'
