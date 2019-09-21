from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255, default=None, blank=True)
    surname = models.CharField(max_length=255,default=None, blank=True)
    group = models.ForeignKey('main.Group', on_delete=models.CASCADE)
    age = models.IntegerField(default=None)

    def __str__(self):
        return self.name+' '+self.surname


class Group(models.Model):
    name = models.CharField(max_length=255, default=None, blank=True)
    suffix = models.CharField(max_length=255,default=None, blank=True)

    def __str__(self):
        return self.name+"-"+self.suffix
