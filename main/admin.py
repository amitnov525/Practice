from django.contrib import admin
from main.models import Student

# Register your models here.
@admin.register(Student)
class StudentDisplay(admin.ModelAdmin):
    list_display=['id','name','rollno','city']

