from django.shortcuts import render,get_object_or_404, redirect
from .models import Students

# Create your views here.

def index(request):
    all_student = Students.objects.all()
    return render(request, 'index.html',{'all_student':all_student})

def detail(request,student_id):
    student = get_object_or_404 (Students,pk=student_id) 
    return render(request,'detail.html',{'student':student})

def update(request,student_id):
    student = get_object_or_404 (Students,pk=student_id) 

    if request.method == 'POST':
        edit = Students()
        
        edit.name = request.POST['name']
        edit.major = request.POST['major']
        edit.number = request.POST['number']
        edit.year = request.POST['year']
        edit.level = request.POST['level']
        edit.average = request.POST['average']

        edit.save()

        return redirect('/detail/'+str(student_id))
    else:
        return render(request,'update.html',{'student':student})

def create(request):
    if request.method == 'POST':
        edit = Students()

        edit.name = request.POST['name']
        edit.major = request.POST['major']
        edit.number = request.POST['number']
        edit.year = request.POST['year']
        edit.level = request.POST['level']
        edit.average = request.POST['average']

        edit.save()

        return redirect('/detail/'+str(student_id))

def delete(request,student_id):
    deletepost=get_object_or_404 (Students,pk=student_id)
    deletepost.delete()
    return redirect('index')