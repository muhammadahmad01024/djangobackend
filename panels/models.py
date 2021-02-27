from jsonfield import JSONField
from django.db import models


# Create your models here.
class PanelComments(models.Model):
    id = models.AutoField(primary_key=True)
    panelName = models.CharField(max_length=200)
    rowId = models.IntegerField()
    commentText = models.CharField(max_length=2000)


class Headers(models.Model):
    data = JSONField(max_length=100000000)


class Reporting(models.Model):
    data = JSONField(max_length=100000000)


class IssueLog(models.Model):
    data = JSONField(max_length=100000000)


class FinancialCrime(models.Model):
    data = JSONField(max_length=100000000)


class News(models.Model):
    data = JSONField(max_length=100000000)


class UpcomingRegulations(models.Model):
    data = JSONField(max_length=100000000)
