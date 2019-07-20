from django import forms

class todo(forms.Form):
    text = forms.CharField(max_length=20,
    widget=forms.TextInput(attrs={
        'id': 'form-control',
        'placeholder': 'A django Todo',
        'required': True
    }))

