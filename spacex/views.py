import requests
from django.shortcuts import render
from django.core.paginator import Paginator

def spacex_launches(request):
    # Make the GET request to the SpaceX API
    response = requests.get('https://api.spacexdata.com/v4/launches')
    
    # Check if the request was successful
    if response.status_code == 200:
        launches = response.json()  # Parse the JSON response
    else:
        launches = []

    # Paginate the launches
    paginator = Paginator(launches, 5)  # Show 10 launches per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'spacex/launches.html', {'page_obj': page_obj})
