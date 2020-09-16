from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import StudentForm
from .models import Student

# Create your views here.

def index(request):
    words = 'hello world!'
    students = Student.get_all()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            form = StudentForm()

        context = {
            'students': students,
            'form': form,
        }
        return render(request, 'index.html', context=context)

