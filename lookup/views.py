from django.shortcuts import render
import datetime
import os

# Create your views here.

api_key = os.environ['DJWEATHER_API_KEY']

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get(
                f'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={zipcode}&date=2021-03-16&distance=25&API_KEY={api_key}')

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['AQI'] == -1:
            category_description = "There was an error getting this data. Try a different Zipcode?"
            category_color = "error"
        elif api[0]['Category']['Name'] == "Good":
            category_description = "(0-50) Enjoy your outdoor activities."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = '(51-100) If you are unusually sensitive to particle pollution, consider reducing your activity level or shorten the amount of time you are active outdoors.'
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101-150) Unhealthy for sensitive groups"
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151-200) Everyone may begin to experience health problems."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201-300) Stay inside."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301-500) Emergency conditions."
            category_color = "hazardous"

        return render(request, 'home.html', {
            'api': api,
            'category_description': category_description,
            'category_color': category_color})
    else:
        api_request = requests.get(
            f'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=63122&date=2021-03-16&distance=25&API_KEY={api_key}')

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        # if api[0]['AQI'] == -1:
        #     category_description = "There was an error getting this data. Try a different Zipcode?"
        #     category_color = "error"
        # elif api[0]['Category']['Name'] == "Good":
        #     category_description = "(0-50) Enjoy your outdoor activities."
        #     category_color = "good"
        # elif api[0]['Category']['Name'] == "Moderate":
        #     category_description = '(51-100) If you are unusually sensitive to particle pollution, consider reducing your activity level or shorten the amount of time you are active outdoors.'
        #     category_color = "moderate"
        # elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
        #     category_description = "(101-150) Unhealthy for sensitive groups"
        #     category_color = "usg"
        # elif api[0]['Category']['Name'] == "Unhealthy":
        #     category_description = "(151-200) Everyone may begin to experience health problems."
        #     category_color = "unhealthy"
        # elif api[0]['Category']['Name'] == "Very Unhealthy":
        #     category_description = "(201-300) Stay inside."
        #     category_color = "veryunhealthy"
        # elif api[0]['Category']['Name'] == "Hazardous":
        #     category_description = "(301-500) Emergency conditions."
        #     category_color = "hazardous"

        return render(request, 'home.html', {
            'api': api})






def about(request):
    return render(request, 'about.html', {})