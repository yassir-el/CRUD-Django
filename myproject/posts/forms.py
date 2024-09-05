from django import forms
from .models import post
 

class GeeksForm(forms.ModelForm):
    class Meta:
        model = post
        fields = "__all__"