import os
import requests
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
from starlette.responses import Response
import uvicorn
from config import app


@app.route('/')
async def index(request):
    template = app.get_template('index.html')
    content = template.render(request=request)
    return HTMLResponse(content)


@app.route('/places/', methods=['GET'])
async def place(request):
    # -23.600978, -46.684317
    error = False
    lat, lng = -23.602610, -46.675336
    try:
        lat = float(request.query_params['lat'])
        lng = float(request.query_params['lng'])
    except:
        error = True

    return JSONResponse({
        'error': error,
        'lat': lat,
        'lng': lng
    })
