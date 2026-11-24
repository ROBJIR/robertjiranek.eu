from django.apps import apps
from .web import WebMainRender

class ModelDatabases(WebMainRender):
    def model_data_get(self):
        model = apps.get_model(
                        self.view_attributes["application"],
                        self.view_attributes["model"],
        )
        template_name = f"{model._meta.model_name}.html"
        records = list(model._default_manager.order_by("pk"))
        self.view_attributes["template_name"] = template_name

        web_data = {}
        web_data["records"] = records
        web_data["records_num_rows"] = len(records)
        return self.view_attributes, web_data