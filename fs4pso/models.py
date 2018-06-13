# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
	name = models.CharField(max_length=10, verbose_name='작성자', default=' ')
	good_points = models.TextField(verbose_name='좋았던 점', default=' ')
	improving_points = models.TextField(verbose_name='개선되었으면 하는 점', default=' ')
	another_points = models.TextField(verbose_name='하고싶은 말', default=' ')
	created_date = models.DateTimeField(auto_now=True)

	def publish(self):
		self.created_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name
