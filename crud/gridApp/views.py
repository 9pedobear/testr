from django.shortcuts import render, redirect
from .models import Employes
from .forms import EmployerForm

# Create your views here.
def index(request):
    emplyers = Employes.objects.all()
    return render(
        request,
        'gridApp/show.html',
        {'sex': emplyers}
    )

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
        context = {
            'fuck' : form
        }
    return render(
        request,
        'gridApp/index.html',
        context=context
    )

def edit(request, id):
    employer = Employes.objects.get(id=id)
    return render(
        request,
        'gridApp/edit.html',
        {'employer' : employer}
    )

def update(request, id):
    employer = Employes.objects.get(id=id)
    form = EmployerForm(request.POST, instance=employer)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(
        request,
        'gridApp/edit.html',
        {'employer' : employer}
    )

def delete(request, id):
    employer = Employes.objects.get(id=id)
    employer.delete()
    return redirect('/')
