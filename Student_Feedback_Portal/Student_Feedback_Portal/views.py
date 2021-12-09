from django.shortcuts import render,redirect

# Create your views here.
def userVerify(request):
    if request.user.groups.filter(name="Teachers").exists():
        return redirect('feedback_result_noBatch')
    else:
        return redirect('feedback_page' )

def homePage(request):
    return render(request,'homepage.html')
