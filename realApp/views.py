from itertools import count
from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    forums = forum.objects.all()
    count = forum.count()
    discussion = []
    for i in forum:
        discussion.append(i.discussion_set.all())

    context = {'forums':forums,
                'count':count,
                'discussions':discussions}
    return render(request,'home.html',context)
    