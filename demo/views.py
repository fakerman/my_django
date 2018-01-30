from django.shortcuts import render
from .models import UserMessage


# Create your views here.
def getform(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        message = request.POST.get('message', '')

        um = UserMessage()
        um.name = name
        um.email = email
        um.address = address
        um.message = message
        um.save()

    return render(request, 'form.html')
