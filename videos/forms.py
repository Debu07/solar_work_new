from django.forms import ModelForm
from .models import Course,Lesson

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields='__all__'
        exclude=['date_posted',]
                                     
class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields='__all__'
                