from .models import uploadimg
from django import forms

choic=[('nature','nature'),('minimal','minimal'),('wall','wall')]

class uploadform(forms.ModelForm):
    class Meta:
        model=uploadimg
        fields=['name','catagory','pic']
        widgets={
            'catagory':forms.Select(choices=choic)

        }

