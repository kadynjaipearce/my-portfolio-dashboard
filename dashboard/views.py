from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.db import models
from .models import posts_collection, projects_collection
import json
from bson import ObjectId
from datetime import datetime

class project:
  def __init__(self, slug, img, title, body, category, githubUrl, websiteUrl, techStack=None):
    if techStack is None:
            techStack = []
    self.slug = slug
    self.img = img
    self.title = title
    self.body = body
    self.category = category
    self.githubUrl = githubUrl
    self.websiteUrl = websiteUrl
    self.techStack = techStack
    self.createdAt = datetime.utcnow()

# Create your views here.
def dashboard(request):
  if request.user.is_authenticated:
    X = 12
    return render(request, "base.html", {"x": X})
  else: 
    return redirect("/")

def add_project(request):
  records = project(slug="skibidi", img="toilet", title="Skibidi", body="asydgaiyjsdhjyugaw", category="Web Development", githubUrl="asdsdas", websiteUrl="asdiyughadsygu", techStack=["React", "Typescript"])
  posts_collection.insert_one(records.__dict__)
  return HttpResponse("New Person Added")

def update_field(request):
   projects_collection.update_one()

def json_encoder(obj):
    if isinstance(obj, (ObjectId, datetime)):
        return str(obj)
    raise TypeError("Object of type {} is not JSON serializable".format(type(obj)))

def get_projects(request):
    projects = list(projects_collection.find())
    project_list = [project for project in projects]
    return HttpResponse(project_list)