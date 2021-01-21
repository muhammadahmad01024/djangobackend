from django.db import models


# Create your models here.
class PanelComments(models.Model):
    id = models.AutoField(primary_key=True)
    panelName = models.CharField(max_length=200)
    rowId = models.IntegerField()
    commentText = models.CharField(max_length=2000)
