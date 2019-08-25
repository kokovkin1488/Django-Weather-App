from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


# Create your views here.
def index(request):
    appid = 'c503541f44151cfa3732c2000ad7e9b8'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    data = []
    for city in cities:
        # делаем запрос и формотируем из json в словарь
        response = requests.get(url.format(city.name)).json()
        city_info = {
            'city_name': city.name,
            'temp': response['main']['temp'],
            'icon': response['weather'][0]['icon']
        }
        data.append(city_info)

    context = {
        'data': data,
        'form': form
    }

    return render(request, 'weather/index.html', context=context)