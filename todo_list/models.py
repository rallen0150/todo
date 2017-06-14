from django.db import models

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("date",)
