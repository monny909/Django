# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField




class Institution(models.Model):
     name = models.CharField(max_length=256,blank=True,null=True)
     bio = models.CharField(max_length=256,blank=True,null=True)

     def __unicode__(self):
         return self.name
     def __str__(self):
         return self.name
     def get_absolute_url(self):
         return "/my-school/"



class Report(models.Model):

    title            =  models.CharField(max_length=120)
    uploaded_file1   =  models.FileField(null=True,blank=True)
    uploaded_file2   =  models.FileField(null=True,blank=True)
    uploaded_file3   =  models.FileField(null=True,blank=True)
    timestamp        =  models.DateTimeField(auto_now_add=True, blank=True)
    username         =  models.ForeignKey(User)
    institution      =  models.ForeignKey(Institution, editable=False)
    description      =  RichTextField()


    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return "/user-reports/"

class Activity(models.Model):

    title            =  models.CharField(max_length=120)
    timestamp        =  models.DateTimeField(auto_now_add=True, blank=True)
    description      =  models.TextField(max_length=1500)

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return "/activity/"


class News(models.Model):

    title            =  models.CharField(max_length=120)
    thumbnail        =  models.FileField(null=True,blank=True)
    timestamp        =  models.DateTimeField(auto_now_add=True, blank=True)
    username         =  models.ForeignKey(User)
    description      =  RichTextField()

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return "/news/"


class Cases(models.Model):

    title            =  models.CharField(max_length=120)
    uploaded_file1   =  models.FileField(null=True,blank=True)
    uploaded_file2   =  models.FileField(null=True,blank=True)
    uploaded_file3   =  models.FileField(null=True,blank=True)
    timestamp        =  models.DateTimeField(auto_now_add=True, blank=True)
    username         =  models.ForeignKey(User)
    description      =  RichTextField()

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return "/cases/"


class Profile(models.Model):

    user            =  models.OneToOneField(User, on_delete=models.CASCADE)
    bio             =  models.CharField(max_length=256,null=True,blank=True)
    institution     =  models.ForeignKey(Institution,null=True,blank=True)


    def __str__(self):
        return self.user.username
    def __unicode__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
