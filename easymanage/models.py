from django.db import models
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(auto_created=True,primary_key=True,max_length=6,)
    customer_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    contact_details = models.CharField(max_length=50)
    customer_stay_start_date = models.DateField()
    customer_stay_end_date = models.DateField()
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer_name)

category = (
        ('Food', "Food"),
        ('Beverages', "Beverages"),
        ('Food&Beverages', "Beverages"),
        ('MaintenanceCost', "MaintenanceCost"),
)

class CustomerService(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='services')
    service_category = models.CharField(max_length=10,choices=category, default='Food')
    description = models.TextField()
    location = models.CharField(max_length=200)
    service_consumption_date = models.DateField(auto_now_add=True)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer_name)

roomtype = (
        ('--' ,"--" ),
        ('Deluxe', "Deluxe"),
        ('Executive', "Executive"),
        ('Suite', "Suite"),
)
class RoomStatus(models.Model):
    room_no = models.IntegerField()
    room_type=models.CharField(max_length=10,choices=roomtype,default=False)
    room_description=models.TextField()
    room_availability=models.BooleanField(default=False)
    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.room_no)