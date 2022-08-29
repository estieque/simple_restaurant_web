from django.contrib import admin

from reservation.models import Reservation

# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'total_person', 'date', 'time', 'message',)
    search_fields = ('name', 'email',)

admin.site.register(Reservation, ReservationAdmin)