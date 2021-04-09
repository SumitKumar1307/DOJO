from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def welcome(response):
    if response.method == "POST":
        print("GOTCHA")
        return HttpResponseRedirect('/register/')
    return render(response, 'welcome/example.html', {})
