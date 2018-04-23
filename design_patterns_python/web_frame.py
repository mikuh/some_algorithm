import asyncio
from aiohttp import web

async def index(request):
    res = {"success": True, "data": "Welcome to use PYEF"}
    print(request.rel_url.query.get('name', None))
    return web.json_response(res)

async def hello(request):
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8003)
    print('Server started at http://127.0.0.1:8003...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()