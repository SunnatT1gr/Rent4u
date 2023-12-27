from django.shortcuts import render
from django.views.generic import TemplateView

def homeview(request):
    return render(request, 'index.html')

class ContactView(TemplateView):
    template_name = 'contact.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class BlogView(TemplateView):
    template_name = 'blog.html'
    
class CarView(TemplateView):
    template_name = 'car.html'
