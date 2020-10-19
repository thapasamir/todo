from django.db import models


class task(models.Model):
    work = models.CharField(max_length=100000, null=True)
    description = models.TextField(max_length=2000000, null=True)

    def __str__(self):
        return self.work
