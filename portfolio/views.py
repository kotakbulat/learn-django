# portfolio/views.py
from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactForm
from django.core.mail import send_mail # Example: for sending email (requires email backend setup in settings.py)
from django.conf import settings

def project_list(request):
    projects = Project.objects.all() # Fetch all Project objects from DB
    context = {'projects': projects}
    return render(request, 'portfolio/project_list.html', context) # Render template

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Example: Print to console (In real app, send email or save to DB)
            print(f"Contact Form Submission:")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Message: {message}")

            # Optional: Send email (needs EMAIL_BACKEND configured in settings.py)
            # try:
            #     send_mail(
            #         f"Contact Form Message from {name}",
            #         message,
            #         email, # From email
            #         [settings.DEFAULT_FROM_EMAIL], # To email (e.g., your admin email)
            #         fail_silently=False,
            #     )
            # except Exception as e:
            #     print(f"Error sending email: {e}") # Handle error appropriately

            return redirect('contact_success') # Redirect after POST
    else:
        form = ContactForm() # Create blank form for GET request

    context = {'form': form}
    return render(request, 'portfolio/contact.html', context)

def contact_success(request):
    return render(request, 'portfolio/contact_success.html')