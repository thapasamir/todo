from django.shortcuts import render, HttpResponseRedirect
from .models import task


def home(request):
    db_data = task.objects.all()  # getting all data of task object from database
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        z = task(work=title, description=desc)
        z.save()

    pi = {'res': db_data}
    return render(request, 'home.html', pi)


def delete(request, id):
    if request.method == "POST":
        print("working>>>>>>>>>>>>>>>>>")
        s = task.objects.get(pk=id)
        s.delete()
        return HttpResponseRedirect('/')
