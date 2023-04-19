from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField("Название задания", max_length=550)
    is_complete = models.BooleanField("Задание завершено",default=False)
    user = models.CharField('Name',max_length=25)

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"


    def __str__(self):
        return self.title
