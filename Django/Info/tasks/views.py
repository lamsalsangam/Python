# django also has the ability ti create the form which is much easier
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# tasks = ["foo", "bar", "space", "taker"]
# tasks = []

class NewTaskForm(forms.Form):
    task =forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    # making the empty taks for the every new user
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request, "tasks/index.html",{
        # "tasks": tasks
        # python manage.py migrate will allow us to create all of the default tables inside the django database
        "tasks": request.session["tasks"]
    })

def add(request):
    # serverside validation
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # tasks.append(task)
            request.session["tasks"] += [task]
            # redirecting
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })