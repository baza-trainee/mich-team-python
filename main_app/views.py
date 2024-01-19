from django.shortcuts import render

# Create your views here.
def home(request):
    """
        View for rendering the home page.

        This view renders the 'home.html' template.
    """
    return render(request, 'home.html')