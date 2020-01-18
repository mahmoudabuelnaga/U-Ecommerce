from django.db.models import Q
from tags.models import Tag
from django.db import models
import random
import os
import datetime
from django.urls import reverse
from colorfield.fields import ColorField
# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename        = random.randint(1,98765467897654678656)
    date                = datetime.datetime.now()
    name, ext           = get_filename_ext(filename)
    finally_filename    = f'{new_filename}{ext}'
    return f"products/{date.year}/{date.month}/{date.day}/{new_filename}/{finally_filename}"

class ProductQuerySet(models.query.QuerySet):

    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)
    
    def search(self, query):
        lookups = (
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(price__lte=query) |
            Q(tag__title__icontains=query)
            )
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()
    
    def featured(self):
        return self.get_queryset().featured()
    
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
    
    def search(self, query):
        return self.get_queryset().active().search(query)
class Color(models.Model):
    color           = ColorField()

    def __str__(self):
        return self.color
    

class Product(models.Model):
    title           = models.CharField(max_length=120)
    description     = models.TextField()
    price           = models.DecimalField(max_digits=20, decimal_places=2, default=39.99)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    color           = models.ManyToManyField(Color, blank=True)
    tags            = models.ManyToManyField(Tag, blank=True)

    objects         = ProductManager()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('products:detail', args=[self.id])