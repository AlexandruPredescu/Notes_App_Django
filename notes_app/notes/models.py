from django.db import models


# Create your models here.

class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Note(MyModel):
    class Meta:
        db_table = 'notes'

    title = models.CharField(max_length=200)
    text = models.TextField()





