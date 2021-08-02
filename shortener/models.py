from django.db import models

# Create your models here.
class Data(models.Model):
    link=models.CharField(max_length=800)
    uuid=models.CharField(max_length=9)

    def __str__(self):
        return self.uuid
