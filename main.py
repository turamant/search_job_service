import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from apis.general_pages.route_homepage import general_pages_router
from core.config import settings


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.include_router(general_pages_router)
    app.mount("/static", StaticFiles(directory="static"), name="static")
    return app


app = start_application()

'''
@app.get('/')
def index():
    return {'hello': 'hellooo world!'}
'''

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, debug=True, reload=True)

