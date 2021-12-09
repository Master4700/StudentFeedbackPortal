from django.shortcuts import render,redirect
from students_app.models import Feedback,Questions
from teachers_app.models import Batches
# Create your views here.
def redirectToLogin(request):
    return redirect('teachers_login')

def feedbackresult(request,batch_year):
    questions = Questions.objects.all()
    batches = Batches.objects.all()
    Totalsum = 0
    try:
        feedbacks = Feedback.objects.get(professor=request.user,batch = batch_year)
        feedbacks.pk = None
        Totalsum = feedbacks.response1 + feedbacks.response2 + feedbacks.response3 + feedbacks.response4 + feedbacks.response5
        feedbacks.response1 = feedbacks.response1/Totalsum*3000
        feedbacks.response2 = feedbacks.response2/Totalsum*3000
        feedbacks.response3 = feedbacks.response3/Totalsum*3000
        feedbacks.response4 = feedbacks.response4/Totalsum*3000
        feedbacks.response5 = feedbacks.response5/Totalsum*3000
    except:
        feedbacks = None
    
    return render(request,'feedbackresult.html',{'feedback':feedbacks,'batch':True,'curr_user':request.user,'Batches':batches,'questions':questions,'TotalSum':Totalsum,'curr_batch':batch_year})

def feedbackresultNoBatch(request):
    feedbacks = None 
    batches = Batches.objects.all()
    return render(request,'feedbackresult.html',{'feedback':feedbacks,'batch':False,'curr_user':request.user,'Batches':batches})
