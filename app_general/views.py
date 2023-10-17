from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from app_general.forms import SubscriptionModelForm
from .models import Subscription

# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')

def about(request):
    return render(request, 'app_general/about.html')

def subscription(request):
    if request.method == 'POST':
        form = SubscriptionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('subscription_thank'))
    else:        
        form = SubscriptionModelForm()
    context = {'form': form}
    return render(request, 'app_general/subscription_form.html', context)

def subscription_thank(request):
    return render(request, 'app_general/subscription_thank.html')