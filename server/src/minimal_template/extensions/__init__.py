from fastapi.staticfiles import StaticFiles

from minimal_template.core.config import settings


def setup_rapidoc(app, override_default_doc=True):
    if override_default_doc:
        rapi_doc_url = "/docs"
        for index, route in enumerate(app.router.routes):
            if route.path == rapi_doc_url:
                app.router.routes.pop(index)
    else:
        rapi_doc_url = "/rapidocs"

    app.mount(rapi_doc_url, StaticFiles(directory=settings.RAPI_DOC_DIR, html=True), name="static")
