from django.shortcuts import render,redirect,get_object_or_404
from main.models import Students

# Create your views here.

def index(request):
    all_student = Students.objects.all()
    return render(request, 'index.html',{'all_student':all_student})

def detail(request,student_id):
    student = get_object_or_404 (Students,pk=student_id)

    return render(request,'detail.html',{'student':student})

def update(request,student_id):
    edit = get_object_or_404 (Students,pk=student_id) 

    if request.method == 'POST':
       
        
        edit.name = request.POST['name']
        edit.major = request.POST['major']
        edit.number = request.POST['number']
        edit.year = request.POST['year']
        edit.level = request.POST['level']
        edit.average = request.POST['average']

        edit.save()

        return redirect('detail',student_id)
    else:
        return render(request,'update.html',{'edit':edit})

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

        return redirect('detail', edit.id)

    return render(request,'create.html')

def delete(request,student_id):
    deletepost=get_object_or_404 (Students,pk=student_id)
    deletepost.delete()

    return redirect('index')