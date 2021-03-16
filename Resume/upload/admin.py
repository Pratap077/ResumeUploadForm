from django.contrib import admin
from .models import Resume

# Register your models here.
@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
  list_displays=('id','name','dob','gender','locality','city','pin','state','email','mobile','job_city','profile_image','my_file')
