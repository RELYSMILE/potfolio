from django.shortcuts import render, redirect
from .models import Home,About,Profile,Category,Portfolio, ContactMessage
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    home = Home.objects.latest('updated')
    about = About.objects.latest('updated')
    profile = Profile .objects.filter(about = about)
    categories = Category.objects.all()
    portfolio = Portfolio.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_message = ContactMessage(name=name, email=email, message=message)
        contact_message.save()

        # subject = 'Contact Form Submission'
        # email_message = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        # from_email = settings.DEFAULT_FROM_EMAIL
        # to_email = 'your-email@example.com'  # Replace with your email address
        # send_mail(subject, email_message, from_email, [to_email])


        if contact_message.save() == None:
            messages.success(request,"Your message has been submitted successfully")
            return redirect('index') 
        else:
            messages.error(request,"Message not submitted, try again")
            return redirect('index') 
        
    context = {
        'home': home,
        'about': about,
        'profile': profile,
        'categories': categories,
        'portfolio': portfolio,
    }
    return render(request, 'daberechi/index.html', context)