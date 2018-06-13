# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def to_index(request): # urls.py에서 request를 받아 index.html을 보여줌
    return render(request, 'fs4pso/index.html', {})
