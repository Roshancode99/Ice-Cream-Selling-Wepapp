from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable' : "This is Roshans website!"
    }
    return render(request , 'index.html')
    #return HttpResponse("This is Home Page!")

def about(request):
    return render(request , 'about.html')

def services(request):
    return render(request , 'services.html')

def contacts(request):
    return render(request , 'contacts.html')