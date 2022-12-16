# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import uuid
from django.db import models


class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def uuid(self):
        return self.id