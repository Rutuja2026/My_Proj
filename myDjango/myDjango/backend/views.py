from django.shortcuts import render
from .models import Message
from django.contrib.auth.decorators import login_required

@login_required
def chat(request):
    return render(request, 'chat/chat.html')
