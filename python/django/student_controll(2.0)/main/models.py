from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    sex_list = (
        ('MALE', "MALE"),
        ('FEMALE', 'FEMALE')
    )
    subject_list = (
        ('ВМ', 'Высшая Математика'),
        ('Физ', 'Физика'),
        ('ОСТ', 'Основы схемотехники'),
        ('УФМ', 'УФМ'),
        ('Про', 'Программирование'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey('main.Groups', on_delete=models.CASCADE, blank=True,null=True, default=None)
    age = models.IntegerField(default=None, null=True, blank=True)
    sex = models.CharField(max_length=255, choices=sex_list, default=None, null=True, blank=True)
    subjects = models.ManyToManyField('main.Subjects', blank=True,)

    def __str__(self):
        return self.user.first_name+" "+self.group.name_of_group+"-"+self.group.suffix


class Groups(models.Model):
    name_of_group = models.CharField(max_length=255, default=None, null=True, blank=True)
    suffix = models.CharField(max_length=255, default=None, null=True, blank=True)
    faculty = models.ForeignKey('main.Faculty', on_delete=models.CASCADE, blank=True, null=True, default=None)
    subject = models.ManyToManyField('main.Subjects', blank=True,)

    def __str__(self):
        return self.name_of_group+"-"+self.suffix


class Faculty(models.Model):
    short_name = models.CharField(max_length=255, default=None, null=True, blank=True)
    full_name = models.CharField(max_length=255, default=None, null=True, blank=True)

    def __str__(self):
        return self.short_name


class Subjects(models.Model):
    full_name = models.CharField(max_length=255, default=None, null=True, blank=True)
    short_name = models.CharField(max_length=255, default=None, null=True, blank=True)

    def __str__(self):
        return self.short_name


class Progress(models.Model):
    name_of_subject = models.CharField(max_length=255, default=None, null=True, blank=True)
    group = models.CharField(max_length=255, default=None, null=True, blank=True)
    name_of_student = models.CharField(max_length=255, default=None, null=True, blank=True)
    points = models.IntegerField(default=None, null=True, blank=True)
    redacted_data = models.DateField(auto_now_add=True)
    redacted_by = models.CharField(max_length=255, default=None, null=True, blank=True)

    def __str__(self):
        return self.name_of_student+" "+self.name_of_subject+" "+self.redacted_data


class Departament(models.Model):
    name_of_the_departament = models.CharField(max_length=255, default=None, null=True, blank=True)

    def __str__(self):
        return self.name_of_the_departament


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_by_father = models.CharField(max_length=255, default=None, null=True, blank=True)
    subject = models.CharField(max_length=255, default=None, null=True, blank=True)
    faculty = models.ManyToManyField(Faculty, default=None, blank=True)
    group = models.ManyToManyField(Groups, default=None, blank=True)
    departament = models.ManyToManyField(Departament, blank=True)

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name
