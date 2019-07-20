from django.db import models

class Todo(models.Model):
    complete = models.BooleanField(default=False)
    text = models.CharField(max_length=20)

    def __str__(self):
        return self.text
