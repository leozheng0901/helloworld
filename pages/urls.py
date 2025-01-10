# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, results, homePost, leoPageView


urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('homePost/', homePost, name='homePost'),
    path('leo/', leoPageView, name='leo'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
]
