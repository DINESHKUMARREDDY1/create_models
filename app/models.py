from django.db import models

# Create your models here.
class topic(models.Model):
    topic_name=models.CharField(max_length=50,primary_key=True)


class webpage(models.Model):
    topic_name=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    url=models.URLField()


class access_records(models.Model):
    topic_name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=50)