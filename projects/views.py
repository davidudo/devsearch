from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from .utils import searchProjects, paginateProjects

# Create your views here

def projects(request):
  projects, search_query = searchProjects(request)
  
  projects, custom_range = paginateProjects(request, projects, 6)
  
  context = { 
    'projects': projects, 
    'search_query': search_query,
    'custom_range': custom_range,
  }
  return render(request, 'projects/projects.html', context)
  
def project(request, pk):
  projectObj = Project.objects.get(id = pk)
  form = ReviewForm()
  
  print(projectObj.imageURL)

  if request.method == 'POST':
    form = ReviewForm(request.POST)
    review = form.save(commit=False)
    review.project = projectObj
    review.owner = request.user.profile
    review.save()

    projectObj.getVoteCount

    messages.success(request, 'Your review was successfully submitted!')
  
  context = { 'project': projectObj, 'form': form }
  return render(request, 'projects/single_project.html', context)
  
@login_required(login_url = "login")
def createProject(request):
  profile = request.user.profile
  form = ProjectForm()
  
  if request.method == 'POST':
    # print(request.POST)
    form = ProjectForm(request.POST, request.FILES)
    newtags = request.POST.get('newtags').replace(',',  " ").split()
    if form.is_valid():
      project = form.save(commit = False)
      project.owner = profile
      project.save()
      
      for tag in newtags:
        tag, created = Tag.objects.get_or_create(name=tag)
        project.tags.add(tag)
        
      messages.success(request, 'Project successfully created!')
    
      return redirect('account')
   
  context = { 'form': form }
  return render (request, 'projects/project_form.html', context)

@login_required(login_url = "login")
def updateProject(request, pk):
  profile = request.user.profile
  project = profile.project_set.get(id = pk)
  form = ProjectForm(instance = project)
  
  if request.method == 'POST':
    # print(request.POST)
    form = ProjectForm(request.POST, request.FILES, instance = project)
    newtags = request.POST.get('newtags').replace(',',  " ").split()
    if form.is_valid():
      form.save()
      
      for tag in newtags:
        tag, created = Tag.objects.get_or_create(name=tag)
        project.tags.add(tag)
        
      messages.success(request, 'Project was successfully updated!')
        
      return redirect('account')
  
  context = { 'form': form, 'project': project }
  return render (request, 'projects/project_form.html', context)

@login_required(login_url = "login")
def deleteProject(request, pk):
  project = Project.objects.get(id = pk)
  
  if request.method == 'POST':
    project.delete()
    messages.success(request, 'Project was successfully deleted!')
    return redirect('account')
  
  context = { 'object': project }
  return render(request, 'delete_template.html', context)