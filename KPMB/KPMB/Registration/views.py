from django.shortcuts import render
from Registration.models import Course

# Create your views here.
def index(request):
    return render(request,'index.html')

def new_course(request):
    if request.method == 'POST':
        course_code = request.POST['code']
        course_desc = request.POST['desc']
        data=Course(code=course_code,description=course_desc)
        data.save()
        dict = {
            'message':'DATA IS SAVE BRO !!!!!'
        }
    else:
        dict = {
            'message':''
        }
        
    return render(request,'new_course.html',dict)

def course(request):
    allcourse=Course.objects.all()
    dict={
        'allcourse':allcourse
    }
    return render (request,'course.html',dict)