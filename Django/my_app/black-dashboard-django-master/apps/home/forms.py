# my_app/home/forms.py

from django import forms
from .models import Document 

class FoodItemForm(forms.Form):
    # Define your form fields here
    name = forms.CharField(label='Food Item Name', max_length=100)
    # Add other fields as needed
    
    
from django import forms

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('uploaded_file', )

