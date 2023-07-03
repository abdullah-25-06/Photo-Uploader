from django.urls import path
from . import views
app_name='photos'

urlpatterns = [
    path('',views.gallery,name='gallery'),
    path('photo/<str:pk>',views.photos,name='photos'),
    path('add/',views.add,name='add'),
]
