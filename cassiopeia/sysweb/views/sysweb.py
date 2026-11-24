from syscor.views.database import ModelDatabases
from syscor.views.auth import SysAuthNoPermission
from django.shortcuts import render
from django.views import View

#
# class WebMainView(SysAuthNoPermission, ModelDatabaseGet):
#
class CassiopeiaView(View):
    def get(self, request):
        # permission_required = "sysweb.view_sysweb"
        view_attributes = {"application": "sysweb", "model": "Cassiopeia", "template_name": "cassiopeia.html"}
        web_page_attributes = {}
        web_data = {}
        return render (request, view_attributes['template_name']
                      , {"web_page_attributes": web_page_attributes, "web_data": web_data})

class WebMainView(View):
    def get(self, request):
        # permission_required = "sysweb.view_sysweb"
        view_attributes = {"application": "sysweb", "model": "WebMain", "template_name": "webmain.html"}
        web_page_attributes = {}
        web_data = {}
        return render (request, view_attributes['template_name']
                      , {"web_page_attributes": web_page_attributes, "web_data": web_data})