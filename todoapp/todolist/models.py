from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField("Название задания", max_length=550)
    is_complete = models.BooleanField("Задание завершено",default=False)
    

    def __str__(self):
        return self.title
