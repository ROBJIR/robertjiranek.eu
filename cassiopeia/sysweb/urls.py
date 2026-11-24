from django.urls import path, include
from .views.sysweb import WebMainView

urlpatterns = [
    path ('',WebMainView.as_view(),name = 'home'),
]
