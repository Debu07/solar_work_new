from django.shortcuts import render
from django.views.generic import ListView,DetailView,View
from .models import Course,Lesson

class CourseListView(ListView):
    model=Course

class CourseDetailView(DetailView):
    model=Course

class LessonDetailView(View):

    def get(self,request,course_slug,lesson_slug,*args,**kwargs):

        course_query_set=Course.objects.filter(slug=course_slug)
        if course_query_set.exists():
            course=course_query_set.first()

        lesson_query_set=course.lessons.filter(slug=lesson_slug)
        if lesson_query_set.exists():
            lesson=lesson_query_set.first()
        context={'lesson':lesson}
        return render(request,'videos/lesson_detail.html',context)
