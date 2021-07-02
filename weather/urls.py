from django.urls import path
from . import views

urlpatterns=[
    path('det/',views.det,name="det"),
    path('suggest/',views.suggest,name="suggest"),
    path('rice/',views.rice,name="rice"),
    path('dispwea/',views.dispwea,name="Display Weather")
]