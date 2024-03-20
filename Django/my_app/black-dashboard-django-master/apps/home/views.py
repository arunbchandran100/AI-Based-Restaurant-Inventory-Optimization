
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.template.loader import get_template
from .models import FoodItem

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


# views.py
from django.shortcuts import render, redirect
from .models import FoodItem, RawMaterial

def create_food_item(request):
  if request.method == 'POST':
    print("entered the fucn")
      
    food_item_name = request.POST.get('name')
    food_item = FoodItem.objects.create(name=food_item_name)

    # Access raw material data as lists of values submitted together
    raw_material_names = request.POST.getlist('raw_material_name[]')
    quantities = request.POST.getlist('quantity[]')
    quantity_types = request.POST.getlist('quantity_type[]')

    print("Raw Material Names:", raw_material_names)
    print("Quantities:", quantities)
    print("Quantity Types:", quantity_types)


    # Create RawMaterial objects for each entry in the lists
    for name, quantity, quantity_type in zip(raw_material_names, quantities, quantity_types):
      # Check if quantity is a valid number before creating the object
      try:
        quantity = float(quantity)  # Convert to a number (e.g., for calculations)
      except ValueError:
        quantity = None  # Handle invalid quantity input (optional)

      RawMaterial.objects.create(
          food_item=food_item,
          name=name,
          quantity=quantity,
          quantity_type=quantity_type
      )

    return render(request, 'home/raw_materials.html')  # Redirect to a success page after saving

  return render(request, 'home/raw_materials.html')


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