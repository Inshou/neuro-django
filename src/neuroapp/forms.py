from django import forms
from .models import TestImage


class UserForm(forms.ModelForm):
    class Meta:
        model = TestImage
        #fields = '__all__'
        fields = ('image', )
        widgets = {
            'image': forms.FileInput(attrs={'class': 'input-image'})
        }
    # image = forms.ImageField()


class ResultForm(forms.Form):
    CHOICES = (('thumb_up', 'thumb_up',), ('ok', 'ok',))
    answer = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, label="")
