from django import forms
from students_app.models import Feedback

class  feedbackForm(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = ('professor','batch','response1','response2','response3','response4','response5')