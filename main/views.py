from django.shortcuts import render, redirect
from main.forms import PlaceForm
from datetime import datetime
import random

def index(request):
    return render(request, 'main/index.html')



def place_list(request):
    places = request.session.get('places', [])
    return render(request, 'main/place_list.html', {'places': places})

def place_detailed(request, index):
    places = request.session.get('places', [])
    if not places or not(0 <= index < len(places)):
        return redirect('place_list')

    place = places[index]
    return render(request, 'main/place_detailed.html', {'place': place})



def add_place_list(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            places = request.session.get('places', [])
            place_data = form.cleaned_data.copy()
            place_data['created_at'] = datetime.now().strftime('%d-%m-%Y %H:%M') #НЕ ЗАБУТИ https://acode.com.ua/method-strftime-python/
            places.append(place_data)
            request.session['places'] = places
            return redirect('place_list')
    else:
        form = PlaceForm()

    return render(request, 'main/add_list.html', {'form': form})




def random_place(request):
    places = request.session.get('places', [])
    if not places:
        return render(request, 'main/place_list.html', {'places': None})

    weighted_places = []
    for place in places:
        rating = int(place.get('rating', 1))
        weighted_places.extend([place] * rating)

    chosen_place = random.choice(weighted_places)
    return render(request, 'main/random_place.html', {'place': chosen_place})

