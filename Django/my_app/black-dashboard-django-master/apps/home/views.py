
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.template.loader import get_template
from .models import FoodItem
from django.template import TemplateDoesNotExist

template = get_template('home/user.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def user_profile(request):
    user = request.user
    
    if request.method == 'POST':
        # Update user profile information
        user.username = request.POST.get('username', user.username)
        user.email = request.POST.get('email', user.email)
        user.first_name = request.POST.get('full_name', user.first_name)
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return render(request, 'home/user.html')
    
    return render(request, 'home/user.html')


from django.http import JsonResponse
from .models import FoodItem, RawMaterial


from django import forms

class FoodItemForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    raw_material_name = forms.CharField(max_length=100, required=True)
    quantity = forms.FloatField(required=True)


from .forms import FoodItemForm

def create_food_item(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            food_item_name = form.cleaned_data['name']
            raw_material_name = form.cleaned_data['raw_material_name']
            quantity = form.cleaned_data['quantity']
            
            # Save data to the database
            FoodItem.objects.create(name=food_item_name)
            RawMaterial.objects.create(name=raw_material_name, quantity=quantity)
            
            # Redirect or render a success page
            return render(request, 'success.html')
    else:
        form = FoodItemForm()
    
    return render(request, 'home/raw_materials.html', {'form': form})




def fetch_food_items(request):
    food_items = FoodItem.objects.all()
    data = [{'name': food_item.name, 'raw_materials': [{'name': rm.name, 'quantity': rm.quantity, 'quantity_type': rm.quantity_type} for rm in food_item.rawmaterial_set.all()]} for food_item in food_items]
    return JsonResponse(data, safe=False)


def get_food_items():
    # Fetch food items from the database
    food_items = FoodItem.objects.all()
    return food_items

def render_page(request):
    # Fetch food items from the database
    food_items = FoodItem.objects.all()

    # Process any other data or perform any other operations here

    # Create a context dictionary with the data to pass to the template
    context = {
        'food_items': food_items,
        # Add any other data you want to pass to the template here
    }

    # Render the template with the provided context
    return render(request, 'path_to_your_template.html', context)




@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))