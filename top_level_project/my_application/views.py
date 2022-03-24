from django.shortcuts import render

# Create your views here.
def index_page(request):
    data = { "i" : 1}
    return render(request, "my_application/home.html", data)
