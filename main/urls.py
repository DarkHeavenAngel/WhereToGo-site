from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('place.list', views.place_list), #'' - люба назва для шляху, потім ми пишемо функцію для стор. і придум любу назву
    path('add_place.list', views.add_place_list),
]