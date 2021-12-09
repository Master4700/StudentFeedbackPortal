from django.urls import path,include
from django.contrib.auth import views as auth_views
from students_app import views as student_views

urlpatterns = [
    path('',student_views.redirectToLogin,name = "redirectToLogin_students"),
    path('login',auth_views.LoginView.as_view(template_name = 'student_login.html'),name='students_login'),
    path('FeedbackSubmission', student_views.noProfName, name = "feedback_page"),
    path('FeedbackSubmission/<prof_name>',student_views.FeedBackForm,name='feedback_page_with_Name'),
    path('logout', auth_views.LogoutView.as_view(template_name='student_logout.html'), name='student_logout')

    # path('response/<prof_name>',student_views.profReview,name='professor_feedback')

#     path('register',views.register, name='register'),
#     path('login',auth_views.LoginView.as_view(template_name = 'login.html'),name='login'),
#     path('logout',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout')
]