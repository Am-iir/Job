from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.contrib.auth import (
     authenticate, 
     get_user_model,
     login,
     logout,
)

from .forms import SignUpForm,JobForm
from accounts.forms import UserLoginForm
from .models import Job

# Create your views here.

def home(request):
  
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form. cleaned_data.get('password')
        user = authenticate(username=username , password=password)
        login(request,user)
        return redirect("/")
        

    return render(request,"home.html",{"form":form})

    # form = SignUpForm(request.POST or None)

    # if form.is_valid():
    #     instance= form.save(commit=False) 
    #     instance.save() #saves in database
    
    # context = {
    #     "form" : form,
    # }
    # return render(request,"home.html",context)

def about(request):
    
    return render(request,"about.html",{})

def post_job(request):
    form = JobForm(request.POST or None)
    if form.is_valid():
        instance= form.save(commit=False) 
        instance.save() #saves in database

        messages.success(request,"Sucessfully saved")
        return HttpResponseRedirect(reverse(home))        
    
    context = {
        "page":'Post',
        "form" : form,
    }
    return render(request,"post_job.html",context)

def job_list(request):
    queryset_list = Job.objects.all()
    
    query=request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 3) # Show contacts per page
    page_request_var="page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    
    context = {
        "object_list": queryset,
        "title":"Jobs Available",
        "page_request_var":page_request_var,
    }

    return render(request,"job_list.html",context)

def job_detail(request,id=None): #Detail retrieve  

   instance =get_object_or_404(Job , id=id)
   context = {       
      "title":instance.title,
      "instance":instance
   }
   return render(request,"job_detail.html",context)

def user_posted(request,id=None): #Detail retrieve  

   instance =get_object_or_404(Job , id=id)
   context = {       
      "title":instance.title,
      "instance":instance
   }
   return render(request,"user_posted.html",context)

def job_update(request,id=None): #Update
   
   instance =get_object_or_404(Job, id=id)
   form=JobForm(request.POST or None, instance=instance)
   if form.is_valid():
      instance=form.save(commit=False)      
      instance.save()        
      
   context = {
        "page":'Update',
      "title":instance.title,
      "instance":instance,
      "form" : form,
   }
   return render(request,"post_job.html",context)

def job_delete(request, id=None): #Delete
   
   instance =get_object_or_404(Job, id=id)
   instance.delete()   
   return redirect("job_list")

def user_list(request, username=None):
    if not username:
        username = request.user.username
    latest_list = Job.objects.filter(company_name=username).order_by('-timestamp')
    context = {'latest_list':latest_list, 'username':username}
    return render(request, 'user_list.html', context)
    

