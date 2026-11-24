from syscor.views.database import ModelDatabaseGet

class WebMainView(ModelDatabaseGet):
    permission_required = "meta.view_meta"
    view_attributes = {"model": "WebMain", "template": "webmain.html"}