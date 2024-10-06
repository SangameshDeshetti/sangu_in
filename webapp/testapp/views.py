from django.shortcuts import render


# Create your views here.
def home_view(request):
    context = {
        "msg": "Welcome to sangu.in!"
    }
    return render(request, "testapp/home.html", context=context)
