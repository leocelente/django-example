from django.shortcuts import render

# Create your views here.
def index_page(request):
    data = { "i" : 1}
    return render(request, "my_application/home.html", data)

def slide_page(request, **kwargs):
    gambiarra = [ "https://imgur.com/GiA65YF", "https://imgur.com/5BqsYrq", "https://imgur.com/ymb6hvT", "https://imgur.com/2AasabR"]
    i = kwargs["slide_id"] % len(gambiarra)
    data = { "i": i, "next": i+1, "prev": i-1,  "url": gambiarra[i]}
    return render(request, "my_application/slide.html", data)
