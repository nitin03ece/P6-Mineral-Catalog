from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Mineral
from django.db import IntegrityError
from django.db import models
from mineral.utility import Utility

import json
import random


def mineralsList(request):
    minerals = Mineral.objects.all()
    return render(request, "mineral/minerals_list.html", {"minerals" : minerals})


def mineralDetail(request, name):
    mineral = get_object_or_404(Mineral, name=name)
    return render(request, "mineral/mineral_detail.html", {"mineral" : mineral})


def randomMineral(request):
    minerals = Mineral.objects.all()
    mineral = random.choice(minerals)
    return render(request, "mineral/random_mineral.html", {"mineral" : mineral})
