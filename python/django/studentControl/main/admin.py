from django.contrib import admin

from main.models import Group, Student


def reg(data):
    admin.site.register(data)


reg(Group)
reg(Student)
# Register your models here.
