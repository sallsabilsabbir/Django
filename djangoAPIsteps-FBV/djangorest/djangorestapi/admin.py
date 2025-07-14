from django.contrib import admin
from . models import Aiquest

# Register your models here.
@admin.register(Aiquest)
#register sequentially so view as like this sequentially-
class AiquestAdmin(admin.ModelAdmin):
	list_display = ['id','teacher_name','course_name','course_duration','seat']
