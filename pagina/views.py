from django.shortcuts import render

def vLandingpage(request):
    return render(request, 'landingpage.html')
