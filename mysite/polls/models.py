from django.db import models

class To_do_list(models.Model):
    to_do_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    deadline = models.DateTimeField('deadline')


class Done_list(models.Model):
    done_text = models.CharField(max_length=100)

