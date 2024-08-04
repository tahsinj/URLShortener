from django.shortcuts import render
from .models import ShortURL
from .forms import NewShortURL
from datetime import datetime
import random, string

# Create your views here.
def home(request):
    return render(request, 'home.html')

def generate(request):
    if request.method == 'POST':
        form = NewShortURL(request.POST)
        if form.is_valid():
            original_site = form.cleaned_data['original_url']
            random_chars_list = list(string.ascii_letters)
            random_chars=''
            for i in range(6):
                random_chars += random.choice(random_chars_list)
            while len(ShortURL.objects.filter(short_url=random_chars)) != 0:
                for i in range(6):
                    random_chars += random.choice(random_chars_list)
            d = datetime.now()
            s = ShortURL(original_url=original_site, short_url=random_chars, time_date_created=d)
            s.save()
            return render(request, 'urlgenerated.html', {'chars':random_chars})
    else:
        form=NewShortURL()
        context={'form': form}
        return render(request, 'generateurl.html', context)

def redirect(request, url):
    obj = ShortURL.objects.filter(short_url=url)
    if len(obj) == 0:
        return render(request, 'pagenotfound.html')
    context = {'obj':obj[0]}
    return render(request, 'redirect.html', context)