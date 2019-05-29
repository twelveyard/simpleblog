from django.http import HttpResponse

def first_page(request):
    return HttpResponse("<head>wondeful world<head/><p>世界好</p><tr1>wonderful,i,jk<tr1><tr2>name<tr2>")