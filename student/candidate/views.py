from django.shortcuts import render
from candidate.models import Profile
from datetime import datetime
# Create your views here.

def info(req):
    all_students = Profile.objects.all()
    d = datetime.now()
    return render(req, 'candidate/all.html', {"students": all_students})


def activity(req):
    return render(req, 'candidate/act.html')