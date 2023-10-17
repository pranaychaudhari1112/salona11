# views.py
from django.shortcuts import render, redirect
from .models import saloona,business


def front(request):
    return render(request,'front.html')


def list_business1(request):
    business = saloona.objects.all()
    context = {"business1": business}
    return render(request,'list_your_bisness.html',context)



def ADD(request):
    if request.method == 'POST':
        yourbusiness = request.POST.get('yourbusiness')
        yourname = request.POST.get('yourname')
        mobilenumber = request.POST.get('mobilenumber')
        emailaddress = request.POST.get('emailaddress')
        business = request.POST.get('business')


        slon = saloona(
            name=yourbusiness,
            email=yourname,
            massege=mobilenumber,
            phone=emailaddress,
            business=business
        )
        slon.save()
        return redirect('index')


# CRUD OPRETION BASIC

def index(request):
    saloona1 = saloona.objects.all()
    context = {"saloona1": saloona1}
    return render(request, 'index.html', context)

def ADD(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        massege = request.POST.get('massege')
        phone = request.POST.get('phone')

        slon = saloona(
            name=name,
            email=email,
            massege=massege,
            phone=phone
        )
        slon.save()
        return redirect('index')  # Redirect to the index view after adding a record

    return redirect(request, "index.html")  # This should be `render` instead of `redirect`

def Edit(request):
    # This view should render the "editEmployeeModal" for editing an employee record
    # You need to pass the specific employee data to the template
    return render(request, 'editEmployeeModal.html')  # Create a new template for editing

def Update(request, id):
    if request.method == 'POST':
        # Retrieve the existing record by ID and update it
        slon = saloona.objects.get(id=id)
        slon.name = request.POST.get('name')
        slon.email = request.POST.get('email')
        slon.massege = request.POST.get('massege')
        slon.phone = request.POST.get('phone')
        slon.save()
        return redirect('index')

def Delete(request, id):
    saloona1 = saloona.objects.get(id=id)
    saloona1.delete()
    context={
        "saloiona1":saloona1
    }

    return redirect('index')
