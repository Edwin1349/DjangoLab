from django.shortcuts import render
from django.http import HttpResponse
from theater.models import *
from django.core import serializers
from django.http import Http404, JsonResponse
from itertools import chain
import json
import itertools as it
from operator import itemgetter
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,'index.html')

def search(request):
    return render(request,'Search.html')

@csrf_exempt
def getEvents(request):
    result = list()
    if request.method == "GET":
        seances = Seance.objects.all().order_by('date')   
    else:
        seances = Seance.objects.filter(repertoireid_id__performance_name__icontains = request.POST.get("cmp","").replace("і","i")).order_by('date') 
  
    count = int(0)
    for i in seances:
        seances = model_to_dict(i)
        halls = model_to_dict(i.hallid)
        performances = model_to_dict(i.repertoireid)

        dic = {}
        for key in (seances.keys() | halls.keys() | performances.keys()):
            if key in seances: dic.setdefault(key, []).append(seances[key])
            if key in halls: dic.setdefault(key, []).append(halls[key])
            if key in performances: dic.setdefault(key, []).append(performances[key])
        
        result.append(dic)
    

    return JsonResponse(result, safe=False)

def info(request,seance_id):
    performance=Seance.objects.get(id_seance=seance_id).repertoireid
    return render(request,"Info.html",{'performance': performance})
   
def tickets(request):
    return render(request,'Tickets.html')