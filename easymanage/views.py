from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.db.models import Sum

now = timezone.now()
def home(request):
   return render(request, 'easymanage/home.html',
                 {'easymanage': home})

def about(request):
    return render(request, 'easymanage/AboutUs.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'easymanage/password_change_form.html', {
        'form': form
    })


@login_required
def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'easymanage/customer_list.html',
                 {'customers':customer})

@login_required
def customer_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            newcustomer = form.save(commit=False)
            newcustomer.created_date = timezone.now()
            newcustomer.save()
            customer = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'easymanage/customer_list.html',
                          {'customers': customer})
    else:
        form = CustomerForm()
    # print("Else")
    return render(request, 'easymanage/customer_new.html', {'form': form})




@login_required
def customer_edit(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   if request.method == "POST":
       # update
       form = CustomerForm(request.POST, instance=customer)
       if form.is_valid():
           editcustomer = form.save(commit=False)
           editcustomer.updated_date = timezone.now()
           editcustomer.save()
           customer = Customer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'easymanage/customer_list.html',
                         {'customers': customer})
   else:
        # edit
       form = CustomerForm(instance=customer)
   return render(request, 'easymanage/customer_edit.html', {'form': form})

@login_required
def customer_delete(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   customer.delete()
   return redirect('easymanage:customer_list')


@login_required
def customerservice_list(request):
    customerservice = CustomerService.objects.filter(created_date__lte=timezone.now())
    return render(request, 'easymanage/customerservice_list.html',
                 {'customerservices':customerservice})

@login_required
def customerservice_new(request):
    if request.method == "POST":
        form = CustomerServiceForm(request.POST)
        if form.is_valid():
            newcustomerservice = form.save(commit=False)
            newcustomerservice.created_date = timezone.now()
            newcustomerservice.save()
            customerservice = CustomerService.objects.filter(created_date__lte=timezone.now())
            return render(request, 'easymanage/customerservice_list.html',
                          {'customerservices': customerservice})
    else:
        form = CustomerServiceForm()
    # print("Else")
    return render(request, 'easymanage/customerservice_new.html', {'form': form})



@login_required
def customerservice_edit(request, pk):
   customerservice = get_object_or_404(CustomerService, pk=pk)
   if request.method == "POST":
       # update
       form = CustomerServiceForm(request.POST, instance=customerservice)
       if form.is_valid():
           editcustomerservice = form.save(commit=False)
           editcustomerservice.updated_date = timezone.now()
           editcustomerservice.save()
           customerservice = CustomerService.objects.filter(created_date__lte=timezone.now())
           return render(request, 'easymanage/customerservice_list.html',
                         {'customerservices': customerservice})
   else:
        # edit
       form = CustomerServiceForm(instance=customerservice)
   return render(request, 'easymanage/customerservice_edit.html', {'form': form})



@login_required
def customerservice_delete(request, pk):
   customerservice = get_object_or_404(CustomerService, pk=pk)
   customerservice.delete()
   return redirect('easymanage:customerservice_list')


@login_required
def roomstatus_list(request):
    roomstatus = RoomStatus.objects.filter(created_date__lte=timezone.now())
    return render(request, 'easymanage/roomstatus_list.html',
                 {'roomstatuss':roomstatus})


@login_required
def roomstatus_new(request):
    if request.method == "POST":
        form = RoomStatusForm(request.POST)
        if form.is_valid():
            newroomstatus = form.save(commit=False)
            newroomstatus.created_date = timezone.now()
            newroomstatus.save()
            roomstatus = RoomStatus.objects.filter(created_date__lte=timezone.now())
            return render(request, 'easymanage/roomstatus_list.html',
                          {'roomstatuss': roomstatus})
    else:
        form = RoomStatusForm()
    # print("Else")
    return render(request, 'easymanage/roomstatus_new.html', {'form': form})

@login_required
def roomstatus_edit(request, pk):
   roomstatus = get_object_or_404(RoomStatus, pk=pk)
   if request.method == "POST":
       # update
       form = RoomStatusForm(request.POST, instance=roomstatus)
       if form.is_valid():
           editroomstatus = form.save(commit=False)
           editroomstatus.updated_date = timezone.now()
           editroomstatus.save()
           roomstatus = RoomStatus.objects.filter(created_date__lte=timezone.now())
           return render(request, 'easymanage/roomstatus_list.html',
                         {'roomstatuss': roomstatus})
   else:
        # edit
       form = RoomStatusForm(instance=roomstatus)
   return render(request, 'easymanage/roomstatus_edit.html', {'form': form})


@login_required
def roomstatus_delete(request, pk):
   roomstatus = get_object_or_404(RoomStatus, pk=pk)
   roomstatus.delete()
   return redirect('easymanage:roomstatus_list')


@login_required
def summary(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customers = Customer.objects.filter(created_date__lte=timezone.now())
    customerservices = CustomerService.objects.filter(customer_name=pk)
    sum_service_charge = CustomerService.objects.filter(customer_name=pk).aggregate(Sum('service_charge'))
    return render(request, 'easymanage/summary.html', {'customers': customers,
                                                      'customerservices': customerservices,
                                                      'sum_service_charge': sum_service_charge,})
