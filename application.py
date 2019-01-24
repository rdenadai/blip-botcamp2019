import os
import requests
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
from starlette.responses import Response
import uvicorn
from config import app, PLACES_API
import googlemaps as gm
import wikipediaapi


@app.route('/')
async def index(request):
    template = app.get_template('index.html')
    content = template.render(request=request)
    return HTMLResponse(content)


@app.route('/places/', methods=['GET'])
async def place(request):
    # -23.600978, -46.684317
    error = False
    found_places = []
    lat, lng = -23.602610, -46.675336
    try:
        lat = float(request.query_params['lat'])
        lng = float(request.query_params['lng'])
        gmaps = gm.Client(key=PLACES_API)
        places = gmaps.places_nearby(location=(lat, lng), radius=500)
        print(list(places))
        # for place in places:
        #     print(place)
        #     print('-' * 20)
    except Exception as e:
        print(e)
        error = True

    return JSONResponse({
        'error': error,
        'places': found_places,
        'lat': lat,
        'lng': lng
    })


@app.route('/wiki/', methods=['GET'])
async def wiki(request):
    error = False
    title = ''
    description = ''
    try:
        search = str(request.query_params['search'])
        wk = wikipediaapi.Wikipedia('en')
        page = wk.page(search)
        title = page.title
        description = page.summary
    except Exception as e:
        print(e)
        error = True

    return JSONResponse({
        'error': error,
        'title': title,
        'description': description
    })
