# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Z_Restaurant, Recipe




## need to register tables where information of Z_Restaurant and Recipe are stored
## tables can be seen at project/project/database/models.py

admin.site.register(Z_Restaurant)
admin.site.register(Recipe)
# Register your models here.


