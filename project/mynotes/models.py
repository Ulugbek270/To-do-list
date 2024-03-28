from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('Name', max_length=60)
    description = models.TextField('Description', max_length=255, null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField('Date', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

