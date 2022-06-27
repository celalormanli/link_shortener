from django.db import models


class Link(models.Model):
    main_link = models.URLField(max_length=250)
    shorted_link=models.CharField(max_length=10, unique=True)
 