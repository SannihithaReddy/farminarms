from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('det/',views.det,name="det"),
    path('suggest/',views.suggest,name="suggest"),
    path('rice/',views.rice,name="rice"),
    path('dispcrop/',views.dispcrop,name="Display Crop"),
    path('dispwea/',views.dispwea,name="Display Weather"),
    path('maize/',views.maize,name="maize"),
    path('scane/',views.scane,name="Sugar Cane"),
    path('bgram/',views.bgram,name="Bengal gram"),
    path('gnut/',views.gnut,name="Ground nut"),
    path('chilli/',views.chilli,name="Chilli"),
    path('cotton/',views.cotton,name="Cotton"),
    path('sbean/',views.sbean,name="Soya bean"),
    path('mgmt/',views.mgmt,name="Crop Management")

]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)