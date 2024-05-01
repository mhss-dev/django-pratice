from django import forms
from .models import myCourses


class formulaireCourses(forms.ModelForm):
    class Meta:
        model=myCourses
        fields=['cours', 'formateur', 'email', 'heures']