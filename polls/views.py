from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Youre at the polls index")
def detail(request, question_id):
    return HttpResponse("Youre looking at question %s." % question_id)

def results(request, question_id):
    response = "Youre looking at the results of questions %s."
    return HttpResponse( response % question_id)

def vote(request, question_id):
    return HttpResponse("Youre voting on question %s." % question_id)

# Create your views here.
