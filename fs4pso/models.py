# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	subject = 
	name = models.CharField(max_length=10, verbose_name='작성자')
	good_points = TextField(verbose_name='좋았던 점')
	improving_points = TextField(verbose_name='개선되었으면 하는 점')
	another_points = models.TextField(verbose_name='하고싶은 말')
	created_date = models.DateTimeField(auto_now=True)

class Subject(models.Model):
	subject = models.CharField(max_length=20, verbose_name='과목')