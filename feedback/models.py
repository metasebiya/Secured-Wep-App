from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Feedbacks(models.Model):
    class Meta:
        db_table = 'feedbacks'

    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to='feedback/documents/', blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    def get_absolute_url(self):
        return reverse('post_detail_view', kwargs={'pk': self.pk})
