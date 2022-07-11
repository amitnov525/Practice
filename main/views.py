from django.shortcuts import render

# Create your views here.
def addshow(request):
    return render(request,'main/addshow.html')

