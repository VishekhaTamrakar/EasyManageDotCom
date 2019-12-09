from django import forms
from .models import Customer,CustomerService,RoomStatus

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_id', 'customer_name', 'city', 'state', 'zipcode', 'contact_details','email_address', 'customer_room_no', 'customer_stay_start_date', 'customer_stay_end_date')

class CustomerServiceForm(forms.ModelForm):
    class Meta:
        model = CustomerService
        fields = ('customer_name','service_category','description','service_consumption_date','service_charge')

class RoomStatusForm(forms.ModelForm):
    class Meta:
        model = RoomStatus
        fields = ('room_type','room_no','room_description','room_availability')