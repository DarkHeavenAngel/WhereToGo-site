from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('place.list', views.place_list, name="place_list"), #'' - люба назва для шляху, потім ми пишемо функцію для стор. і придум любу назву
    path('place.list/<int:index>', views.place_detailed, name="place_detailed"),
    path('add_place.list', views.add_place_list, name="add_place_list"),
    path("random/", views.random_place, name="random_place"),
]