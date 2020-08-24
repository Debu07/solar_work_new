from django.db import models
from django.urls import reverse

class Course(models.Model):
    slug=models.SlugField()
    title=models.CharField(max_length=100)
    description=models.TextField()
    thumbnail=models.ImageField()
    date_posted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('videos:detail',kwargs={'slug':self.slug})
        
    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')

class Lesson(models.Model):
    slug=models.SlugField()
    title=models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    position=models.IntegerField()
    video_file=models.FileField()
    date_posted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.title +" | "+ self.title

    def get_absolute_url(self):
        return reverse(
            'videos:lesson-detail',
            kwargs={
                'course_slug':self.course.slug,
                'lesson_slug':self.slug
                })
