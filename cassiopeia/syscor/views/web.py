from django.shortcuts import render
from django.views import View

class WebMainRender(View):
    def get(self, request):

        view_attributes, web_data = self.model_data_get()

        web_page_attributes = {}
        web_page_attributes["application_code"] = ""
        web_page_attributes["application_name"] = web_page_attributes["application_code"]
        web_page_attributes["module_code"] = ""
        web_page_attributes["module_name"] = web_page_attributes["module_code"].lower()
        web_page_attributes["application_module_start"] = web_page_attributes["module_code"]
        web_page_attributes["module_file_template"] = web_page_attributes["module_code"]
        return render(request, view_attributes['template_name']
                      , {"web_page_attributes":web_page_attributes,"web_data": web_data })
