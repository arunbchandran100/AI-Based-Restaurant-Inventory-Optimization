
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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from django.http import JsonResponse
from .models import FoodItem, RawMaterial

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

def create_food_item(request):
  if request.method == 'POST':
      
    food_item_name = request.POST.get('name')
    food_item = FoodItem.objects.create(name=food_item_name)

    # Access raw material data as lists of values submitted together
    raw_material_names = request.POST.getlist('raw_material_name[]')
    quantities = request.POST.getlist('quantity[]')
    quantity_types = request.POST.getlist('quantity_type[]')

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

def ml_req(request):
    print("Yes---------")
    if request.method == 'GET':
        # Update user profile information
        Day = request.GET.get('day')
        Month = request.GET.get('month')
        Year = request.GET.get('year')
        Temperature = request.GET.get('temperature')
        Precipitation = request.GET.get('precipitation')
        SpecialOccasion = request.GET.get('specialOccasion')

        print('Day')
        print(Day)
        print('Month')
        print(Month)
        print('Year')
        print(Year)
        print('Temperature')
        print(Temperature)
        print('Precipitation')
        print(Precipitation)
        print('SpecialOccasion')
        print(SpecialOccasion)
        
        # Load the dataset
        # Make sure to upload the '12to22.csv' file in your environment
        file_path = os.path.join(settings.BASE_DIR, '12to22.csv')
        dataset = pd.read_csv(file_path)

        # Split the dataset into features (X) and target variable (y)
        X = dataset.drop(columns=['Qty'])  # Features
        y = dataset['Qty']  # Target variable

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=60)

        # Initialize the Random Forest Regressor
        rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

        # Train the model
        rf_regressor.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = rf_regressor.predict(X_test)
        """
        # Calculate Mean Absolute Error and R^2 Score
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print("Mean Absolute Error:", mae)
        print("R^2 Score:", r2)"""


        # Example new data input including Day, Month, and Year
        new_data = pd.DataFrame({
            'Day': [Day],  # Example Day
            'Month': [Month],  # Example Month
            'Year': [Year],  # Example Year
            'Temperature': [Temperature],
            'Precipitation': [Precipitation],
            'Special Occasion': [SpecialOccasion]
        }, index=[0])

        predicted_quantity = rf_regressor.predict(new_data)
        print("Predicted Quantity:", predicted_quantity[0])
        
        data = {'success' : True, 'value' : predicted_quantity[0]}
        return JsonResponse(data, safe=False)

    data = {'success' : False}
    return JsonResponse(data, safe=False)
    

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

    except TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
 
    
    
    
from django.shortcuts import render, redirect
from django.conf import settings
import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from django.core.files.storage import FileSystemStorage

"""
def upload_dataset(request):
    print("Working")
    if request.method == 'POST' :
        #dataset_file = request.FILES['dataset_file']
        dataset = pd.read_csv('12to22.csv')
        #fs = FileSystemStorage()
        ##file_path = fs.path(filename)

        #dataset = pd.read_csv(file_path)
        X = dataset.drop(columns=['Qty'])
        y = dataset['Qty']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=60)
        
        rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
        rf_regressor.fit(X_train, y_train)
        predicted_quantity = rf_regressor.predict(X_test)  # Predict on test data

        # Clean up uploaded file
        #fs.delete(filename)
        
        print(predicted_quantity)
        
        print("Working")
        return render(request, 'home/tables.html')
    
    return render(request, 'home/tables.html')"""


from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from django.views.decorators.http import require_POST


 # Disable CSRF token for this view, use cautiously.
@require_POST
def upload_dataset(request):
    if 'dataset_file' not in request.FILES:
        return JsonResponse({"success": False, "message": "No file was uploaded."}, status=400)

    file = request.FILES['dataset_file']
    try:
        # Assuming the file is a CSV for demonstration
        df = pd.read_csv(file)
        # Perform any necessary processing here
        # For demonstration, let's just print the dataframe head
        print(df.head())
        return JsonResponse({"success": True, "message": "File uploaded and processed successfully."})
    except Exception as e:
        return JsonResponse({"success": False, "message": "Error processing the file: " + str(e)}, status=600)
    return redirect('home') 