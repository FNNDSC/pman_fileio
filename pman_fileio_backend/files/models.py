
from django.db import models


class FileUpload(models.Model):
    fname = models.FileField(max_length=200)

    def __str__(self):
        return self.fname.name   


