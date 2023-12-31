from django.contrib import admin

# Register your models here.
from .models import Category, Location,Bus,Schedule,Booking,Customer


admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Bus)
admin.site.register(Schedule)
admin.site.register(Booking)
admin.site.register(Customer)

