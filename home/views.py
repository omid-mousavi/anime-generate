from django.shortcuts import render
import requests
# Create your views here.
def home(request):
  global result
  result = requests.get('https://nekos.best/api/v2/waifu').json()
  return render(request, 'index.html', {'res': result['results'][0]['url']})

def artist(request):
  return render(request, 'artist.html', {'sr': result['results'][0]['source_url'], 'nam': result['results'][0]['artist_name'], 'artist_ref': result['results'][0]['artist_href']})