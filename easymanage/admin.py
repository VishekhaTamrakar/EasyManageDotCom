from django.contrib import admin

from .models import Customer,CustomerService,RoomStatus

class CustomerList(admin.ModelAdmin):
    list_display = ( 'customer_id', 'customer_name')
    list_filter = ( 'customer_id', 'customer_name')
    search_fields = ('customer_id','customer_name')
    ordering = ['customer_id']

admin.site.register(Customer,CustomerList)

class ServiceList(admin.ModelAdmin):
    list_display = ( 'customer_name', 'service_category')
    list_filter = ( 'customer_name','service_category')
    search_fields = ('customer_name','service_category')
    ordering = ['customer_name']

admin.site.register(CustomerService,ServiceList)


class RoomList(admin.ModelAdmin):
    list_display = ( 'room_no', 'room_availability')
    list_filter = ( 'room_no','room_availability')
    search_fields = ('room_no','room_availability')
    ordering = ['room_no']

admin.site.register(RoomStatus,RoomList)