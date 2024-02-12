from django.shortcuts import render, HttpResponse, redirect

def login(request):
    if (request.user.is_authenticated):
      return redirect("/dashboard")
    else:
      return render(request, "base.html", {})
