from django.shortcuts import render  # Make sure to import render

def home(request):
    return render(request, 'index.html')  # Render the 'index.html' template
