import os
from starlette.applications import Starlette
from starlette.middleware.gzip import GZipMiddleware
from starlette.staticfiles import StaticFiles

app = Starlette(debug=False, template_directory='./templates')
app.add_middleware(GZipMiddleware, minimum_size=500)
app.mount('/static', StaticFiles(directory='./media'), name='static')

PLACES_API = os.environ.get('PLACES_API', None)
