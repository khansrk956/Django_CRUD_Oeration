from django.shortcuts import render,redirect
from . forms import EmployeeForm
from . models import Employee
# Create your views here.
def home(request):
    #variable name
    # get the html form from forms.py
    form1 =EmployeeForm()
    
    # data save into database.
    if request.method=="POST":
        f=EmployeeForm(request.POST)
        f.save()
        form1=EmployeeForm()
    # to fetch data from database use this line.
    getData = Employee.objects.all()
    data = {
        'form':form1,
        'getData':getData
    }
    return render(request,'index.html',data)


# delete data
def delete(request,id):
    match_id = Employee.objects.get(pk=id)
    match_id.delete()
    return redirect('/')    


# update data
def edit(request,id):
    if request.method=="POST":
        data = Employee.objects.get(pk=id)
        form = EmployeeForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            
    
    else:
        data = Employee.objects.get(pk=id)
        form = EmployeeForm(instance=data)


    context ={
        'data':form
    }
    return render(request,'update.html',context)
    