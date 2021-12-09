from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from students_app.models import Questions
from students_app.models import Feedback
from students_app.forms import feedbackForm
from django.contrib import messages

# Create your views here.
def redirectToLogin(request):
    return redirect('students_login')

def FeedBackForm(request,prof_name):

    if request.user.username == "AnonymousUser":
        messages.success(request,("Please login as students to continue"))
        return redirect('students_login')

    questions = Questions.objects.all()
    if request.method=='POST':
        post = request.POST.copy()
        user = post['batch']
        number = 0
        batch = ""
        for i in user:
            number+=1
            batch+=i
            if number==4:
                break
        post['batch'] = batch
        try:
            feedback = Feedback.objects.get(professor= post['professor'] ,batch = batch)

            # for i in post['response1']:
            #     post['response1'] = chr(i + feedback.response2)
            #     break
            post['response1'] = str(ord(post['response1'][0]) - 48 + feedback.response1)
            post['response2'] = str(ord(post['response2'][0]) - 48 + feedback.response2)
            post['response3'] = str(ord(post['response3'][0]) - 48 + feedback.response3)
            post['response4'] = str(ord(post['response4'][0]) - 48 + feedback.response4)
            post['response5'] = str(ord(post['response5'][0]) - 48 + feedback.response5)
            request.POST = post
            form = feedbackForm(request.POST,instance=feedback)
            #messages.success(request,("Idhar aaya tha ")) #+str(type(post['response1'])) +str(ord(post['response1'][0])) + str(type(feedback.response1))))
        except Exception as e:
            request.POST = post
            # messages.success(request,(str(e)))
            form = feedbackForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,("Updated Successfully"))
        else:
            messages.success(request,("Error in the form!"))    
        # form.fields['professor'] = post['prof_name']
        # form.fields['batch'] = post['username']
        # total_index = Questions.objects.count()
        # response = ""
        # for Question in questions:
        #     response += str(post.get(Question.question))

        # for i in range(total_index):
        #     if post[chr(i+1)]:
        #         response+= str(post[chr(i+1)])
        #     else:
        #         response+='0'
        
    
    users = User.objects.filter(groups__name='Teachers')
    return render(request,'Feedback_form.html',{'user_list':users,'prof_name':prof_name,'questions':questions,'curr_user':request.user,'professor':True})

def noProfName(request):   
    questions = Questions.objects.all() 
    users = User.objects.filter(groups__name='Teachers')
    for Username in users:
        prof_name = Username.username
        break
    return render(request,'Feedback_form.html',{'user_list':users,'prof_name':prof_name,'questions':questions,'curr_user':request.user,'professor':False})
