from .app import killer_tofu as app, result, collection
import muffin
import asyncio

def fingerprint(request, exc=Exception('undefined AcoustID')):
    fingerprint = str(request.match_info.get('fingerprint', None))
    if exc and not fingerprint:
        raise exc
    return fingerprint

def fix_id(doc):
    doc['_id'] = str(doc.get('_id'))
    return doc

def assert_found(doc):
    if not doc:
        raise Exception('unknow AcoustID')

def assert_delete(auid, r):
    if not r or not r.get('ok'):
        raise Exception("Can't remove {}".format(auid))
    
def set_id(auid, doc=None):
    result = doc or {}
    result['fingerprint'] = auid
    data = yield from collection().find_one({'fingerprint': auid})
    if data:
        result['_id'] = data.get('_id')
    return result

@app.register('/music/{fingerprint}')
class Music(muffin.Handler):

    @asyncio.coroutine
    def get(self, request):
        doc = yield from collection().find_one({'fingerprint': fingerprint(request)})
        assert_found(doc)
        return result(fix_id(doc))

    @asyncio.coroutine
    def post(self, request):
        _fingerprint = fingerprint(request)
        doc = yield from self.parse(request)
        doc = set_id(_fingerprint, doc)
        doc['_id'] = yield from collection().save(doc)
        return result(fix_id(doc))

    @asyncio.coroutine
    def delete(self, request):
        _fingerprint = fingerprint(request)
        doc = set_id(_fingerprint)
        r = yield from collection().remove(doc)
        assert_delete(_fingerprint, r)
        return result()
