from django.db import models


# Create your models here.

class Mineral(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=True)
    image_filename = models.ImageField(upload_to='img', blank=True)
    image_caption = models.TextField(blank=True)
    category = models.CharField(max_length=255, blank=True)
    formula = models.TextField(blank=True)
    strunz_classification = models.TextField(blank=True)
    color = models.CharField(max_length=255, blank=True)
    crystal_system = models.CharField(max_length=255, blank=True)
    unit_cell = models.TextField(blank=True)
    crystal_symmetry = models.TextField(blank=True)
    cleavage = models.TextField(blank=True)
    mohs_scale_hardness = models.TextField(blank=True)
    luster = models.TextField(blank=True)
    streak = models.CharField(max_length=255, blank=True)
    diaphaneity = models.CharField(max_length=255, blank=True)
    optical_properties = models.TextField(blank=True)
    refractive_index = models.TextField(blank=True)
    crystal_habit = models.TextField(blank=True)
    specific_gravity = models.TextField(blank=True)
    group = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return self.name
