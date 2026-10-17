from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee
from .forms import EmpForm
# Create your views here.

def addEmployee(request):
    form=EmpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dash')
    return render(request,'AddEmp.html',{'form':form})

def ViewEmp(request):
    emp=Employee.objects.all()
    return render(request,'Dashboard.html',{'emp':emp})

def EditEmp(request,id):
    emp=get_object_or_404(Employee,id=id)
    form=EmpForm(request.POST or None,instance=emp)
    if form.is_valid():
        form.save()
        return redirect('dash')
    return render(request,'EditEmployee.html',{'form':form})

def DeleteEmp(request,id):
    emp=get_object_or_404(Employee,id=id)
    if request.method=="POST":
        emp.delete()
        return redirect('dash')
    return render(request,'DeleteEmp.html')

def Dashboard(request):
    emp=Employee.objects.all()
    empcount=Employee.objects.count()
    
    search=request.GET.get('search')
    if search:
        emp=emp.filter(name__icontains=search)
    
        
    context={
        'emp':emp,
        'empcount':empcount
    }
    
    return render(request,'Dashboard.html',context)