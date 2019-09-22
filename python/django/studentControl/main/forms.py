from django import forms

from main.models import Student


class StudentSearching(forms.ModelForm):

    class Meta:
        fields = [
            'name',
            'surname',
        ]
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия'
        }
        widgets = {
            'name': forms.TextInput(),
            'surname': forms.TextInput(),
        }

        model = Student
