from django.shortcuts import render
from .models import Student
import django.db

# Create your views here.
def index(request):
    if request.method == 'POST':
        rollno = request.POST.get('rollno')
        stud_name = request.POST.get('sname')
        address = request.POST.get('addr')
        stud_class = request.POST.get('cname')
        sl = Student(Rollno=rollno, Stud_Name=stud_name, Address=address, stud_class=stud_class)
        sl.save()
        return render(request,'./student/index.html')
    else:
        return render(request, './student/index.html')

def show(request):
    student = Student.objects.all()
    context = {'student_list': student}
    return render(request,'./student/show.html',context)