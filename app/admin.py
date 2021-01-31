from django.contrib import admin
from .models import studentData, parentData, doctorData, login, testData

# Register your models here.
admin.site.register(studentData)
admin.site.register(parentData)
admin.site.register(doctorData)
admin.site.register(testData)
admin.site.register(login)