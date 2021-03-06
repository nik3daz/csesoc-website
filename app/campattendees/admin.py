from django.contrib import admin
from app.campattendees.models import Application
from app import campglobals

class ApplicationAdmin(admin.ModelAdmin):
  list_filter = ('year','shirt_size','gender', 'payment_status', 'medical_form')
  list_display = ('full_name', 'cse_username', 'gender', 'age', 'cse_program','shirt_size','payment_status', 'medical_form', 'year')
  actions = [campglobals.mark_depositpaid, campglobals.mark_arcpaid, campglobals.mark_fullpaid, campglobals.mark_medicalyes]

admin.site.register(Application, ApplicationAdmin)
