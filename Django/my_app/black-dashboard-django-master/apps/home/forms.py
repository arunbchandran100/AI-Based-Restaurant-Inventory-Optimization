# my_app/home/forms.py

from django import forms

class FoodItemForm(forms.Form):
    # Define your form fields here
    name = forms.CharField(label='Food Item Name', max_length=100)
    # Add other fields as needed
