from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def second(request):
    data = request.POST['fname']
    
    return render(request, 'second.html',{"data":data})