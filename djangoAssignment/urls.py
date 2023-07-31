from django.urls import path
from .views import placeView

urlpatterns = [
    path('places/', placeView.as_view(), name='places'),
]