from django.db import models

import datetime
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=200)
    displayed_name = models.CharField(max_length=200)
    comment = models.TextField()
    def __unicode__(self):
        return self.name + " : " + self.comment

class Event(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publication')
    category = models.ForeignKey(Category)
    img_link = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="imgArticles/")
    def __unicode__(self):
        return self.name

class GoodSite(models.Model):
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name + " : " + self.comment

def get_latest_events():
    """ Returns the last published events."""
    return Event.objects.filter(pub_date__lte=timezone.now()).filter(article__is_beta=False).order_by('-pub_date')[:4]

def get_events_by_category(category):
    returned_events = []
    for e in Event.objects.all():
        if e.category == category and e.pub_date < timezone.now():
            returned_events.append(e)
    return returned_events

def get_good_sites():
    """Returns the good sites list."""
    return GoodSite.objects.all()

def get_category_by_name(category_name):
    for c in Category.objects.all():
        if c.name == category_name:
            return c
