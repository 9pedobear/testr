from django.shortcuts import render, redirect
from gridApp.forms import EmployerForm
from gridApp.models import Employes

# Create your views here.

def addnew(request):
    if request.method == "POST":
        form = EmployerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = EmployerForm()
    return render(request,'gridApp/index.html',{'form':form})
def index(request):
    employees = Employes.objects.all()
    return render(request,"gridApp/show.html",{'employees':employees})
def edit(request, id):
    employee = Employes.objects.get(id=id)
    return render(request,'gridApp/edit.html', {'employee':employee})
def update(request, id):
    employee = Employes.objects.get(id=id)
    form = EmployerForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'gridApp/edit.html', {'employee': employee})
def delete(request, id):
    employee = Employes.objects.get(id=id)
    employee.delete()
    return redirect("/")
