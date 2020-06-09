from django.shortcuts import render
from student.forms import StudentForm
from student.models import Student

# Create your views here.

def emp(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StudentForm()
    return render(request,'index.html',{'form':form})
def show(request):
    students = Student.objects.all()
    return render(request,"show.html",{'students':students})
def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request,'edit.html', {'student':student})  
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
