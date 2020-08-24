from django.db import models
from django.contrib.auth.models import User
from videos.models import Course

class Thread(models.Model):
    course=models.OneToOneField(Course,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=200)
    description=models.TextField()
    date_created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_latest_date(self):
        if self.reply_set.count()>0:
            return self.reply_set.latest('date_created').date_created
            
        return self.date_created



class Reply(models.Model):
    thread=models.ForeignKey(Thread,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.TextField()
    date_created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username