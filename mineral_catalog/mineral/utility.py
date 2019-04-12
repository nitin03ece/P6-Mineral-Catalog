from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Mineral
from django.db import IntegrityError

import json
import random
from django.db import models
from collections import Counter

class Utility:
    def readFromJSON(self):
        with open('minerals.json', encoding='UTF-8') as file:
            minerals = json.loads(file.read())

        for mineral in minerals:
            try:
                Mineral(
                    name = mineral.get("name", ""),
                    image_filename = mineral.get("image filename", ""),
                    image_caption = mineral.get("image caption", ""),
                    category = mineral.get("category", ""),
                    formula = mineral.get("formula", ""),
                    strunz_classification = mineral.get("strunz classification", ""),
                    color = mineral.get("color", ""),
                    crystal_system = mineral.get("crystal system", ""),
                    unit_cell = mineral.get("unit cell", ""),
                    crystal_symmetry = mineral.get("crystal symmetry", ""),
                    cleavage = mineral.get("cleavage", ""),
                    mohs_scale_hardness = mineral.get("mohs scale hardness", ""),
                    luster = mineral.get("luster", ""),
                    streak = mineral.get("streak", ""),
                    diaphaneity = mineral.get("diaphaneity", ""),
                    optical_properties = mineral.get("optical properties", ""),
                    refractive_index = mineral.get("refractive index", ""),
                    crystal_habit = mineral.get("crystal habit", ""),
                    specific_gravity = mineral.get("specific gravity", ""),
                    group = mineral.get("group", "")
                ).save()
            except IntegrityError:
                pass


    def deleteDatabase(self):
        querry = Mineral.objects.all()
        for record in querry:
            record.delete()


    def changeImageFileName(self):
        minerals = Mineral.objects.all()
        for mineral in minerals:
            file_name = str(mineral.name) + ".jpg"
            mineral.image_filename = file_name
            mineral.save()


    def commonDetails(self):
        with open('minerals.json', encoding='UTF-8') as file:
            minerals = json.loads(file.read())
        keys = []
        for mineral in minerals:
            keys += mineral.keys()

        cnt = Counter()
        for key in keys:
            cnt[key] += 1
        
        return list(cnt.keys())


    def convertToDict(self, mineral):
        dictMineral = {}
        keys = self.commonDetails()
        for key in keys:
            if getattr(mineral, key, ''):
                try:
                    dictMineral[key] = mineral.__getattribute__(key)
                except AttributeError:
                    pass
        return dictMineral
