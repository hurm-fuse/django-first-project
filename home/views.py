from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message_text, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
        return redirect('/')
    contacts = Contact.objects.values_list('name', flat=True)
    context = {
        'price': "$10,000",
        'contact': contacts
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def buy(request):
    return render(request, 'buy.html')
