from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from west.models import Character

def index(request):
    return HttpResponse("i like west foods.")

#def staff(request):
    staff_list = Character.objects.all()
    staff_str  = map(str, staff_list)
    return HttpResponse("<p>" + ' '.join(staff_str) + "</p>")

#from django.http import HttpResponse
from django.shortcuts import render

def templay(request):
    context          = {}
    context['label'] = 'Hello World!'
    return render(request, 'west/templay.html', context)

def staff(request):
    staff_list  = Character.objects.all()
    staff_str  = map(str, staff_list)
    context   = {'label': ' '.join(staff_str)}
    return render(request, 'west/templay.html', context)

from django.shortcuts import render

def form(request):
    return render(request, 'west/form.html')

from django.shortcuts import render

def investigate(request):
    rlt = request.GET['staff']
    return HttpResponse(rlt)
