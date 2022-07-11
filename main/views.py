from django.shortcuts import render,HttpResponseRedirect
from main.forms import StudentForm
from main.models import Student


# Create your views here.
def addshow(request):
    if request.method=="POST":
        fm=StudentForm(data=request.POST)
        if fm.is_valid():
            fm.save() 
    fm=StudentForm()
    students=Student.objects.all()
    context={'fm':fm,'students':students}
    return render(request,'main/addshow.html',context)

def delete1(request,id):
    stu=Student.objects.get(id=id).delete()
    return HttpResponseRedirect('/')

def update1(request,id):
    if request.method=="POST":
        stu=Student.objects.get(id=id)
        fm=StudentForm(request.POST,instance=stu)
        if fm.is_valid():
            fm.save()
    else:
        stu=Student.objects.get(id=id)
        fm=fm=StudentForm(instance=stu)
    context={'fm':fm}
    return render(request,'main/update.html',context)



