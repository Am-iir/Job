from django.contrib import admin

# Register your models here.
from .models import SignUp, Job

class SignUpAdmin(admin.ModelAdmin):
    list_display= ["full_name", "email" ,"timestamp"]
    class Meta:        
        model = SignUp

admin.site.register(SignUp , SignUpAdmin)

class JobUp(admin.ModelAdmin):
    list_display = ["title", "company_name" , "description", "timestamp"]
    class Meta:        
        model = Job
admin.site.register(Job , JobUp)
 