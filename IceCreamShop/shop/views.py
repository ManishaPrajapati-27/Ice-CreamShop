from django.shortcuts import render, HttpResponse
from datetime import datetime
from shop.models import Contact

from django.contrib import messages
# from shop.models import Contact
# Create your views here.
def index(request):
    # return HttpResponse("This is Home Page")
    return render(request, 'index.html')
def about(request):
    # return HttpResponse("This is About Page")
    return render(request, 'about.html')
def blog(request):
    # return HttpResponse("This is Services Page")
    return render(request, 'blog.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent.')
    # return HttpResponse("This is Contact Page")
    return render(request, 'contact.html')
