from django.shortcuts import render,redirect
from.models import Employees


# Create your views here.

def show_employees(request):
    employees = Employees.objects.all()
    return render(request, 'webside/show_emp.html', {'employees': employees})

def add_employees(request):
    if request.method == 'POST':
        Employees.objects.create(name = request.POST.get('nm'),
        email = request.POST.get('em'),
        department = request.POST.get('dep'),
        age = request.POST.get('ag'),
        city = request.POST.get('ct'),
        salary = request.POST.get('sal'),
        phone = request.POST.get('pho'),
        pincode = request.POST.get('pin'))
        return redirect('show-employees')
    return render(request,template_name= 'webside/add_emp.html')

def edit_employees(request, eid):
    employee = Employees.objects.get(id=eid)
    if request.method == 'POST':
        employee.name = request.POST.get('na',employee.name)
        employee.email = request.POST.get('em',employee.email)
        employee.department = request.POST.get('dep',employee.department)
        employee.age = request.POST.get('ag',employee.age)
        employee.city = request.POST.get('ct',employee.city)
        employee.salary = request.POST.get('sal',employee.salary)
        employee.phone = request.POST.get('pho',employee.phone)
        employee.pincode = request.POST.get('pin',employee.pincode)

        # employee.name = name
        # employee.email = email
        # employee.department = department
        # employee.age = age
        # employee.city = city
        # employee.salary = salary
        # employee.phone = phone
        employee.save()
        return redirect('show-employees')
    return render(request, 'webside/edit_emp.html', {'employee': employee})

def delete_employees(request, eid):
    employee = Employees.objects.get(id=eid)
    if request.method == 'POST':
        employee.delete()
        return redirect('show-employees')
    return render(request, 'webside/delete_emp.html', {'employee': employee})



# def login_employees(request,eid):
#     if request.method == 'POST':
#          employee = Employees.objects.filter(employee.email)
