from django.http import HttpResponse

def homepage(request):
    return HttpResponse("HomePage")

def about(request):
    return HttpResponse("About")