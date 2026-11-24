from django.urls import path, include
from .views.sysweb import WebMainView, CassiopeiaView

urlpatterns = [
    path('',WebMainView.as_view(), name = 'webhome'),
    path('cassiopeia', CassiopeiaView.as_view(), name = 'cassiopeia'),
]
