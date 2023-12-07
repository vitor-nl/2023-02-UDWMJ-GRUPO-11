from django.shortcuts import render

# Create your views here.

def home(request):
    template_name ='../templates/base.html'
    context = {}
    return render(request, template_name, context)
