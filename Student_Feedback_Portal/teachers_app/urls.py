from django.urls import path,include
from django.contrib.auth import views as auth_views
from teachers_app import views as teachers_views


urlpatterns = [
    path('',teachers_views.redirectToLogin,name = "redirectToLogin_Teachers"),
    path('login',auth_views.LoginView.as_view(template_name = 'teachers_login.html'),name='teachers_login'),
    path('feedbackresult/<batch_year>',teachers_views.feedbackresult,name='feedback_result'),
    path('feedbackresult',teachers_views.feedbackresultNoBatch,name='feedback_result_noBatch'),
    path('logout',auth_views.LogoutView.as_view(template_name='teacher_logout.html'),name='teacher_logout')


#     path('register',views.register, name='register'),
#     path('login',auth_views.LoginView.as_view(template_name = 'login.html'),name='login'),
#     path('logout',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout')
]