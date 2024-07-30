from fubuki import Controller, get, Request
from fubuki.response import JSONResponse
from fubuki.template import TemplateResponse

class HomeController(Controller):
    @get('/')
    async def welcome(request: Request):
        return TemplateResponse("index.html")

    @get(r'/users/(?P<user_id>\d+)')
    async def get_user(request: Request, user_id):
        return JSONResponse({"Id": user_id})

    @get(r'/posts/(?P<post_slug>[a-z0-9_-]{3,16})')
    async def get_post(request: Request, post_slug):
        return JSONResponse({"Slug": post_slug})