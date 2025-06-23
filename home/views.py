from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib.messages import constants as messages
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        'variable':"this is sent",
        'variable2': "this is var 2"
    }
    # return HttpResponse("this is homepage")
    # messages.success(request, "this is a test message")
    return render(request,'index.html',context)

def about(request):
    # return HttpResponse("this is about page")
    return render(request,'about.html' )

def services(request):
    # return HttpResponse("this is services page")
    return render(request,'services.html' )


def contact(request):
    # return HttpResponse("this is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email = email, phone = phone, message = message ,
                           date = datetime.today())
        contact.save()
        messages.success(request, "Message successfully sent!")

    return render(request,'contact.html' )

def index(request):
    images_with_text = [
        ("/static/choco_truffle.jpg", "Our signature chocolate truffle — rich, moist, and irresistible. A perfect treat for all occasions!"),
        ("/static/red_velvet.jpg", "Classic red velvet layered with cream cheese frosting — a smooth, velvety experience in every bite."),
        ("/static/strawberry.jpg", "A delightful strawberry cream cake topped with fresh berries and a soft sponge base."),
        ("/static/mocha.jpg", "Coffee-infused sponge layered with mocha cream — for the caffeine lovers with a sweet tooth!"),
        ("/static/butterscotch.jpg", "Butterscotch caramel cake, drizzled with rich sauce and crunchy toffee chunks."),
        ("/static/pineapple.jpg", "Pineapple sunshine cake with tropical flavors and light cream — a refreshing taste of summer."),
    ]
    return render(request, 'index.html', {'images_with_text': images_with_text})




