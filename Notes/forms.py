from django import forms
from .models import Notes
class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        # this fields are used to create columns for these form
        fields = ['subject','topic','date','notes']