from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm
from .models import Contact
from django.contrib import messages


def index(request):
    # contact_list = Contact.objects.all()

    # context = {
    #     "contact_list": contact_list,

    # }
    return render(request, 'home/index.html')


def contactFormHandle(request):
    recieved = 0
    if request.method == 'POST':
        recieved = 1
        print("Form Recieved")
        form = ContactForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have successfully submitted your message')
        else:
            messages.error(
                request, 'Error submitting your message.Please correct the message first.')

    context = {
        "form": ContactForm()
    }
    return context


def contact(request):

    context = {
        "form": contactFormHandle(request)
    }
    return render(request, 'home/contact.html', context)


def about(request):

    return render(request, 'home/about.html')


def blog(request):
    return render(request, 'home/blog.html')


def shop(request):
    return render(request, 'home/shop.html')
