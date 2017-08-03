from django.db import models
from datetime import datetime, time, date
# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(null=True, blank=True) #can add 'default=time(16, 00)'

    def __str__(self):
        return self.title

    #### Order by earlier date
    class Meta:
        ordering = ("date",)

    @property
    def is_past_due(self):
        if date.today() > self.date:
            return True
        return False

    # @property
    # def past_time(self):
    #     time_now = datetime.now().strftime('%I:%M %p')
    #     if time_now > self.time:
    #         return True
    #     return False
