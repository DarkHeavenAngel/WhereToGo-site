from django import forms

class PlaceForm(forms.Form):
    name = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', max_length=100)
    type = forms.CharField(label='Type', max_length=100)
    location = forms.CharField(label='Location', max_length=100, required=False)
    rating = forms.IntegerField(label='Rating', min_value=1, max_value=5)
    photo = forms.ImageField(label='photo', required=False)
    creation_date = forms.DateTimeField(widget=forms.HiddenInput(), required=False)