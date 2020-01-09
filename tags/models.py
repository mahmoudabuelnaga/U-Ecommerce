from django.db import models
from product.models import Product
from django.utils.text import slugify

class Tag(models.Model):
    title       = models.CharField(max_length=30)
    slug        = models.SlugField(null=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    active      = models.BooleanField(default=True)
    products    = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Tag, self).save(*args,**kwargs)
    