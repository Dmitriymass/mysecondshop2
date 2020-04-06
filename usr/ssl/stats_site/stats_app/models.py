from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class User(models.Model):
    #id = models.PrimaryKey()
    #id = models.IntegerField()
    first_name =  models.CharField(max_length=200)
    last_name =  models.CharField(max_length=200)
    email =  models.CharField(max_length=200)
    gender =  models.CharField(max_length=10)
    ip_address =  models.CharField(max_length=20)

class Statistic(models.Model):
    #user_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    page_views = models.IntegerField()
    clicks = models.IntegerField()
